import data,threading,time,datetime,frame,menu,os
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg

def save_start():
	if menu.flag_save==0:
		now_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		frame.view3.insert(END,now_time+'  开始记录数据')
		frame.view3.see(END)
		time_name=datetime.datetime.now().strftime('%Y-%m-%d %H.%M')
		filename='.//users//'+str(frame.admin)+'//'+str(time_name)+'.txt'
		save_data=[]
		def update():
			with open(filename,'w') as file_object:	
				new_data={}
				new_data['time']=data.now_time
				new_data['voltageA']=data.voltageA_valid
				new_data['voltageB']=data.voltageB_valid
				new_data['voltageC']=data.voltageC_valid
				new_data['currentA']=data.currentA_valid
				new_data['currentB']=data.currentB_valid
				new_data['currentC']=data.currentC_valid
				new_data['e']=data.e
				new_data['ei']=data.ei
				new_data['PA']=data.PA
				new_data['PB']=data.PB
				new_data['PC']=data.PC
				new_data['QA']=data.QA
				new_data['QB']=data.QB
				new_data['QC']=data.QC
				save_data.append(new_data)
				file_object.write(str(save_data))
				file_object.close()
				global timer
				timer=threading.Timer(1,update)
				timer.start()				
		update()
		menu.flag_save=1	
	else:
		showerror('错误','系统已处于记录中')

	

def save_stop():
	if menu.flag_save==0:
		showerror('错误','系统尚未开始记录')
	else:
		timer.cancel()
		menu.flag_save=0
		now_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		frame.view3.insert(END,now_time+'  停止记录数据')
		frame.view3.see(END)

def save_window():
	def close():
		root.destroy()
	def figure():
		text1=chose1.get()
		text2=chose2.get()
		root.destroy()
		filename='.//users//'+str(frame.admin)+'//'+str(text1)
		voltagesA=[]
		voltagesB=[]
		voltagesC=[]
		currentsA=[]
		currentsB=[]
		currentsC=[]
		es=[]
		eis=[]
		PAS=[]
		PBS=[]
		PCS=[]
		QAS=[]
		QBS=[]
		QCS=[]
		times=[]
		with open(filename) as file:
			file_data=file.read()
			file_data=eval(file_data)
			for i in file_data:
				times.append(i['time'])
				voltagesA.append(i['voltageA'])
				voltagesB.append(i['voltageB'])
				voltagesC.append(i['voltageC'])
				currentsA.append(i['currentA'])
				currentsB.append(i['currentB'])
				currentsC.append(i['currentC'])
				es.append(i['e'])
				eis.append(i['ei'])
				PAS.append(i['PA'])
				PBS.append(i['PB'])
				PCS.append(i['PC'])
				QAS.append(i['QA'])
				QBS.append(i['QB'])
				QCS.append(i['QC'])
		if text2=='A相电流电压波形图':
			win=Tk()
			win.resizable(0,0)
			win.title('A相电流电压波形图')				
			fig=plt.figure(num='A相电流电压波形图',dpi=128,figsize=(9,5))
			plt.plot(times,voltagesA,label='电压')
			plt.plot(times,currentsA,label='电流')
			plt.legend(loc='upper right',bbox_to_anchor=(1.13,1.0))
			fig.autofmt_xdate()
			canvas=FigureCanvasTkAgg(fig,win)
			canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
			canvas.draw()
			toolbar=NavigationToolbar2TkAgg(canvas,win)
			toolbar.update()
			canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
			win.mainloop()	
		if text2=='B相电流电压波形图':
			win=Tk()
			win.resizable(0,0)
			win.title('B相电流电压波形图')
			fig=plt.figure(num='B相电流电压波形图',dpi=128,figsize=(9,5))
			plt.plot(times,voltagesB,label='电压')
			plt.plot(times,currentsB,label='电流')
			plt.legend(loc='upper right',bbox_to_anchor=(1.13,1.0))
			fig.autofmt_xdate()		
			canvas=FigureCanvasTkAgg(fig,win)
			canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
			canvas.draw()
			toolbar=NavigationToolbar2TkAgg(canvas,win)
			toolbar.update()
			canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
			win.mainloop()	
		if text2=='C相电流电压波形图':
			win=Tk()
			win.resizable(0,0)
			win.title('C相电流电压波形图')
			fig=plt.figure(num='C相电流电压波形图',dpi=128,figsize=(9,5))
			plt.plot(times,voltagesC,label='电压')
			plt.plot(times,currentsC,label='电流')
			plt.legend(loc='upper right',bbox_to_anchor=(1.13,1.0))
			fig.autofmt_xdate()		
			canvas=FigureCanvasTkAgg(fig,win)
			canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
			canvas.draw()
			toolbar=NavigationToolbar2TkAgg(canvas,win)
			toolbar.update()
			canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
			win.mainloop()	
		if text2=='电流电压数据表':
			win=Tk()
			win.resizable(0,0)
			win.title("电流电压数据表")
			tree=ttk.Treeview(win,show='headings',height=30)
			tree['columns']=('a','b','c','d','e','f','g','h','i')
			vbar=ttk.Scrollbar(win,command=tree.yview)
			tree.config(yscrollcommand=vbar.set)
			tree.column("a",width=172,anchor="center")
			tree.column("b",width=125,anchor="center")  
			tree.column("c",width=125,anchor="center")
			tree.column("d",width=125,anchor="center")
			tree.column("e",width=125,anchor="center")  
			tree.column("f",width=125,anchor="center")			
			tree.column("g",width=125,anchor="center")
			tree.column("h",width=125,anchor="center")
			tree.column("i",width=125,anchor="center")    
			tree.heading("a",text='时间')
			tree.heading("b",text='A相电压(V)')  
			tree.heading("c",text='A相电流(A)')
			tree.heading("d",text='B相电压(V)')
			tree.heading("e",text='B相电流(A)')  
			tree.heading("f",text='C相电压(V)')			
			tree.heading("g",text='C相电流(A)')
			tree.heading("h",text='三相电压不平衡度') 
			tree.heading("i",text='三相电流不平衡度') 
			for i in range(len(times)):
				tree.insert('',i,values=(times[i],voltagesA[i],
				currentsA[i],voltagesB[i],currentsB[i],voltagesC[i],
				currentsC[i],es[i],eis[i]))
			tree.grid(row=0,column=0,sticky=NSEW)
			vbar.grid(row=0,column=1,sticky=NS)
			win.mainloop()
		if text2=='三相功率数据表':
			win=Tk()
			win.resizable(0,0)
			win.title("三相功率数据表")
			tree=ttk.Treeview(win,show='headings',height=30)
			vbar=ttk.Scrollbar(win,command=tree.yview)
			tree.config(yscrollcommand=vbar.set)
			tree['columns']=('a','b','c','d','e','f','g','h','i','j')
			tree.column("a",width=152,anchor="center")
			tree.column("b",width=115,anchor="center")  
			tree.column("c",width=115,anchor="center")
			tree.column("d",width=115,anchor="center")
			tree.column("e",width=115,anchor="center")  
			tree.column("f",width=115,anchor="center")			
			tree.column("g",width=115,anchor="center")
			tree.column("h",width=115,anchor="center")
			tree.column("i",width=115,anchor="center")
			tree.column("j",width=115,anchor="center")    
			tree.heading("a",text='时间')
			tree.heading("b",text='A相有功功率(W)')  
			tree.heading("c",text='A相无功功率(W)')
			tree.heading("d",text='B相有功功率(W)')
			tree.heading("e",text='B相无功功率(W)')  
			tree.heading("f",text='C相有功功率(W)')			
			tree.heading("g",text='C相无功功率(W)')
			tree.heading("h",text='总有功功率(W)') 
			tree.heading("i",text='总无功功率(W)')
			tree.heading("j",text='功率因数') 
			for i in range(len(times)):
				P=float(PAS[i])+float(PBS[i])+float(PCS[i])				
				Q=float(QAS[i])+float(QBS[i])+float(QCS[i])
				try:
					PF=P/((P**2+Q**2)**0.5)
				except :
					PF=0
				tree.insert('',i,values=(times[i],PAS[i],QAS[i],PBS[i],
				QBS[i],PCS[i],QCS[i],"%.2f"%P,"%.2f"%Q,"%.4f"%PF))
			tree.grid(row=0,column=0,sticky=NSEW)
			vbar.grid(row=0,column=1,sticky=NS)
			win.mainloop()
		
	for root,dirs,files in os.walk('.//users//1415211009//'):
		files_name=files
	root=Tk()
	root.resizable(0,0)
	root.title('数据查询')
	Label(root,text="历史数据选择").grid(row=0,column=0,padx=10,sticky=W)
	var1=StringVar()
	var2=StringVar()
	chose1=ttk.Combobox(root,width=20,value=files_name,textvariable=var1)
	chose1.grid(row=1,column=0,padx=10,sticky=W)
	choselist=['A相电流电压波形图','B相电流电压波形图','C相电流电压波形图',
	'电流电压数据表','三相功率数据表']
	Label(root,text="数据类型选择").grid(row=2,column=0,padx=10,sticky=W)
	chose2=ttk.Combobox(root,width=20,value=choselist,textvariable=var2)
	chose2.grid(row=3,column=0,padx=10,sticky=W)
	btn1=ttk.Button(root,width=8,text='确定',command=figure)
	btn1.grid(row=4,column=0,padx=(10,0),pady=10,sticky=W)
	btn2=ttk.Button(root,width=8,text='取消',command=close)
	btn2.grid(row=4,column=0,padx=(0,10),pady=10,sticky=E)
	root.mainloop()

		
