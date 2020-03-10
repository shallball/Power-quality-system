# coding=gbk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import account as acc
import save,frame


def change_admin(self):
	self.destroy()
	acc.account_login()


def about():
	root=Tk()
	root.resizable(0,0)
	root.title('关于')
	Label(root,text='作者：黄凯').grid(padx=10,pady=10,sticky=W)
	Label(root,text='邮箱：1132970244@qq.com').grid(padx=10,pady=10,sticky=W)
	ttk.Button(root,text='确定',command=root.destroy).grid(padx=10,pady=10)
	root.mainloop()
		
def makemenu(win):
	global flag_save
	flag_save=0
	top=Menu(win)
	win.config(menu=top)
	sys=Menu(top,tearoff=False)
	sys.add_command(label='切换用户',
	command=lambda:change_admin(win),underline=0)
	top.add_cascade(label='系统',menu=sys,underline=0)
	
	analysis=Menu(top,tearoff=False)
	analysis.add_command(label='电压和频率偏差',
	command=lambda:frame.switch(8),underline=0)
	analysis.add_command(label='谐波分析',
	command=lambda:frame.switch(9),underline=0)
	analysis.add_command(label='三相不平衡',
	command=lambda:frame.switch(10),underline=0)
	top.add_cascade(label='电能质量显示',menu=analysis,underline=0)
	
	view=Menu(top,tearoff=False)
	view.add_command(label='A相有效值波形图',
	command=lambda:frame.switch(0),underline=0)
	view.add_command(label='B相有效值波形图',
	command=lambda:frame.switch(1),underline=0)
	view.add_command(label='C相有效值波形图',
	command=lambda:frame.switch(2),underline=0)
	view.add_command(label='A相瞬时值波形图',
	command=lambda:frame.switch(3),underline=0)
	view.add_command(label='B相瞬时值波形图',
	command=lambda:frame.switch(4),underline=0)
	view.add_command(label='C相瞬时值波形图',
	command=lambda:frame.switch(5),underline=0)
	view.add_command(label='电流电压数据表  ',
	command=lambda:frame.switch(6),underline=0)
	view.add_command(label='三相功率数据表  ',
	command=lambda:frame.switch(7),underline=0)
	top.add_cascade(label='基本电量显示',menu=view,underline=0)

	
	tool=Menu(top,tearoff=False)
	tool.add_command(label='开始记录',
	command=save.save_start,underline=0)
	tool.add_command(label='结束记录',
	command=save.save_stop,underline=0)
	tool.add_command(label='历史数据查询',
	command=save.save_window,underline=0)
	top.add_cascade(label='数据记录',menu=tool,underline=0)
	

	help=Menu(top,tearoff=False)
	help.add_command(label='关于',command=about,underline=0)
	top.add_cascade(label='帮助',menu=help,underline=0)


	

