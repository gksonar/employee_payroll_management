import os
import sys
from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk

import mysql.connector


con=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Emp"    
    )

cursor= con.cursor()
class add_holiday:
    def disp_dashboard(self):
        root.destroy();
        os.system('python hr.py');
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll System")
        self.root.geometry("1350x768+0+0")
        
        #all Images
 
        
        self.bg_icon=ImageTk.PhotoImage(file="images/Payrollfinal.jpg")
        self.employee_icon=ImageTk.PhotoImage(file="images/employee.png")
        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        title=Label(self.root,text="Employee Payroll System",font=("times new roman",30,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)        
        title.place(x=0,y=0,relwidth=1)        
        
        self.hdate=StringVar()
        self.hdesc=StringVar()
        
        addholiday_Frame1=Frame(self.root,bg="white")
        addholiday_Frame1.place(x=1200,y=12)        
        btn_log1=Button(addholiday_Frame1,text="Dashboard",command=self.disp_dashboard,height=1,width=10,font=("arial",16,"bold"),bg="lightgray",fg="black").grid(row=3,column=0,pady=0)
  
        addholiday_frame=Frame(self.root,bg="white")
        addholiday_frame.place(x=200,y=200)
        
        logolbl=Label(addholiday_frame,text="",image=self.employee_icon,bd=0).grid(row=0,columnspan=2,pady=0)
        btn_log=Label(addholiday_frame,text="Add Holiday",height=2,width=20,font=("arial",18,"bold"),bg="white",fg="red").grid(row=3,column=1,pady=0)
           
        addholiday_frame=Frame(self.root,bg="")
        addholiday_frame.place(x=750,y=220)
        
        lbluser=Label(addholiday_frame,compound=LEFT,font=("times new roman",16,"bold"),bg="white").grid(row=1,column=0,padx=0,pady=2)
                
        lbl_date=Label(addholiday_frame,text="Date",compound=LEFT,font=("times new roman",16,"bold")).grid(row=2,column=0,padx=0,pady=10)
        txt_date=Entry(addholiday_frame,bd=2,width=20,textvariable=self.hdate,relief=GROOVE,font=("",12)).grid(row=2,column=1,padx=20)

        lbl_desc=Label(addholiday_frame,text="Description",font=("times new roman",16,"bold"))
        lbl_desc.grid(row=3,column=0,padx=0,pady=10)
        self.txt_desc=Text(addholiday_frame,width=23,height=4,bd=2)
        self.txt_desc.grid(row=3,column=1,padx=20,pady=10)

        btn_addholiday=Button(addholiday_frame,text="Add Holiday",command=self.add_holiday,width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=4,column=1,padx=0,pady=20)
        btn_clear=Button(addholiday_frame,text = "Reset",command=self.reset,width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=4,column=0,padx=20,pady=20)
     
     
    def add_holiday(self):
        hdate=self.hdate.get() 
        desc=self.txt_desc.get('1.0',END)

        if self.hdate.get()=="":
             messagebox.showinfo("Alert","Enter Date")
        elif self.txt_desc.get('1.0',END)=="":
             messagebox.showinfo("Alert","Enter Description")
        else:
            cursor.execute("SELECT * FROM `holiday` WHERE `hdate` = %s", [self.hdate.get()])
            if cursor.fetchone() is not None:
                messagebox.showinfo("Message","Date Already Exists")
            else:
                res=cursor.execute("INSERT INTO `holiday` ( `hdate`, `hdescription`) VALUES(%s, %s)",(str(hdate), str(desc)))
                messagebox.showinfo("Message","Holiday Added Succesfully")
                
                con.commit()                
                self.reset()
                
    def reset(self):
        
        self.hdate.set("") 
        self.txt_desc.delete('1.0',END)
            
root=Tk()
obj=add_holiday(root)
root.mainloop()






