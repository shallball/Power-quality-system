import random,threading,math,sys,os,signal,datetime
import serial,crcmod,time
def convert_int(string):
	res = []
	result = []
	for item in string:
		res.append(item)
	for i in res:
		result.append(int(i))
	return result

def harmonic_int(string):
	res = []
	result = []
	harmonics=[]
	for item in string:
		res.append(item)
	for i in res:
		result.append(int(i))
	for i in range(16):
		harmonics.append((result[3+2*i]*16**2+result[4+2*i])*0.1)
	return harmonics
			
def data(t):
	global voltagesA,voltagesB,voltagesC
	voltageA=voltageA_valid*(2**0.5)*math.sin(100*math.pi*t+
	math.acos(B))
	voltageB=voltageB_valid*(2**0.5)*math.sin(100*math.pi*t+2*math.pi/3+
	math.acos(B))
	voltageC=voltageC_valid*(2**0.5)*math.sin(100*math.pi*t+4*math.pi/3+
	math.acos(B))
	voltagesA.insert(0,voltageA)
	voltagesB.insert(0,voltageB)
	voltagesC.insert(0,voltageC)
	del voltagesA[250]
	del voltagesB[250]
	del voltagesC[250]
	voltageA_max=max(voltagesA)
	voltageB_max=max(voltagesB)
	voltageC_max=max(voltagesC)
	voltageA_min=min(voltagesA)
	voltageB_min=min(voltagesB)
	voltageC_min=min(voltagesC)
	global voltageA_pp,voltageB_pp,voltageC_pp
	voltageA_pp="%.2f"%(voltageA_max-voltageA_min)
	voltageB_pp="%.2f"%(voltageB_max-voltageB_min)
	voltageC_pp="%.2f"%(voltageB_max-voltageC_min)

	global currentsA,currentsB,currentsC
	currentA=currentA_valid*(2**0.5)*math.sin(100*math.pi*t)
	currentB=currentB_valid*(2**0.5)*math.sin(100*math.pi*t+2*math.pi/3)
	currentC=currentC_valid*(2**0.5)*math.sin(100*math.pi*t+4*math.pi/3)
	currentsA.insert(0,currentA)
	currentsB.insert(0,currentB)
	currentsC.insert(0,currentC)
	del currentsA[250]
	del currentsB[250]
	del currentsC[250]
	currentA_max=max(currentsA)
	currentB_max=max(currentsB)
	currentC_max=max(currentsC)
	currentA_min=min(currentsA)
	currentB_min=min(currentsB)
	currentC_min=min(currentsC)
	global currentA_pp,currentB_pp,currentC_pp
	currentA_pp="%.2f"%(currentA_max-currentA_min)
	currentB_pp="%.2f"%(currentB_max-currentB_min)
	currentC_pp="%.2f"%(currentC_max-currentC_min)
	t=t+0.0004
	timer=threading.Timer(0.004,data,(t,))
	timer.start()	

def harmonic():				#谐波
	adresses={'0':[0x01,0x03,0x00,0xC9,0x00,0x10],
	'1':[0x01,0x03,0x01,0x2D,0x00,0x10],
	'2':[0x01,0x03,0x01,0x91,0x00,0x10],
	'3':[0x01,0x03,0x01,0xF5,0x00,0x10],
	'4':[0x01,0x03,0x02,0x59,0x00,0x10],
	'5':[0x01,0x03,0x02,0xBD,0x00,0x10]}
	name=[harmonicsA_U,harmonicsB_U,harmonicsC_U,harmonicsA_I,
	harmonicsB_I,harmonicsC_I]
	crc16=crcmod.mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)

	x=[]
	try:
		com=serial.Serial('com6',9600,timeout=0.5)
	except:
		pass
	for j in range(6):
		adress=adresses[str(j)]
		adress_b=bytes(adress)
		crc=crc16(adress_b)
		crc_l=crc%256
		crc_h=int((crc-crc_l)/256)				
		text=[1,3,adress[2],int(adress[3]),0,16,crc_l,crc_h]	
		text=bytes(text)
		try:
			com.write(text)
			x=com.read(37)
			x=harmonic_int(x)	
		except:
			x=name[j]
		for i in range(16):
			harmonic_name=name[j]
			harmonic_name[i]=float("%.1f"%(x[i]))
		time.sleep(0.5)

	

def voltage_deviation():	#电压偏差和频率偏差

	global column2,column3,column4
	global times_all,rowA5,rowA6,rowB5,rowB6,rowC5,rowC6
	times_all=times_all+1
	column2[0]="%.3f"%((float(voltageA_valid)-220)*100/220)
	column3[0]="%.3f"%((float(voltageB_valid)-220)*100/220)
	column4[0]="%.3f"%((float(voltageC_valid)-220)*100/220)
	if abs(float(column4[0]))>abs(float(column4[1])):
		column4[1]=column4[0]
	if abs(float(column2[0]))>abs(float(column2[1])):
		column2[1]=column2[0]
	if abs(float(column3[0]))>abs(float(column3[1])):
		column3[1]=column3[0]
	if float(column2[2])==0:
		column2[2]=column2[0]
	if float(column3[2])==0:
		column3[2]=column2[0]
	if float(column4[2])==0:
		column4[2]=column2[0]	
	if abs(float(column2[0]))<abs(float(column2[2])):
		column2[2]=column2[0]
	if abs(float(column3[0]))<abs(float(column3[2])):
		column3[2]=column3[0]
	if abs(float(column4[0]))<abs(float(column4[2])):
		column4[2]=column4[0]
	if float(column2[0])>95 or float(column2[0])<-95:
		column2[3]=column2[0]
	if float(column3[0])>95 or float(column3[0])<-95:
		column3[3]=column3[0]
	if float(column4[0])>95 or float(column4[0])<-95:
		column4[3]=column4[0]
	if float(column2[0])>7:
		rowA5=rowA5+1
	if float(column3[0])>7:
		rowB5=rowB5+1
	if float(column4[0])>7:
		rowC5=rowC5+1
	if float(column2[0])<-10:
		rowA6=rowA6+1
	if float(column3[0])<-10:
		rowB6=rowB6+1		
	if float(column4[0])<-10:
		rowC6=rowC6+1	
	column2[5]="%.3f"%(rowA5/times_all*100)
	column3[5]="%.3f"%(rowB5/times_all*100)
	column4[5]="%.3f"%(rowC5/times_all*100)
	column2[6]="%.3f"%(rowA6/times_all*100)
	column3[6]="%.3f"%(rowB6/times_all*100)
	column4[6]="%.3f"%(rowC6/times_all*100)
	column2[4]="%.3f"%((times_all-rowA5-rowA6)/times_all*100)
	column3[4]="%.3f"%((times_all-rowB5-rowB6)/times_all*100)
	column4[4]="%.3f"%((times_all-rowC5-rowC6)/times_all*100)

	
	global column21,column31,column41
	global rowA51,rowA61,rowB51,rowB61,rowC51,rowC61
	column21[0]="%.3f"%((float(f)-50))
	column31[0]="%.3f"%((float(f)-50))
	column41[0]="%.3f"%((float(f)-50))	
	if abs(float(column21[0]))>abs(float(column21[1])):
		column21[1]=column21[0]
	if abs(float(column31[0]))>abs(float(column31[1])):
		column31[1]=column31[0]
	if abs(float(column41[0]))>abs(float(column41[1])):
		column41[1]=column41[0]
	if float(column21[2])==0:
		column21[2]=column21[0]
	if float(column31[2])==0:
		column31[2]=column21[0]
	if float(column41[2])==0:
		column41[2]=column21[0]	
	if abs(float(column21[0]))<abs(float(column21[2])):
		column21[2]=column21[0]
	if abs(float(column31[0]))<abs(float(column31[2])):
		column31[2]=column31[0]
	if abs(float(column41[0]))<abs(float(column41[2])):
		column41[2]=column41[0]
	if abs(float(column21[0]))>47.5:
		column21[3]=column21[0]
	if abs(float(column31[0]))>47.5:
		column31[3]=column31[0]
	if abs(float(column41[0]))>47.5:
		column41[3]=column41[0]
	if float(column21[0])>0.2:
		rowA51=rowA51+1
	if float(column31[0])>0.2:
		rowB51=rowB51+1
	if float(column41[0])>0.2:
		rowC51=rowC51+1
	if float(column21[0])<-0.2:
		rowA61=rowA61+1
	if float(column31[0])<-0.2:
		rowB61=rowB61+1		
	if float(column41[0])<-0.2:
		rowC61=rowC61+1	
	column21[5]="%.3f"%(rowA51/times_all*100)
	column31[5]="%.3f"%(rowB51/times_all*100)
	column41[5]="%.3f"%(rowC51/times_all*100)
	column21[6]="%.3f"%(rowA61/times_all*100)
	column31[6]="%.3f"%(rowB61/times_all*100)
	column41[6]="%.3f"%(rowC61/times_all*100)
	column21[4]="%.3f"%((times_all-rowA51-rowA61)/times_all*100)
	column31[4]="%.3f"%((times_all-rowB51-rowB61)/times_all*100)
	column41[4]="%.3f"%((times_all-rowC51-rowC61)/times_all*100)
	timer=threading.Timer(1,voltage_deviation)
	timer.start()	
	

	
def arraydata():
	global voltageA_valid,voltageB_valid,voltageC_valid,B,f	
	text=bytes([1,3,0,0,0,52,68,29])
	try:
		com=serial.Serial('com6',9600,timeout=0.5)	
		com.write(text)
		x1=com.read(109)	
		x1=convert_int(x1)
	except:
		x1=[]
		for i in range(109):
			x1.append(0)
	if len(x1)!=109:
		x1=[]
		for i in range(109):
			x1.append(0)	
	voltageA_valid=float("%.3f"%((x1[4]*16**4+x1[5]*16**2+x1[6])*0.001))
	voltageB_valid=float("%.3f"%((x1[8]*16**4+x1[9]*16**2+x1[10])*0.001))
	voltageC_valid=float("%.3f"%((x1[12]*16**4+x1[13]*16**2+x1[14])
	*0.001))
	f=(x1[105]*16**2+x1[106])*0.001
	B=(x1[100]*16**4+x1[101]*16**2+x1[102])*0.001
	global currentA_valid,currentB_valid,currentC_valid	
	currentA_valid=(x1[28]*16**4+x1[29]*16**2+x1[30])*0.001
	currentB_valid=(x1[32]*16**4+x1[33]*16**2+x1[34])*0.001
	currentC_valid=(x1[36]*16**4+x1[37]*16**2+x1[38])*0.001
	global PA,PB,PC,QA,QB,QC
	PA="%.2f"%(voltageA_valid*currentA_valid*B)
	PB="%.2f"%(voltageB_valid*currentB_valid*B)
	PC="%.2f"%(voltageC_valid*currentC_valid*B)
	QA="%.2f"%(voltageA_valid*currentA_valid*(1-B*B)**0.5)
	QB="%.2f"%(voltageB_valid*currentB_valid*(1-B*B)**0.5)
	QC="%.2f"%(voltageC_valid*currentC_valid*(1-B*B)**0.5)
	global e,ei
	e=(x1[81]*16**2+x1[82])*0.01
	ei=(x1[79]*16**2+x1[80])*0.01
	global now_time
	now_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	times.insert(0,now_time)
	del times[36]
	global voltagesA_valid,voltagesB_valid,voltagesC_valid,es
	voltagesA_valid.insert(0,voltageA_valid)
	voltagesB_valid.insert(0,voltageB_valid)
	voltagesC_valid.insert(0,voltageC_valid)
	es.insert(0,e)
	eis.insert(0,ei)
	del voltagesA_valid[300]
	del voltagesB_valid[300]
	del voltagesC_valid[300]
	del es[36]	
	del eis[36]
	global currentsA_valid,currentsB_valid,currentsC_valid
	currentsA_valid.insert(0,currentA_valid)
	currentsB_valid.insert(0,currentB_valid)
	currentsC_valid.insert(0,currentC_valid)
	del currentsA_valid[300]
	del currentsB_valid[300]
	del currentsC_valid[300]
	global PAS,PBS,PCS,QAS,QBS,QCS
	PAS.insert(0,float(PA))
	PBS.insert(0,float(PB))
	PCS.insert(0,float(PC))
	QAS.insert(0,float(QA))
	QBS.insert(0,float(QB))
	QCS.insert(0,float(QC))
	del PAS[36],PBS[36],PCS[36],QAS[36],QBS[36],QCS[36]
	timer=threading.Timer(1,arraydata)
	timer.start()
	
	
times_all=0
sys.setrecursionlimit(10000000)
rowA6=rowB6=rowC6=0
rowA5=rowB5=rowC5=0
rowA61=rowB61=rowC61=0
rowA51=rowB51=rowC51=0
voltagesA=[]
voltagesB=[]
voltagesC=[]
currentsA=[]
currentsB=[]
currentsC=[]
es=[]
eis=[]
voltagesA_valid=[]
voltagesB_valid=[]
voltagesC_valid=[]
currentsA_valid=[]
currentsB_valid=[]
currentsC_valid=[]
PAS=[]
PBS=[]
PCS=[]
QAS=[]
QBS=[]
QCS=[]
times=[]
column2=[]
column3=[]
column4=[]
column21=[]
column31=[]
column41=[]
harmonicsA_U=[]
harmonicsB_U=[]
harmonicsC_U=[]
harmonicsA_I=[]
harmonicsB_I=[]
harmonicsC_I=[]
for i in range(300):
	voltagesA_valid.append(0)
	voltagesB_valid.append(0)
	voltagesC_valid.append(0)
	currentsA_valid.append(0)
	currentsB_valid.append(0)
	currentsC_valid.append(0)

for i in range(250):
	voltagesA.append(0)
	voltagesB.append(0)
	voltagesC.append(0)
	currentsA.append(0)
	currentsB.append(0)
	currentsC.append(0)	
for i in range(36):
	times.append(0)
	PAS.append(0)
	PBS.append(0)
	PCS.append(0)
	QAS.append(0)
	QBS.append(0)
	QCS.append(0)
	es.append(0)
	eis.append(0)
for i in range(7):
	column2.append(0)
	column3.append(0)
	column4.append(0)
	column21.append(0)
	column31.append(0)
	column41.append(0)
for i in range(16):	
	harmonicsA_I.append(0)
	harmonicsB_I.append(0)
	harmonicsC_I.append(0)
	harmonicsA_U.append(0)
	harmonicsB_U.append(0)
	harmonicsC_U.append(0)

timer1=threading.Timer(0,harmonic)
timer1.start()
timer2=threading.Timer(7,voltage_deviation)
timer2.start()	
timer3=threading.Timer(6,arraydata)
timer3.start()
timer4=threading.Timer(7,data,(0,))
timer4.start()







