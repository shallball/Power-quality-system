# coding=gbk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter.messagebox import *
import sys,frame,os

	
def account(self):	#账号密码等控件
	self.title("监控系统")
	text1=Label(self,text="账号：",bg='white')
	text1.grid(row=0,column=0,padx=(130,0),pady=(70,150))
	text1=Label(self,text="密码：",bg='white')
	text1.grid(row=0,column=0,padx=(130,0),pady=(100,120))
	ent1=Entry(self,width=15)
	ent2=Entry(self,width=15,show='*')
	ent1.grid(row=0,column=1,padx=(10,130),pady=(67,150))
	ent2.grid(row=0,column=1,padx=(10,130),pady=(97,120))
	btnlogin=ttk.Button(self,text='登录',width=5,
	command=lambda:register(self,ent1,ent2,1))
	btnlogin.grid(row=0,column=0,padx=(130,0),pady=(150,70))
	btnregister=ttk.Button(self,text='注册',width=5,
	command=lambda:register(self,ent1,ent2,2))
	btnregister.grid(row=0,column=1,padx=(60,110),pady=(150,70))
	

def imagebg(self):	#背景图片
	img=ImageTk.PhotoImage(file="images/1.jpg")
	imag=Label(self,image=img)
	imag.image=img
	imag.place(x=-3,y=-3)
	
	
def register(self,ent1,ent2,log):		#注册
	filename='account.txt'
	account_list=[]
	adm=ent1.get()
	pas=ent2.get()
	if len(adm)<6 or len(pas)<6:
		showinfo('提示','账号和密码的长度至少为6位')
	else:
		with open(filename) as acc:
			acc_data=acc.read()
		if acc_data=='':
			exi=0
		else:
			acc_data=eval(acc_data)
			for acc_admin in acc_data:
				account_list.append(acc_admin.copy())
				if acc_admin['admin']==adm:
					exi=1
					if acc_admin['password']==pas:
						exi=2
						break
				else:
					exi=0
		if exi==0 and log==2:
			new_account={}
			new_account['admin']=adm
			new_account['password']=pas
			account_list.append(new_account.copy())
			with open(filename,'w') as acc:
				acc.write(str(account_list))
				acc.close()
				showinfo('提示','注册成功')
				os.makedirs('.\\users\\'+adm)
		if exi!=0 and log==2:
			showinfo('提示','账号已被注册')
		if exi==2 and log==1:
			showinfo('提示','登录成功')
			self.destroy()	
			frame.main_interface(adm)
		if exi!=2 and log==1:
			showinfo('提示','账号或密码错误')

def account_login():
	root=Tk()
	imagebg(root)
	account(root)	
	root.resizable(0,0)
	root.protocol("WM_DELETE_WINDOW",lambda:os._exit(0))
	root.mainloop()
	
if __name__=='__main__':
	account_login()	







