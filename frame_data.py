#-*- coding: utf-8 -*-
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from tkinter import *
import data,time,threading,gc
from matplotlib.gridspec import GridSpec


def frame_20(self):
	global view20
	view20=Frame(self,width=1180,height=600,bg='white')
	view20.grid_propagate(0)
	view20.config(bd=2,relief=GROOVE)		
	fig1=plt.figure(dpi=128,figsize=(9,2))
	ax1=plt.axes(xlim=(0,5),ylim=(0,400))
	ax1.set_xticklabels(['0','1min','2min','3min','4min','5min'])
	ax1.set_ylabel('A相电压(V)',fontsize=16)
	ax1.grid(linestyle='--')
	line1,=ax1.plot([],[],lw=1)
	fig2=plt.figure(dpi=128,figsize=(9,2))
	ax2=plt.axes(xlim=(0,5),ylim=(0,10))
	ax2.set_xticklabels(['0','1min','2min','3min','4min','5min'])
	ax2.set_ylabel('A相电流(A)',fontsize=16)
	ax2.grid(linestyle='--')
	line2,=ax2.plot([],[],lw=1)


	def init1():
		line1.set_data([],[])
		return line1,
	def init2():
		line2.set_data([],[])
		return line2,

	def animate_U(i):
		x=np.linspace(0,5,300)	
		y=data.voltagesA_valid
		line1.set_data(x,y)
		return line1,
		
	def animate_I(i):
		x=np.linspace(0,5,300)
		y=data.currentsA_valid
		line2.set_data(x,y)
		return line2,
			
	def init1_label():
		label_U.set_text('')
		label_I.set_text('')
		return label_U,label_I
	def update1_label(i):
		label_U.set_text('电压有效值：'+str(data.voltageA_valid)+
		' V')
		label_I.set_text('电流有效值：'+str(data.currentA_valid)+
		' A')
		return label_U,label_I
			
	canvas1=FigureCanvasTkAgg(fig1,view20)
	canvas1.get_tk_widget().grid(row=0,column=0)
	animator01=animation.FuncAnimation(fig1,animate_U,init_func=init1,
	frames=1,interval=1000,blit=True)
	canvas2=FigureCanvasTkAgg(fig2,view20)
	canvas2.get_tk_widget().grid(row=1,column=0)
	animator02=animation.FuncAnimation(fig2,animate_I,init_func=init2,
	frames=1,interval=1000,blit=True)
	canvas2.draw()
	fig3=plt.figure(dpi=128,figsize=(9,0.5),facecolor='white')
	ax=fig3.add_subplot(111,frameon=False,xticks=[],yticks=[])
	canvas3=FigureCanvasTkAgg(fig3,view20)
	canvas3.get_tk_widget().grid(row=2,column=0)	
	label_U=plt.text(0.05,0.2,'',fontsize=20)
	label_I=plt.text(0.5,0.2,'',fontsize=20)
	animator03=animation.FuncAnimation(fig3,update1_label,init_func=init1_label,
	frames=1,interval=1000,blit=True)
	canvas3.draw()
	plt.close(fig1)
	plt.close(fig2)
	plt.close(fig3)



	
	
def frame_21(self):
	global view21
	view21=Frame(self,width=1180,height=600,bg='white')
	view21.grid_propagate(0)
	view21.config(bd=2,relief=GROOVE)	
	fig1=plt.figure(dpi=128,figsize=(9,2))
	ax1=plt.axes(xlim=(0,5),ylim=(0,400))
	ax1.set_xticklabels(['0','1min','2min','3min','4min','5min'])
	ax1.set_ylabel('B相电压(V)',fontsize=16)
	ax1.grid(linestyle='--')
	line1,=ax1.plot([],[],lw=1)


	fig2=plt.figure(dpi=128,figsize=(9,2))
	ax2=plt.axes(xlim=(0,5),ylim=(0,10))
	ax2.set_xticklabels(['0','1min','2min','3min','4min','5min'])
	ax2.set_ylabel('B相电流(A)',fontsize=16)
	ax2.grid(linestyle='--')
	line2,=ax2.plot([],[],lw=1)



	def init1():
		line1.set_data([],[])
		return line1,
	def init2():
		line2.set_data([],[])
		return line2,

	def animate_U(i):
		x=np.linspace(0,5,300)	
		y=data.voltagesB_valid
		line1.set_data(x,y)
		return line1,
		
	def animate_I(i):
		x=np.linspace(0,5,300)
		y=data.currentsB_valid
		line2.set_data(x,y)
		return line2,
	def init2_label():
		label_U.set_text('')
		label_I.set_text('')
		return label_U,label_I
		
	def update2_label(i):
		label_U.set_text('电压有效值：'+str(data.voltageB_valid)+
		' V')
		label_I.set_text('电流有效值：'+str(data.currentB_valid)+
		' A')
		return label_U,label_I
		
	canvas1=FigureCanvasTkAgg(fig1,view21)
	canvas1.get_tk_widget().grid(row=0,column=0)	
	animator11=animation.FuncAnimation(fig1,animate_U,init_func=init1,
	frames=1,interval=1000,blit=True)
	canvas1.draw()	
	canvas2=FigureCanvasTkAgg(fig2,view21)
	canvas2.get_tk_widget().grid(row=1,column=0)
	animator12=animation.FuncAnimation(fig2,animate_I,init_func=init2,
	frames=1,interval=1000,blit=True)
	canvas2.draw()
	fig3=plt.figure(dpi=128,figsize=(9,0.5),facecolor='white')
	ax=fig3.add_subplot(111,frameon=False,xticks=[],yticks=[])
	canvas3=FigureCanvasTkAgg(fig3,view21)
	canvas3.get_tk_widget().grid(row=2,column=0)	
	label_U=plt.text(0.05,0.2,'',fontsize=20)
	label_I=plt.text(0.5,0.2,'',fontsize=20)
	animator13=animation.FuncAnimation(fig3,update2_label,init_func=init2_label,
	frames=1,interval=1000,blit=True)
	canvas3.draw()


	
	
def frame_22(self):
	global view22
	view22=Frame(self,width=1180,height=600,bg='white')
	view22.grid_propagate(0)
	view22.config(bd=2,relief=GROOVE)	
	fig1=plt.figure(dpi=128,figsize=(9,2))
	ax1=plt.axes(xlim=(0,5),ylim=(0,400))
	ax1.set_xticklabels(['0','1min','2min','3min','4min','5min'])
	ax1.set_ylabel('C相电压(V)',fontsize=16)
	ax1.grid(linestyle='--')
	line1,=ax1.plot([],[],lw=1)


	fig2=plt.figure(dpi=128,figsize=(9,2))
	ax2=plt.axes(xlim=(0,5),ylim=(0,10))
	ax2.set_xticklabels(['0','1min','2min','3min','4min','5min'])
	ax2.set_ylabel('C相电流(A)',fontsize=16)
	ax2.grid(linestyle='--')
	line2,=ax2.plot([],[],lw=1)



	def init1():
		line1.set_data([],[])
		return line1,
	def init2():
		line2.set_data([],[])
		return line2,

	def animate_U(i):
		x=np.linspace(0,5,300)	
		y=data.voltagesC_valid
		line1.set_data(x,y)
		return line1,
		
	def animate_I(i):
		x=np.linspace(0,5,300)
		y=data.currentsC_valid
		line2.set_data(x,y)
		return line2,
	def init3_label():
		label_U.set_text('')
		label_I.set_text('')
		return label_U,label_I
	def update3_label(i):
		label_U.set_text('电压有效值：'+str(data.voltageC_valid)+
		' V')
		label_I.set_text('电流有效值：'+str(data.currentC_valid)+
		' A')
		return label_U,label_I
			
	canvas1=FigureCanvasTkAgg(fig1,view22)
	canvas1.get_tk_widget().grid(row=0,column=0)	
	animator21=animation.FuncAnimation(fig1,animate_U,init_func=init1,
	frames=1,interval=1000,blit=True)
	canvas1.draw()	
	canvas2=FigureCanvasTkAgg(fig2,view22)
	canvas2.get_tk_widget().grid(row=1,column=0)	
	animator22=animation.FuncAnimation(fig2,animate_I,init_func=init2,
	frames=1,interval=1000,blit=True)
	canvas2.draw()
	fig3=plt.figure(dpi=128,figsize=(9,0.5),facecolor='white')
	ax=fig3.add_subplot(111,frameon=False,xticks=[],yticks=[])
	canvas3=FigureCanvasTkAgg(fig3,view22)
	canvas3.get_tk_widget().grid(row=2,column=0)	
	label_U=plt.text(0.05,0.2,'',fontsize=20)
	label_I=plt.text(0.5,0.2,'',fontsize=20)
	animator23=animation.FuncAnimation(fig3,update3_label,init_func=init3_label,
	frames=1,interval=1000,blit=True)
	canvas3.draw()

	
	
def frame_23(self):
	global view23
	view23=Frame(self,width=1180,height=600,bg='white')
	view23.grid_propagate(0)
	view23.config(bd=2,relief=GROOVE)	
	fig1=plt.figure(dpi=128,figsize=(9,2))
	ax1=plt.axes(xlim=(0,5),ylim=(-600,600))
	ax1.set_xticklabels(['0','0.02s','0.04s','0.06s','0.08s','0.10s'])
	ax1.set_ylabel('A相电压(V)',fontsize=16)
	ax1.grid(linestyle='--')
	line1,=ax1.plot([],[],lw=1)
	voltages=[]

	fig2=plt.figure(dpi=128,figsize=(9,2))
	ax2=plt.axes(xlim=(0,5),ylim=(-20,20))
	ax2.set_xticklabels(['0','0.02s','0.04s','0.06s','0.08s','0.10s'])
	ax2.set_ylabel('A相电流(A)',fontsize=16)
	ax2.grid(linestyle='--')
	line2,=ax2.plot([],[],lw=1)
	currents=[]	



	def init1():
		line1.set_data([],[])
		return line1,
	def init2():
		line2.set_data([],[])
		return line2,

	def animate_U(i):
		x=np.linspace(0,5,250)			
		y=data.voltagesA
		line1.set_data(x,y)
		return line1,
		
	def animate_I(i):
		x=np.linspace(0,5,250)
		y=data.currentsA
		line2.set_data(x,y)
		return line2,
	def init1_label():
		label_U.set_text('')
		label_I.set_text('')
		return label_U,label_I
	def update1_label(i):
		label_U.set_text('电压峰峰值：'+str(data.voltageA_pp)+
		' V')
		label_I.set_text('电流峰峰值：'+str(data.currentA_pp)+
		' A')
		return label_U,label_I
		
	matplotlib.rcParams['axes.unicode_minus']=False		
	canvas1=FigureCanvasTkAgg(fig1,view23)
	canvas1.get_tk_widget().grid(row=0,column=0)	
	animator31=animation.FuncAnimation(fig1,animate_U,init_func=init1,
	frames=1,interval=1000,blit=True)
	canvas1.draw()	
	canvas2=FigureCanvasTkAgg(fig2,view23)
	canvas2.get_tk_widget().grid(row=1,column=0)	
	animator32=animation.FuncAnimation(fig2,animate_I,init_func=init2,
	frames=1,interval=1000,blit=True)
	canvas2.draw()
	fig3=plt.figure(dpi=128,figsize=(9,0.5),facecolor='white')
	ax=fig3.add_subplot(111,frameon=False,xticks=[],yticks=[])
	canvas3=FigureCanvasTkAgg(fig3,view23)
	canvas3.get_tk_widget().grid(row=2,column=0)	
	label_U=plt.text(0.05,0.2,'',fontsize=20)
	label_I=plt.text(0.5,0.2,'',fontsize=20)
	animator33=animation.FuncAnimation(fig3,update1_label,init_func=init1_label,
	frames=1,interval=1000,blit=True)
	canvas3.draw()

	


def frame_24(self):
	global view24
	view24=Frame(self,width=1180,height=600,bg='white')
	view24.grid_propagate(0)
	view24.config(bd=2,relief=GROOVE)	
	fig1=plt.figure(dpi=128,figsize=(9,2))
	ax1=plt.axes(xlim=(0,5),ylim=(-600,600))
	ax1.set_xticklabels(['0','0.02s','0.04s','0.06s','0.08s','0.10s'])
	ax1.set_ylabel('B相电压(V)',fontsize=16)
	ax1.grid(linestyle='--')
	line1,=ax1.plot([],[],lw=1)
	voltages=[]

	fig2=plt.figure(dpi=128,figsize=(9,2))
	ax2=plt.axes(xlim=(0,5),ylim=(-20,20))
	ax2.set_xticklabels(['0','0.02s','0.04s','0.06s','0.08s','0.10s'])
	ax2.set_ylabel('B相电流(A)',fontsize=16)
	ax2.grid(linestyle='--')
	line2,=ax2.plot([],[],lw=1)
	currents=[]	



	def init1():
		line1.set_data([],[])
		return line1,
	def init2():
		line2.set_data([],[])
		return line2,

	def animate_U(i):
		x=np.linspace(0,5,250)			
		y=data.voltagesB
		line1.set_data(x,y)
		return line1,
		
	def animate_I(i):
		x=np.linspace(0,5,250)
		y=data.currentsB
		line2.set_data(x,y)
		return line2,

	def init2_label():
		label_U.set_text('')
		label_I.set_text('')
		return label_U,label_I
	def update2_label(i):
		label_U.set_text('电压峰峰值：'+str(data.voltageB_pp)+
		' V')
		label_I.set_text('电流峰峰值：'+str(data.currentB_pp)+
		' A')
		return label_U,label_I

	
	matplotlib.rcParams['axes.unicode_minus']=False		
	canvas1=FigureCanvasTkAgg(fig1,view24)
	canvas1.get_tk_widget().grid(row=0,column=0)	
	animator41=animation.FuncAnimation(fig1,animate_U,init_func=init1,
	frames=1,interval=1000,blit=True)
	canvas1.draw()	
	canvas2=FigureCanvasTkAgg(fig2,view24)
	canvas2.get_tk_widget().grid(row=1,column=0)	
	animator42=animation.FuncAnimation(fig2,animate_I,init_func=init2,
	frames=1,interval=1000,blit=True)
	canvas2.draw()
	fig3=plt.figure(dpi=128,figsize=(9,0.5),facecolor='white')
	ax=fig3.add_subplot(111,frameon=False,xticks=[],yticks=[])
	canvas3=FigureCanvasTkAgg(fig3,view24)
	canvas3.get_tk_widget().grid(row=2,column=0)	
	label_U=plt.text(0.05,0.2,'',fontsize=20)
	label_I=plt.text(0.5,0.2,'',fontsize=20)
	animator43=animation.FuncAnimation(fig3,update2_label,init_func=init2_label,
	frames=1,interval=1000,blit=True)
	canvas3.draw()

		


def frame_25(self):
	global view25
	view25=Frame(self,width=1180,height=600,bg='white')
	view25.grid_propagate(0)
	view25.config(bd=2,relief=GROOVE)	
	fig1=plt.figure(dpi=128,figsize=(9,2))
	ax1=plt.axes(xlim=(0,5),ylim=(-600,600))
	ax1.set_xticklabels(['0','0.02s','0.04s','0.06s','0.08s','0.10s'])
	ax1.set_ylabel('C相电压(V)',fontsize=16)
	ax1.grid(linestyle='--')
	line1,=ax1.plot([],[],lw=1)
	voltages=[]

	fig2=plt.figure(dpi=128,figsize=(9,2))
	ax2=plt.axes(xlim=(0,5),ylim=(-20,20))
	ax2.set_xticklabels(['0','0.02s','0.04s','0.06s','0.08s','0.10s'])
	ax2.set_ylabel('C相电流(A)',fontsize=16)
	ax2.grid(linestyle='--')
	line2,=ax2.plot([],[],lw=1)
	currents=[]	



	def init1():
		line1.set_data([],[])
		return line1,
	def init2():
		line2.set_data([],[])
		return line2,

	def animate_U(i):
		x=np.linspace(0,5,250)			
		y=data.voltagesC
		line1.set_data(x,y)
		return line1,
		
	def animate_I(i):
		x=np.linspace(0,5,250)
		y=data.currentsC
		line2.set_data(x,y)
		return line2,
	def init3_label():
		label_U.set_text('')
		label_I.set_text('')
		return label_U,label_I
	def update3_label(i):
		label_U.set_text('电压峰峰值：'+str(data.voltageC_pp)+
		' V')
		label_I.set_text('电流峰峰值：'+str(data.currentC_pp)+
		' A')
		return label_U,label_I
		

	matplotlib.rcParams['axes.unicode_minus']=False		
	canvas1=FigureCanvasTkAgg(fig1,view25)
	canvas1.get_tk_widget().grid(row=0,column=0)	
	animator51=animation.FuncAnimation(fig1,animate_U,init_func=init1,
	frames=1,interval=1000,blit=True)
	canvas1.draw()	
	canvas2=FigureCanvasTkAgg(fig2,view25)
	canvas2.get_tk_widget().grid(row=1,column=0)	
	animator52=animation.FuncAnimation(fig2,animate_I,init_func=init2,
	frames=1,interval=1000,blit=True)
	canvas2.draw()
	fig3=plt.figure(dpi=128,figsize=(9,0.5),facecolor='white')
	ax=fig3.add_subplot(111,frameon=False,xticks=[],yticks=[])
	canvas3=FigureCanvasTkAgg(fig3,view25)
	canvas3.get_tk_widget().grid(row=2,column=0)	
	label_U=plt.text(0.05,0.2,'',fontsize=20)
	label_I=plt.text(0.5,0.2,'',fontsize=20)

	animator53=animation.FuncAnimation(fig3,update3_label,init_func=init3_label,
	frames=1,interval=1000,blit=True)
	canvas3.draw()

	


def frame_26(self):
	global view26
	view26=Frame(self,width=1180,height=600,bg='white')
	view26.grid_propagate(0)
	view26.config(bd=2,relief=GROOVE)		
	tree=ttk.Treeview(view26,show='headings',height=29)
	tree['columns']=('a','b','c','d','e','f','g','h','i')
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
	def update_tree():
		for _ in map(tree.delete,tree.get_children("")):
			pass
		for i in range(28):
			tree.insert('',i,values=(data.times[i],
			data.voltagesA_valid[i],data.currentsA_valid[i],
			data.voltagesB_valid[i],data.currentsB_valid[i],
			data.voltagesC_valid[i],data.currentsC_valid[i],
			data.es[i],data.eis[i]))	
		timer2=threading.Timer(10,update_tree)
		timer2.start()
	tree.grid(row=0,column=0,sticky=NS)
	update_tree()

	
def frame_27(self):
	global view27
	view27=Frame(self,width=1180,height=600,bg='white')
	view27.grid_propagate(0)
	view27.config(bd=2,relief=GROOVE)				
	tree=ttk.Treeview(view27,show='headings',height=29)
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
	def update_tree():
		for _ in map(tree.delete,tree.get_children("")):
			pass
		for i in range(28):
			P=data.PAS[i]+data.PBS[i]+data.PCS[i]
			Q=data.QAS[i]+data.QBS[i]+data.QCS[i]
			try:
				PF=data.B
			except:
				PF=0
			tree.insert('',i,values=(data.times[i],data.PAS[i],
			data.QAS[i],data.PBS[i],data.QBS[i],data.PCS[i],
			data.QCS[i],"%.2f"%P,"%.2f"%Q,PF))
	
		timer2=threading.Timer(10,update_tree)
		timer2.start()
	tree.grid(row=0,column=0,sticky=NS)
	update_tree()

def frame_28(self):		#电压和频率偏差
	global view28
	view28=Frame(self,width=1180,height=600,bg='white')
	view28.grid_propagate(0)
	view28.config(bd=2,relief=GROOVE)	
	tree1=ttk.Treeview(view28,show='headings',height=7)
	tree1['columns']=('a','b','c','d')
	tree1.column("a",width=192,anchor="w")
	tree1.column("b",width=140,anchor="center")  
	tree1.column("c",width=140,anchor="center")
	tree1.column("d",width=140,anchor="center")
	tree1.heading("a",text='line')
	tree1.heading("b",text='A相')  
	tree1.heading("c",text='B相')
	tree1.heading("d",text='C相')
	column1=['电压偏差(%)','最大电压偏差(%)','最小电压偏差(%)',
	'电压偏差95%概率大值(%)','电压偏差合格率(%)','电压正偏差越限率(%)',
	'电压负偏差越限率(%)']
	def update_tree1():
		for _ in map(tree1.delete,tree1.get_children("")):
			pass
		for i in range(7):
			tree1.insert('',i,values=(column1[i],data.column2[i],
			data.column3[i],data.column4[i]))	
		timer1=threading.Timer(5,update_tree1)
		timer1.start()
	label1=Label(view28,text='电压偏差',font=("Arial, 12"),bg='white')
	label1.grid(row=0,column=0,pady=(10,0))
	tree1.grid(row=1,column=0,padx=250,pady=10)

	tree2=ttk.Treeview(view28,show='headings',height=7)
	tree2['columns']=('a','b','c','d')
	tree2.column("a",width=192,anchor="w")
	tree2.column("b",width=140,anchor="center")  
	tree2.column("c",width=140,anchor="center")
	tree2.column("d",width=140,anchor="center")
	tree2.heading("a",text='line')
	tree2.heading("b",text='A相')  
	tree2.heading("c",text='B相')
	tree2.heading("d",text='C相')
	column11=['频率偏差(Hz)','最大频率偏差(Hz)','最小频率偏差(Hz)',
	'频率偏差95%概率大值(Hz)','频率偏差合格率(%)','频率正偏差越限率(%)',
	'频率负偏差越限率(%)']
	def update_tree2():
		for _ in map(tree2.delete,tree2.get_children("")):
			pass
		for i in range(7):
			tree2.insert('',i,values=(column11[i],data.column21[i],
			data.column31[i],data.column41[i]))	
		timer2=threading.Timer(5,update_tree2)
		timer2.start()
	label2=Label(view28,text='频率偏差',font=("Arial, 12"),bg='white')
	label2.grid(row=2,column=0,pady=(10,0))
	tree2.grid(row=3,column=0,padx=250,pady=10)
	update_tree2()
	update_tree1()
	
def frame_29(self):
	def on_press(event):
		global x_now
		x_now=event.xdata
	global view29
	view29=Frame(self,width=1180,height=600,bg='white')
	view29.grid_propagate(0)
	view29.config(bd=2,relief=GROOVE)
	global fig	
	fig=plt.figure(dpi=100,figsize=(8,4.5))
	fig.add_subplot(211)
	plt.ylabel('电压含量(%)')
	plt.title('谐波分析')
	x1=range(16)	
	x2=[i+0.3 for i in x1]
	x3=[i+0.6 for i in x1]
	y1=data.harmonicsA_U
	y2=data.harmonicsB_U
	y3=data.harmonicsC_U
	plt.bar(x1,y1,facecolor='red',width=0.3,label='A相')
	plt.bar(x2,y2,facecolor='green',width=0.3,label='B相')
	plt.bar(x3,y3,facecolor='blue',width=0.3,label='C相')
	xlabel=[3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,'THD']
	plt.xticks(x2,xlabel)
	global ax1,ax2
	ax1=plt.gca()	
	plt.legend(loc='upper right',bbox_to_anchor=(1.13,1.0))	
	fig.add_subplot(212)
	plt.ylabel('电流含量(%)')
	x4=range(16)
	x5=[i+0.3 for i in x1]
	x6=[i+0.6 for i in x1]
	y4=data.harmonicsA_I
	y5=data.harmonicsB_I
	y6=data.harmonicsC_I
	
	plt.bar(x4,y4,facecolor='red',width=0.3,label='A相')
	plt.bar(x5,y5,facecolor='green',width=0.3,label='B相')
	plt.bar(x6,y6,facecolor='blue',width=0.3,label='C相')
	plt.xticks(x2,xlabel)
	ax2=plt.gca()
	ax2.set_xticklabels(xlabel)
	canvas1=FigureCanvasTkAgg(fig,view29)
	canvas1.get_tk_widget().grid(row=0,column=0,padx=(150,0),sticky=N)	
	canvas1.draw()	

			
	fig.canvas.mpl_connect('motion_notify_event', on_press)
	tree=ttk.Treeview(view29,show='headings',height=5)
	tree['columns']=('a','b','c','d','e','f','g')
	vbar=ttk.Scrollbar(view29,command=tree.yview)
	tree.config(yscrollcommand=vbar.set)
	tree.column("a",width=50,anchor="center")
	tree.column("b",width=100,anchor="center")  
	tree.column("c",width=100,anchor="center")
	tree.column("d",width=100,anchor="center")
	tree.column("e",width=100,anchor="center")  
	tree.column("f",width=100,anchor="center")			
	tree.column("g",width=100,anchor="center")  
	tree.heading("a",text='谐波次数')
	tree.heading("b",text='A相电压含量(%)')  
	tree.heading("c",text='B相电压含量(%)')
	tree.heading("d",text='C相电压含量(%)')
	tree.heading("e",text='A相电流含量(%)')  
	tree.heading("f",text='B相电流含量(%)')			
	tree.heading("g",text='C相电流含量(%)')
	for i in range(16):
		tree.insert('',i,values=(xlabel[i],"%.2f"%data.harmonicsA_U[i],
		"%.2f"%data.harmonicsB_U[i],"%.2f"%data.harmonicsC_U[i],
		"%.2f"%data.harmonicsA_I[i],"%.2f"%data.harmonicsB_I[i],
		"%.2f"%data.harmonicsC_I[i]))
	tree.grid(row=1,column=0,padx=(170,0),pady=(18,0),sticky=NSEW)
	vbar.grid(row=1,column=0,padx=(950,0),pady=(18,0),sticky=NS)
	def on_press(event):
		x_now=event.xdata
		try:
			for i in range(16):
				if i<=x_now<=i+0.6:
					if i<15:
						a=hex(i+1)
						a=str.upper(a[2])
						tree.see('I00'+a)
						tree.selection_set('I00'+a)
					else:
						a=hex(i+1)
						a=str.upper(a[2]+a[3])
						tree.see('I0'+a)
						tree.selection_set('I0'+a)
		except:
			pass
	fig.canvas.mpl_connect('motion_notify_event', on_press)
	
def frame_210(self):
	global view210
	view210=Frame(self,width=1180,height=600,bg='white')
	view210.grid_propagate(0)
	view210.config(bd=2,relief=GROOVE)	
	fig1=plt.figure(dpi=128,figsize=(9,2))
	ax1=plt.axes(xlim=(0,5),ylim=(-600,600))
	ax1.set_xticklabels(['0','0.02s','0.04s','0.06s','0.08s','0.10s'])
	ax1.set_ylabel('A相电压(V)',fontsize=16)
	ax1.grid(linestyle='--')
	line1,=ax1.plot([],[],'r',lw=1,label='A相')
	line2,=ax1.plot([],[],'b',lw=1,label='B相')
	line3,=ax1.plot([],[],'g',lw=1,label='C相')
	plt.legend(loc='upper right',bbox_to_anchor=(1.13,1.0))
	voltages=[]

	fig2=plt.figure(dpi=128,figsize=(9,2))
	ax2=plt.axes(xlim=(0,5),ylim=(-20,20))
	ax2.set_xticklabels(['0','0.02s','0.04s','0.06s','0.08s','0.10s'])
	ax2.set_ylabel('A相电流(A)',fontsize=16)
	ax2.grid(linestyle='--')
	line4,=ax2.plot([],[],'r',lw=1)
	line5,=ax2.plot([],[],'b',lw=1)
	line6,=ax2.plot([],[],'g',lw=1)
	currents=[]	


	def init1():
		line1.set_data([],[])
		line2.set_data([],[])
		line3.set_data([],[])
		return line1,line2,line3
	def init2():
		line4.set_data([],[])
		line5.set_data([],[])
		line6.set_data([],[])
		return line4,line5,line6

	def animate_U(i):
		x=np.linspace(0,5,250)			
		y=data.voltagesA
		line1.set_data(x,y)			
		y=data.voltagesB
		line2.set_data(x,y)
		y=data.voltagesC
		line3.set_data(x,y)
		return line1,line2,line3
		
	def animate_I(i):
		x=np.linspace(0,5,250)
		y=data.currentsA
		line4.set_data(x,y)
		y=data.currentsB
		line5.set_data(x,y)
		y=data.currentsC
		line6.set_data(x,y)
		return line4,line5,line6
			
	def init1_label():
		label_U.set_text('')
		label_I.set_text('')
		return label_U,label_I
	def update1_label(i):
		label_U.set_text('电压有效值：'+str(data.voltageA_valid)+
		' V')
		label_I.set_text('电流有效值：'+str(data.currentA_valid)+
		' A')
		return label_U,label_I
			
	canvas1=FigureCanvasTkAgg(fig1,view210)
	canvas1.get_tk_widget().grid(row=0,column=0)
	animator01=animation.FuncAnimation(fig1,animate_U,init_func=init1,
	frames=1,interval=1000,blit=True)
	canvas2=FigureCanvasTkAgg(fig2,view210)
	canvas2.get_tk_widget().grid(row=1,column=0)
	animator02=animation.FuncAnimation(fig2,animate_I,init_func=init2,
	frames=1,interval=1000,blit=True)
	canvas2.draw()
	plt.close(fig1)
	plt.close(fig2)	
	tree=ttk.Treeview(view210,show='headings',height=2)
	tree['columns']=('a','b','c','d','e')
	tree.column("a",width=192,anchor="w")
	tree.column("b",width=140,anchor="center")  
	tree.column("c",width=140,anchor="center")
	tree.column("d",width=140,anchor="center")
	tree.column("e",width=140,anchor="center")
	tree.heading("a",text='')
	tree.heading("b",text='A相')  
	tree.heading("c",text='B相')
	tree.heading("d",text='C相')
	tree.heading("e",text='三相不平衡')
	def update_tree():
		for _ in map(tree.delete,tree.get_children("")):
			pass
		tree.insert('',0,values=('电压',data.voltageA_valid,
		data.voltageB_valid,data.voltageC_valid,data.e))
		tree.insert('',1,values=('电流',data.currentA_valid,
		data.currentB_valid,data.currentC_valid,data.ei))
		timer=threading.Timer(1,update_tree)
		timer.start()	
	tree.grid(row=2,column=0)
	update_tree()	


	
	
