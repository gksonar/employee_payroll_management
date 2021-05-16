import sys
import os
from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk
class index_page:
    def demo(self):
        root.destroy();
        os.system('python emp_login.py');
    def demo2(self):
        root.destroy();
        os.system('python hr_login.py');
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll System")
        self.root.geometry("1350x7000+0+0")
        
        self.bg_icon=ImageTk.PhotoImage(file="images/Payrollfinal.jpg")   
        self.employee_icon=ImageTk.PhotoImage(file="images/employee.png")
        self.hr_icon=ImageTk.PhotoImage(file="images/hr1.png")
        
        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        title=Label(self.root,text="Employee Payroll System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        emp_frame=Frame(self.root,bg="white")
        emp_frame.place(x=300,y=150)
        
        logo_employee=Label(emp_frame,text="",image=self.employee_icon,bd=0).grid(row=0,columnspan=2,pady=0)
        btn_employee=Button(emp_frame,text="Employee",width=20,font=("times new roman",14,"bold"),bg="yellow",fg="red",command=self.demo).grid(row=3,column=0,pady=0)
        
        hr_frame1=Frame(self.root,bg="white")
        hr_frame1.place(x=800,y=150)
        
        logo_hr=Label(hr_frame1,text="",image=self.hr_icon,bd=0).grid(row=0,columnspan=4,pady=0)
        btn_hr=Button(hr_frame1,text="HR",width=20,font=("times new roman",14,"bold"),bg="yellow",fg="red",command=self.demo2).grid(row=3,column=0,pady=0)
    
        
root=Tk()
obj=index_page(root)
root.mainloop()
