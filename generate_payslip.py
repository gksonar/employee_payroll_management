from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk
import random
import mysql.connector 

con=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Emp"
    )

cursor= con.cursor()

class generate_payslip:
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

        self.eid=StringVar()
        self.name=StringVar()
        self.dept=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()
        self.desg=StringVar()
        self.jd=StringVar()
        self.sal=StringVar()
        self.email=StringVar()
        self.leaves=StringVar()
        self.ot=StringVar()
        self.days=StringVar()
        self.leavesrupee=StringVar()
        self.overtrupee=StringVar()
        self.basic=StringVar()
        self.pf=StringVar()
        self.other=StringVar()
        self.medical=StringVar()
        self.net_sal=StringVar()
        self.month=StringVar()
        self.year=StringVar()
        self.address=StringVar()
        
        frame=Frame(self.root,bg="white",bd=5,relief=RIDGE)
        frame.place(x=10,y=80,width=700,height=130)      
        title_frame1=Label(frame,text="Generate a Salary Slip",height=2,width=20,font=("arial",30,"bold"),fg="black").place(x=100,y=10)

        frame1=Frame(self.root,bg="white",bd=5,relief=RIDGE)
        frame1.place(x=10,y=220,width=700,height=470)      
        title_frame1=Label(frame1,text="Employee Details",width=20,font=("arial",18,"bold"),bg="white",fg="red").place(x=2,y=1)
        
        lbl_eid=Label(frame1,text="Employee ID",font=("arial",14),bg="white").place(x=10,y=50)
        txt_name=Entry(frame1,font=("arial",14),bg="white",textvariable=self.eid).place(x=150,y=50,width=100)
        
        btn_find= Button(frame1,text = "Find" ,width=15,font=("arial",12,"bold"),command=self.find,bg="yellow",fg="red",pady=0).place(x=300,y=45,width=100)

        
        lbl_Name=Label(frame1,text="Name",font=("arial",14),bg="white").place(x=10,y=100)
        txt_name=Entry(frame1,font=("arial",14),bg="white",textvariable=self.name).place(x=120,y=100,width=200)
        
        lbl_dob=Label(frame1,text="DOB",font=("arial",14),bg="white").place(x=350,y=100)
        txt_dob=Entry(frame1,font=("arial",14),bg="white",textvariable=self.dob).place(x=460,y=100,width=200)
        #########
        lbl_salary=Label(frame1,text="Salary",font=("arial",14),bg="white").place(x=10,y=150)
        txt_salary=Entry(frame1,font=("arial",14),bg="white",textvariable=self.sal).place(x=120,y=150,width=200)
        
        lbl_doj=Label(frame1,text="DOJ",font=("arial",14),bg="white").place(x=350,y=150)
        txt_doj=Entry(frame1,font=("arial",14),bg="white",textvariable=self.jd).place(x=460,y=150,width=200)
        ########
        lbl_contact=Label(frame1,text="Contact",font=("arial",14),bg="white").place(x=10,y=200)
        txt_contact=Entry(frame1,font=("arial",14),bg="white",textvariable=self.contact).place(x=120,y=200,width=200)
        
        lbl_designation=Label(frame1,text="Designation",font=("arial",14),bg="white").place(x=350,y=200)
        txt_designation=Entry(frame1,font=("arial",14),bg="white",textvariable=self.desg).place(x=460,y=200,width=200)
        

        lbl_dept=Label(frame1,text="Department",font=("arial",14),bg="white").place(x=10,y=250)
        txt_dept=Entry(frame1,font=("arial",14),bg="white",textvariable=self.dept).place(x=120,y=250,width=200)
        
        lbl_mail=Label(frame1,text="Email",font=("arial",14),bg="white").place(x=350,y=250)
        txt_mail=Entry(frame1,font=("arial",14),bg="white",textvariable=self.email).place(x=460,y=250,width=200)
        ########
        lbl_lt=Label(frame1,text="Leaves",font=("arial",14),bg="white").place(x=10,y=300)
        txt_lt=Entry(frame1,font=("arial",14),bg="white",textvariable=self.leaves).place(x=120,y=300,width=200)
        
        lbl_ot=Label(frame1,text="Overtime(hr.)",font=("arial",14),bg="white").place(x=350,y=300)
        txt_ot=Entry(frame1,font=("arial",14),bg="white",textvariable=self.ot).place(x=460,y=300,width=200)
        
        lbl_add=Label(frame1,text="Address",font=("arial",14),bg="white").place(x=10,y=350)
        
        self.txt_add=Text(frame1,width=67,height=5,bd=2)
        self.txt_add.place(x=120,y=350)        
        #frame 2         
        frame2=Frame(self.root,bg="white",bd=5,relief=RIDGE)
        frame2.place(x=750,y=80,width=600,height=300)

        title_frame2=Label(frame2,text="Salary Details",width=20,font=("arial",18,"bold"),bg="white",fg="red").place(x=2,y=1)
        
        lbl_month=Label(frame2,text="Month",font=("arial",14),bg="white").place(x=10,y=50)
        txt_month=Entry(frame2,font=("arial",14),bg="white",textvariable=self.month).place(x=80,y=50,width=100)
        #btn_find= Button(frame2,text = "Find", width=15,font=("arial",12,"bold"),bg="yellow",fg="red",pady=0).place(x=300,y=45,width=100)
        lbl_year=Label(frame2,text="Year",font=("arial",14),bg="white").place(x=200,y=50)
        txt_year=Entry(frame2,font=("arial",14),bg="white",textvariable=self.year).place(x=250,y=50,width=100)
        
        lbl_sal=Label(frame2,text="Basic Salary",font=("arial",14),bg="white").place(x=370,y=50)
        txt_sal=Entry(frame2,font=("arial",14),bg="white",textvariable=self.basic).place(x=480,y=50,width=100)
        
        lbl_days=Label(frame2,text="Days",font=("arial",14),bg="white").place(x=10,y=100)
        txt_days=Entry(frame2,font=("arial",14),bg="white",textvariable=self.days).place(x=80,y=100,width=100)
        
        lbl_full_leaves=Label(frame2,text="Leave(Rs.)",font=("arial",14),bg="white").place(x=280,y=100)
        txt_full_leaves=Entry(frame2,font=("arial",14),bg="white",textvariable=self.leavesrupee).place(x=460,y=100,width=100)
        #########
           
        lbl_otp=Label(frame2,text="Overtime(Rs.)",font=("arial",14),bg="white").place(x=280,y=150)
        txt_otp=Entry(frame2,font=("arial",14),bg="white",textvariable=self.overtrupee).place(x=460,y=150,width=100)
        ########
        lbl_medical=Label(frame2,text="Medical",font=("arial",14),bg="white").place(x=10,y=150)
        txt_medical=Entry(frame2,font=("arial",14),bg="white",textvariable=self.medical).place(x=80,y=150,width=100)
        
        lbl_others=Label(frame2,text="Other(Rs.)",font=("arial",14),bg="white").place(x=280,y=200)
        txt_others=Entry(frame2,font=("arial",14),bg="white",textvariable=self.other).place(x=460,y=200,width=100)
        

        lbl_pf=Label(frame2,text="PF",font=("arial",14),bg="white").place(x=10,y=200)
        txt_pf=Entry(frame2,font=("arial",14),bg="white",textvariable=self.pf).place(x=80,y=200,width=100)
        
        lbl_netsal=Label(frame2,text="Net Salary",font=("arial",14),bg="white").place(x=10,y=250)
        txt_netsal=Entry(frame2,font=("arial",14),bg="white",textvariable=self.net_sal).place(x=110,y=250,width=100)
        
        btn_calculate= Button(frame2,text = "Calculate", width=15,font=("arial",12,""),command=self.calculate,bg="yellow",fg="red",pady=0).place(x=250,y=250,width=100)
        btn_pay= Button(frame2,text = "Receipt", width=15,font=("arial",12,""),bg="yellow",command=self.pay,fg="red",pady=0).place(x=375,y=250,width=100)
        btn_clear= Button(frame2,text = "Clear",command=self.reset ,width=15,font=("arial",12,""),bg="yellow",fg="red",pady=0).place(x=500,y=250,width=80)

       
        
        frame3=Frame(self.root,bg="white",bd=5,relief=RIDGE)
        frame3.place(x=750,y=390,width=600,height=300)
        title_sal=Label(frame3,text="Salary receipt",font=("arial",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        
        sal_frame2=Frame(frame3,bg="white",bd=2,relief=RIDGE)
        sal_frame2.place(x=0,y=37,relwidth=1,height=220)
        scroll_y=Scrollbar(sal_frame2,orient=VERTICAL)      
        scroll_y.pack(side=RIGHT,fill=Y)    
        self.txt_salary_receipt=Text(sal_frame2,font=("arial",12,"bold"),yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        
        btn_print= Button(frame3,text = "Pay", command=self.print,width=15,font=("arial",12,"bold"),bg="yellow",fg="red",pady=0).place(x=500,y=258,width=80)

    def find(self):
        eid=self.eid.get() 
         
        res=cursor.execute("SELECT * FROM `employee` WHERE `eid` = %s ", [self.eid.get()])
        row=cursor.fetchone()
        if row==None:            
            messagebox.showinfo("Error","Enter Valid ID ")
        else:
            print(row)
            self.eid.set(row[0])
            self.name.set(row[1])
            self.dept.set(row[2])
            self.sal.set(row[7])
            self.contact.set(row[3])
            self.dob.set(row[4])
            self.desg.set(row[5])
            self.email.set(row[8])
            self.jd.set(row[6])
            self.basic.set(row[7])
            self.address.set(row[8])
            self.txt_add.delete('1.0',END)
            self.txt_add.insert(END,row[9])

    def calculate(self):
        medic=1000
        medical=self.medical.set(medic)
        others=1000
        other=self.other.set(others)
        pfs=1500
        pf=self.pf.set(pfs)
        basic_sal=int(self.sal.get())
        leaves=int(self.leaves.get())
        salary=int(self.sal.get())
        days=int(self.days.get())
        overtimehr=int(self.ot.get())
        workday=days-leaves
        perday=salary/days
        lrupee=leaves*perday
        onehrsal=perday/8;
        orupee=(50+onehrsal)*overtimehr
        self.leavesrupee.set(int(lrupee))
        self.overtrupee.set(int(orupee))
        
        netsal=basic_sal-pfs-medic-others-lrupee+orupee
        self.net_sal.set(int(netsal))
        
    def pay(self):
        n=random.randint(1,99999)
        self.txt_salary_receipt.delete("1.0", END)
        self.txt_salary_receipt.insert(END, "\t\tPay Slip \t\t Receipt No. "+str(n)+"\n\n")
        self.txt_salary_receipt.insert(END, "Employee ID:\t\t" + self.eid.get() + "\n\n")
        self.txt_salary_receipt.insert(END, "Full Name :\t\t" + self.name.get() + "\t\t Contact :\t" + self.contact.get() + "\n\n")
        self.txt_salary_receipt.insert(END, "Leaves :\t\t" +self.leaves.get()+ "\t\t Leaves charges Rs. \t\t"+self.leavesrupee.get()+"\n\n")
        self.txt_salary_receipt.insert(END, "overtime (hours) :\t\t" + self.ot.get() + "\t\t Overtime charges Rs. \t\t"+self.overtrupee.get()+"\n\n")
        self.txt_salary_receipt.insert(END, "Medical :\t\t" + self.medical.get() + "\n\n")
        self.txt_salary_receipt.insert(END, "PF :\t\t" + self.pf.get() + "\n\n")
        self.txt_salary_receipt.insert(END, "Others. :\t\t" + self.other.get() + "\n\n")
        self.txt_salary_receipt.insert(END, "Nat Salary :\t\t" + self.net_sal.get()+ "\n\n")
            
    def print(self):
        eid=self.eid.get()
        leaves=self.leaves.get()
        overtime=self.ot.get()
        pf=self.pf.get()
        medical=self.medical.get()
        other=self.other.get()
        leavesrs=self.leavesrupee.get()
        overtimers=self.overtrupee.get()
        net_sal=self.net_sal.get()
        month=self.month.get()
        year=self.year.get()
        basic=self.basic.get()
        
        if self.eid.get()=="":
             messagebox.showinfo("Alert","Id Should be Mandatory *")
        elif self.net_sal.get()=="":
             messagebox.showinfo("Alert","Net Salary Cant be Empty")
    
        else:
            cursor.execute("SELECT * FROM `salary_detail` WHERE `eid` = %s", [self.eid.get()])
            if cursor.fetchone() is not None:
                messagebox.showinfo("Message","Employee Salary already Paid!!!")
            else:
                res=cursor.execute("INSERT INTO `salary_detail`( `eid`, `leaves`, `overtime`, `pf`, `other`, `medical`, `leavesrs`, `overtimers`, `net_sal`, `month`, `year`, `basic_sal`) VALUES( %s, %s,%s,%s, %s, %s, %s,%s,%s, %s, %s,%s)", (str(eid), str(leaves), str(overtime), str(pf),str(medical), str(other), str(leavesrs), str(overtimers), str(net_sal),str(month),str(year),str(basic) ))
                messagebox.showinfo("Message","Salary Paid Succesfully")      
                con.commit()
         
    def reset(self):
        self.eid.set("")
        self.name.set("")
        self.dept.set("")
        self.contact.set("")
        self.dob.set("")
        self.desg.set("")
        self.jd.set("")
        self.sal.set("")
        self.email.set("")
        self.leaves.set("")
        self.ot.set("")
        self.days.set("")
        self.leavesrupee.set("")
        self.overtrupee.set("")
        self.basic.set("")
        self.pf.set("")
        self.other.set("")
        self.medical.set("")
        self.net_sal.set("")
        self.month.set("")
        self.year.set("")
        self.address.set("")
            
        
root=Tk()
obj=generate_payslip(root)
root.mainloop()


