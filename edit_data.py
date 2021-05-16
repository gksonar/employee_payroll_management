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
    database="emp"
    )

cursor= con.cursor()

class edit_data():
    def disp_d(self):
        root.destroy();root.destroy();
        os.system('python employee.py');
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
  
        addemp_frame1=Frame(self.root,bg="white")
        addemp_frame1.place(x=1200,y=12)        
        btn_log1=Button(addemp_frame1,text="Dashboard",command=self.disp_d,height=1,width=10,font=("arial",16,"bold"),bg="lightgray",fg="black").grid(row=3,column=0,pady=0)
  
        addemp_frame=Frame(self.root,bg="white")
        addemp_frame.place(x=200,y=200)
        
        logolbl=Label(addemp_frame,text="",image=self.employee_icon,bd=0).grid(row=0,columnspan=2,pady=0)
        btn_log=Label(addemp_frame,text="Edit Data",height=2,width=20,font=("arial",18,"bold"),bg="white",fg="red").grid(row=3,column=1,pady=0)
             
        addemp_frame=Frame(self.root,bg="")
        addemp_frame.place(x=750,y=85)
        self.eid=StringVar()
        self.name=StringVar()
        self.dept=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()
        self.desg=StringVar()
        self.jd=StringVar()
        self.sal=StringVar()
        self.address=StringVar()
        
        lbl_eid=Label(addemp_frame,text="Eid",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=0,pady=10)
        txt_eid=Entry(addemp_frame,bd=5,width=20,relief=GROOVE,font=("",12),textvariable=self.eid).grid(row=1,column=1,padx=20)
   
        lbl_contact=Label(addemp_frame,text="Contact",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=20,pady=10)
        txt_contact=Entry(addemp_frame,bd=5,width=20,relief=GROOVE,font=("",12),textvariable=self.contact).grid(row=2,column=1,padx=20)

        btn_edit=Button(addemp_frame,text="Find", width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red",command=self.find).grid(row=3,column=1,padx=0,pady=20)

        lbl_name=Label(addemp_frame,text="Name",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=20,pady=10)
        txt_name=Entry(addemp_frame,bd=5,width=20,relief=GROOVE,font=("",12),textvariable=self.name).grid(row=4,column=1,padx=20)
        
         
        lbl_dept=Label(addemp_frame,text="Department",font=("times new roman",16,"bold")).grid(row=5,column=0,padx=20,pady=10)
        txt_dept=Entry(addemp_frame,bd=5,width=20, relief=GROOVE,font=("",12),textvariable=self.dept).grid(row=5,column=1,padx=20)
        
 
        lbl_dob=Label(addemp_frame,text="DOB",font=("times new roman",16,"bold")).grid(row=6,column=0,padx=20,pady=10)
        txt_dob=Entry(addemp_frame,bd=5,width=20, relief=GROOVE,font=("",12),textvariable=self.dob).grid(row=6,column=1,padx=20)
        
        lbl_desg=Label(addemp_frame,text="Designation",font=("times new roman",16,"bold")).grid(row=7,column=0,padx=20,pady=10)
        txt_desg=Entry(addemp_frame,bd=5,width=20, relief=GROOVE,font=("",12),textvariable=self.desg).grid(row=7,column=1,padx=20)
        
        lbl_jd=Label(addemp_frame,text="Join Date",font=("times new roman",16,"bold")).grid(row=8,column=0,padx=20,pady=10)
        txt_jd=Entry(addemp_frame,bd=5,width=20, relief=GROOVE,font=("",12),textvariable=self.jd).grid(row=8,column=1,padx=20)  
           
        lbl_sal=Label(addemp_frame,text="Salary",font=("times new roman",16,"bold"),).grid(row=9,column=0,padx=20,pady=10)
        txt_sal=Entry(addemp_frame,bd=5,width=20, relief=GROOVE,font=("",12),textvariable=self.sal).grid(row=9,column=1,padx=20)
   
        btn_edit=Button(addemp_frame,text="Edit", width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red",command=self.edit).grid(row=10,column=1,padx=0,pady=20)
        btn_clear= Button(addemp_frame,text = "Reset", width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red",command=self.reset).grid(row=10,column=0,padx=20,pady=20)

        
    def find(self):
        eid=self.eid.get() 
        contact=self.contact.get() 
        res=cursor.execute("SELECT * FROM `employee` WHERE `eid` = %s AND contact=%s", [self.eid.get(),self.contact.get()])
        row=cursor.fetchone()
        if row==None:            
            messagebox.showinfo("Error","Enter Valid ID ")
        else:
            self.eid.set(row[0])
            self.name.set(row[1])
            self.dept.set(row[2])
            self.contact.set(row[3])
            self.dob.set(row[4])
            self.desg.set(row[5])
            self.jd.set(row[6])
            self.sal.set(row[7])
            self.address.set(row[8])
  
        
    def edit(self):
        eid=self.eid.get()
        name=self.name.get()
        dept=self.dept.get()
        contact=self.contact.get()
        dob=self.dob.get()
        desg=self.desg.get()
        jd=self.jd.get()
        sal=self.sal.get()

        if self.name.get()=="":
             messagebox.showinfo("Alert","Enter Name")
        elif self.dept.get()=="":
             messagebox.showinfo("Alert","Enter Department")
        elif self.contact.get()=="":
             messagebox.showinfo("Alert","Enter Contact")
        elif self.dob.get()=="":
             messagebox.showinfo("Alert","Enter DOB")
        elif self.desg.get()=="":
             messagebox.showinfo("Alert","Enter Designation")
        elif self.jd.get()=="":
             messagebox.showinfo("Alert","Enter Join date")
        elif self.sal.get()=="":
             messagebox.showinfo("Alert","Enter Salary")
        else:
            res=cursor.execute("UPDATE `employee` SET `name`=%s,`department`=%s,`contact`=%s,`dob`=%s,`designation`=%s,`join_date`=%s,`salary`=%s WHERE `eid`=%s", (str(name), str(dept),  str(dob),str(desg), str(jd), str(sal),str(contact),str(eid) ))
            messagebox.showinfo("Message","Employee Updated Succesfully")
            con.commit()
            self.reset()
            
            
    def reset(self):
        self.eid.set("") 
        self.name.set("") 
        self.dept.set("") 
        self.contact.set("") 
        self.dob.set("") 
        self.desg.set("") 
        self.jd.set("") 
        self.sal.set("") 
        
            
        
        
root=Tk()
obj=edit_data(root)
root.mainloop()

