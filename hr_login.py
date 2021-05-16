import os
import sys
from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk
# import sqlite3

class hr_login:
     def login(self):
        if((self.uname.get()=="HR" or self.uname.get()=="hr")and(self.upass.get()=="Payroll@2021")):
            os.system('python hr.py');
        elif(self.uname.get()=="" or self.upass.get()==""):
            messagebox.showerror("Error", "All fields are Empty!!")
        elif (self.uname.get()=="shop" and self.upass.get()=="1234"):
            messagebox.showinfo("Sucessfull",f"welcome {self.uname.get()}")
            self.abc()
        else:
            messagebox.showerror("Error","Invalid Username and Password")

     def reset_values(self):
        self.uname.set("")
        self.upass.set("")
        
     def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll System")
        self.root.geometry("1350x768+0+0")
        
        #all Images 
        self.bg_icon=ImageTk.PhotoImage(file="images/PayrollFinal.jpg")
        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        title=Label(self.root,text="Employee Payroll System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        
        self.uname=StringVar()
        self.upass=StringVar()
        
        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=400,y=150)
        
        logolbl=Label(Login_Frame,text="HR Login",font=("ARIAL",20,"bold"),bd=0,bg="white",fg="Blue").grid(row=0,columnspan=2,pady=20)
        
        lblhrid=Label(Login_Frame,text="Hr id",compound=LEFT,font=("times new roman",20,"bold")).grid(row=1,column=0,padx=20,pady=10)
        txthrid=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)
        
        lblpass=Label(Login_Frame,text="Password",compound=LEFT,font=("times new roman",20,"bold")).grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(Login_Frame,bd=5, show="*",textvariable=self.upass,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)
        
        btn_hr_log=Button(Login_Frame,text="Login", command=self.login,width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=20)
        reset = Button(Login_Frame,text = "Reset", command =self.reset_values,width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=0,padx=10,pady=20)
         
    
   
   
root=Tk()
obj=hr_login(root)
root.mainloop()

