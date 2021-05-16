import sys
import os
from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk
class hr:
    def add_e(self):
        os.system('python add_employee.py');
    def manage_e(self):
        os.system('python manage_employee.py');
    def add_h(self):
        os.system('python add_holiday.py');
    def manage_h(self):
        os.system('python manage_holiday.py');
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll System")
        self.root.geometry("1350x768+0+0")
        
        self.bg_icon=ImageTk.PhotoImage(file="images/Payrollfinal.jpg")   
        self.employee_icon=ImageTk.PhotoImage(file="images/employee.png")
        self.hr_icon=ImageTk.PhotoImage(file="images/hr1.png")
        
        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        title=Label(self.root,text="Employee Payroll System",font=("arial",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        
        hr_frame1=Frame(self.root,bg="white")
        hr_frame1.place(x=550,y=100)      
        btn_log=Label(hr_frame1,text="HR (Human Resource)",height=2,width=20,font=("arial",18,"bold"),bg="white",fg="red").grid(row=3,column=0,pady=0)


        hr_frame=Frame(self.root,bg="white")
        hr_frame.place(x=350,y=200)      
        btn_log=Button(hr_frame,text="Add Employees",command=self.add_e,height=2,width=20,font=("arial",16,"bold"),bg="yellow",fg="red").grid(row=3,column=0,pady=0)
            
        hr_frame=Frame(self.root,bg="white")
        hr_frame.place(x=350,y=350)
        btn_log1=Button(hr_frame,text="Manage Employees",command=self.manage_e,height=2,width=20,font=("arial",16,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=0)

        hr_frame=Frame(self.root,bg="white")
        hr_frame.place(x=750,y=200)        
        btn_log1=Button(hr_frame,text="Add Holidays",height=2,command=self.add_h,width=20,font=("arial",16,"bold"),bg="yellow",fg="red").grid(row=3,column=0,pady=0)
        
        hr_frame=Frame(self.root,bg="white")
        hr_frame.place(x=750,y=350)        
        btn_log1=Button(hr_frame,text="Manage Holidays",command=self.manage_h,height=2,width=20,font=("arial",16,"bold"),bg="yellow",fg="red").grid(row=3,column=0,pady=0)
        
root=Tk()
obj=hr(root)
root.mainloop()

