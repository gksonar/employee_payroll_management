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

class add_employee:
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
        btn_log1=Button(addemp_frame1,text="Dashboard",height=1,width=10,font=("arial",16,"bold"),bg="lightgray",fg="black").grid(row=3,column=0,pady=0)
  
        addemp_frame=Frame(self.root,bg="white")
        addemp_frame.place(x=200,y=200)
        
        logolbl=Label(addemp_frame,text="",image=self.employee_icon,bd=0).grid(row=0,columnspan=2,pady=0)
        lbl_add=Label(addemp_frame,text="Add Employee",height=2,width=20,font=("arial",18,"bold"),bg="white",fg="red").grid(row=3,column=1,pady=0)
             
        addemp_frame=Frame(self.root,bg="")
        addemp_frame.place(x=750,y=85)
        
        
        
        self.name=StringVar()
        self.dept=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()
        self.desg=StringVar()
        self.jd=StringVar()
        self.sal=StringVar()
        self.email=StringVar()
        self.address=StringVar()
    
       # lbl_eid=Label(addemp_frame,text="E ID",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=0,pady=10)
       # txt_eid=Entry(addemp_frame,bd=2,width=20,relief=GROOVE,font=("",12)).grid(row=1,column=1,padx=20)
        
        lbl_name=Label(addemp_frame,text="Name",font=("times new roman",16,"bold")).grid(row=3,column=0,padx=20,pady=10)
        txt_name=Entry(addemp_frame,bd=2,width=20,textvariable=self.name,relief=GROOVE,font=("",12)).grid(row=3,column=1,padx=20)
         
        lbl_dept=Label(addemp_frame,text="Department",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=20,pady=10)
        txt_dept=Entry(addemp_frame,bd=2,width=20,textvariable=self.dept, relief=GROOVE,font=("",12)).grid(row=4,column=1,padx=20)
        
        lbl_contact=Label(addemp_frame,text="Contact",font=("times new roman",16,"bold")).grid(row=5,column=0,padx=20,pady=10)
        txt_contact=Entry(addemp_frame,bd=2,width=20,textvariable=self.contact,relief=GROOVE,font=("",12)).grid(row=5,column=1,padx=20)
        
        lbl_dob=Label(addemp_frame,text="DOB",font=("times new roman",16,"bold")).grid(row=6,column=0,padx=20,pady=10)
        txt_dob=Entry(addemp_frame,bd=2,width=20, textvariable=self.dob, relief=GROOVE,font=("",12)).grid(row=6,column=1,padx=20)
        
        lbl_desg=Label(addemp_frame,text="Designation",font=("times new roman",16,"bold")).grid(row=7,column=0,padx=20,pady=10)
        txt_desg=Entry(addemp_frame,bd=2,width=20, textvariable=self.desg, relief=GROOVE,font=("",12)).grid(row=7,column=1,padx=20)
        
        lbl_jd=Label(addemp_frame,text="Join Date",font=("times new roman",16,"bold")).grid(row=8,column=0,padx=20,pady=10)
        txt_jd=Entry(addemp_frame,bd=2,width=20, textvariable=self.jd, relief=GROOVE,font=("",12)).grid(row=8,column=1,padx=20)  
           
        lbl_sal=Label(addemp_frame,text="Salary",font=("times new roman",16,"bold"),).grid(row=9,column=0,padx=20,pady=10)
        txt_sal=Entry(addemp_frame,bd=2,width=20, textvariable=self.sal, relief=GROOVE,font=("",12)).grid(row=9,column=1,padx=20)
        
        lbl_email=Label(addemp_frame,text="E-Mail",font=("times new roman",16,"bold"),).grid(row=10,column=0,padx=20,pady=10)
        txt_email=Entry(addemp_frame,bd=2,width=20, textvariable=self.email, relief=GROOVE,font=("",12)).grid(row=10,column=1,padx=20)
        
        
#        lbl_city=Label(addemp_frame,text="City",font=("times new roman",16,"bold"),).grid(row=11,column=0,padx=20,pady=10)
#        txt_city=Entry(addemp_frame,bd=2,width=20, textvariable=self.address, relief=GROOVE,font=("",12)).grid(row=11,column=1,padx=20)
        
        lbl_add=Label(addemp_frame,text="Address",font=("times new roman",16,"bold"))
        lbl_add.grid(row=11,column=0,padx=0,pady=10)
        self.txt_add=Text(addemp_frame,width=23,height=4,bd=2)
        self.txt_add.grid(row=11,column=1,padx=20,pady=10)

        btn_addemp=Button(addemp_frame,text="Add Employee", command=self.add_emp,width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=12,column=1,padx=0,pady=20)
        btn_clear= Button(addemp_frame,text = "Reset",command=self.reset, width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").place(x=40,y=510,width=100)
        
    def add_emp(self):
        name=self.name.get() 
        dept=self.dept.get() 
        contact=self.contact.get() 
        dob= self.dob.get() 
        desg=self.desg.get() 
        jd=self.jd.get() 
        sal=self.sal.get() 
        email=self.email.get()
        add=self.txt_add.get('1.0',END)

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
        elif self.email.get()=="":
             messagebox.showinfo("Alert","Enter Email")
        elif self.txt_add.get('1.0',END)=="":
             messagebox.showinfo("Alert","Enter Address") 
        else:
            cursor.execute("SELECT * FROM `employee` WHERE `contact` = %s", [self.contact.get()])
            if cursor.fetchone() is not None:
                messagebox.showinfo("Message","Employee Already Exists")
            else:
                res=cursor.execute("INSERT INTO `employee` (`name`, `department`, `contact`, `dob`, `designation`, `join_date`, `salary`, `email`, `address`) VALUES(%s, %s, %s, %s,%s,%s, %s, %s, %s)", (str(name), str(dept), str(contact), str(dob),str(desg), str(jd), str(sal), str(email),str(add)))
                messagebox.showinfo("Message","Employee Added Succesfully")
                self.reset()
                con.commit()

    def reset(self):
        self.name.set("") 
        self.dept.set("") 
        self.contact.set("") 
        self.dob.set("") 
        self.desg.set("") 
        self.jd.set("") 
        self.sal.set("") 
        self.email.set("")
        self.address.set("")
        self.txt_add.delete('1.0',END)     
root=Tk()
obj=add_employee(root)
root.mainloop()

