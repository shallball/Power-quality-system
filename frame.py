# coding=gbk
from tkinter import *
from PIL import Image,ImageTk
import frame_data 
from matplotlib.figure import Figure
import threading,datetime
import menu,time,os
from matplotlib.widgets import MultiCursor
def switch(a):
	view1.var.set(a)
	frame_data.view20.grid_forget()
	frame_data.view21.grid_forget()
	frame_data.view22.grid_forget()
	frame_data.view23.grid_forget()
	frame_data.view24.grid_forget()
	frame_data.view25.grid_forget()
	frame_data.view26.grid_forget()
	frame_data.view27.grid_forget()
	frame_data.view28.grid_forget()
	frame_data.view29.grid_forget()
	frame_data.view210.grid_forget()
	frame_data.view20.grid_propagate(0)
	frame_data.view21.grid_propagate(0)
	frame_data.view22.grid_propagate(0)
	frame_data.view23.grid_propagate(0)
	frame_data.view24.grid_propagate(0)
	frame_data.view25.grid_propagate(0)
	frame_data.view26.grid_propagate(0)
	frame_data.view27.grid_propagate(0)
	frame_data.view28.grid_propagate(0)
	frame_data.view29.grid_propagate(0)
	frame_data.view210.grid_propagate(0)
	if a==0:
		frame_data.view20.grid(row=0,column=1,padx=(0,0),pady=(7,0))
	if a==1:	
		frame_data.view21.grid(row=0,column=1,padx=(0,0),pady=(7,0))
	if a==2:
		frame_data.view22.grid(row=0,column=1,padx=(0,0),pady=(7,0))
	if a==3:
		frame_data.view23.grid(row=0,column=1,padx=(0,0),pady=(7,0))
	if a==4:		
		frame_data.view24.grid(row=0,column=1,padx=(0,0),pady=(7,0))
	if a==5:
		frame_data.view25.grid(row=0,column=1,padx=(0,0),pady=(7,0))
	if a==6:
		frame_data.view26.grid(row=0,column=1,padx=(0,0),pady=(7,0))
	if a==7:
		frame_data.view27.grid(row=0,column=1,padx=(0,0),pady=(7,0))
	if a==8:
		frame_data.view28.grid(row=0,column=1,padx=(0,0),pady=(7,0))
	if a==9:
		frame_data.view29.grid(row=0,column=1,padx=(0,0),pady=(7,0))
	if a==10:
		frame_data.view210.grid(row=0,column=1,padx=(0,0),pady=(7,0))
		
def frame1(self):
	global view1
	view1=Frame(self,width=150,height=582,bg='white')
	view1.grid_propagate(0)
	view1.grid(row=0,column=0,padx=(5,5),pady=(23,0))
	view1.config(bd=2,relief=GROOVE)
	label=Label(self,text='数据显示')
	label.grid(row=0,column=0,padx=(5,0),sticky=NW)
	view1.config(bd=2,relief=RIDGE)
	names=['A相有效值波形图','B相有效值波形图','C相有效值波形图',
	'A相瞬时值波形图','B相瞬时值波形图','C相瞬时值波形图','电流电压数据表  ',
	'三相功率数据表  ','电压和频率偏差','谐波分析','三相不平衡度']
	view1.var=StringVar()
	view1.var.set(3)
	Label(view1,text='基本电量显示',bg='white').grid(sticky=W)
	Radiobutton(view1,text=names[3],bg='white',command=lambda:switch(3),
	variable=view1.var,value=3).grid(sticky=N)
	Radiobutton(view1,text=names[4],bg='white',command=lambda:switch(4),
	variable=view1.var,value=4).grid(sticky=N)
	Radiobutton(view1,text=names[5],bg='white',command=lambda:switch(5),
	variable=view1.var,value=5).grid(sticky=N)
	Radiobutton(view1,text=names[0],bg='white',command=lambda:switch(0),
	variable=view1.var,value=0).grid(sticky=N)
	Radiobutton(view1,text=names[1],bg='white',command=lambda:switch(1),
	variable=view1.var,value=1).grid(sticky=N)
	Radiobutton(view1,text=names[2],bg='white',command=lambda:switch(2),
	variable=view1.var,value=2).grid(sticky=N)
	Radiobutton(view1,text=names[6],bg='white',command=lambda:switch(6),
	variable=view1.var,value=6).grid(sticky=N)
	Radiobutton(view1,text=names[7],bg='white',command=lambda:switch(7),
	variable=view1.var,value=7).grid(sticky=N)
	Label(view1,text='电能质量显示',bg='white').grid(sticky=W)
	Radiobutton(view1,text=names[8],bg='white',command=lambda:switch(8),
	variable=view1.var,value=8).grid(sticky=NW)
	Radiobutton(view1,text=names[9],bg='white',command=lambda:switch(9),
	variable=view1.var,value=9).grid(sticky=NW)
	Radiobutton(view1,text=names[10],bg='white',command=lambda:switch(10),
	variable=view1.var,value=10).grid(sticky=NW)
	

			
		
def frame2(self):
	frame_data.frame_20(self)
	frame_data.frame_21(self)
	frame_data.frame_22(self)
	frame_data.frame_23(self)
	frame_data.frame_24(self)
	frame_data.frame_25(self)
	frame_data.frame_26(self)
	frame_data.frame_27(self)
	frame_data.frame_28(self)
	frame_data.frame_29(self)
	frame_data.frame_210(self)
	frame_data.view23.grid(row=0,column=1,padx=(0,0),pady=(7,0))
	
def frame3(self):
	sbar=Scrollbar(self)
	
	global view3
	view3=Listbox(self,width=192,height=8,bg='white',fg='blue')
	view3['yscrollcommand']=sbar.set
	sbar['command']=view3.yview
	view3.grid(row=1,column=0,columnspan=2,padx=(5,0),pady=(5,0))
	sbar.grid(row=1,column=3,rowspan=4,pady=(5,0),sticky=NS)
	now_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	view3.insert(END,now_time+'  当前用户：'+admin)



	
def main_interface(adm):
	global admin
	admin=adm
	root=Tk()
	root.title('监控系统')
	menu.makemenu(root)
	frame1(root)
	frame2(root)
	frame3(root)
	cursor=MultiCursor(frame_data.fig.canvas,(frame_data.ax1,
	frame_data.ax2),color='r',linewidth=1)	
	root.protocol("WM_DELETE_WINDOW",lambda:os._exit(0))
	root.mainloop()


	
	
		
		
