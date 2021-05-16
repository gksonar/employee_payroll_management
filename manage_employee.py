from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
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
class manage_employee:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll System")
        self.root.geometry("1350x760+0+0")
        
        self.bg_icon=ImageTk.PhotoImage(file="images/Payrollfinal.jpg")
        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        
        title=Label(self.root,text="Employee Payroll System",font=("times new roman",30,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)        
        title.place(x=0,y=0,relwidth=1)
        
        
        self.name=StringVar()
        self.dept=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()
        self.desg=StringVar()
        self.jd=StringVar()
        self.sal=StringVar()
        self.email=StringVar()
        self.address=StringVar()
        self.search_by=StringVar()
        self.search_text=StringVar()
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
                
        manage_frame=Frame(self.root,bd=4,relief=RIDGE, bg="white")
        manage_frame.place(x=20,y=90,width=450,height=560)
        
        m_title=Label(manage_frame,text="Add Employee",height=2,width=20,font=("arial",18,"bold"),bg="white",fg="red")
        m_title.grid(row=0,columnspan=2,pady=10)
        
               
        lbl_name=Label(manage_frame,text="Name",font=("arial",14),bg="white")
        lbl_name.grid(row=1,column=0,pady=5,padx=10,sticky="w")        
        txt_name=Entry(manage_frame,font=("arial",12),bd=2,relief=GROOVE,textvariable=self.name)
        txt_name.grid(row=1,column=1,pady=5,padx=20,sticky="w")
        
        lbl_dept=Label(manage_frame,text="Department",font=("arial",14),bg="white")
        lbl_dept.grid(row=2,column=0,pady=5,padx=10,sticky="w")        
        txt_dept=Entry(manage_frame,font=("arial",12),bd=2,relief=GROOVE,textvariable=self.dept)
        txt_dept.grid(row=2,column=1,pady=5,padx=20,sticky="w")

        lbl_contact=Label(manage_frame,text="Contact",font=("arial",14),bg="white")
        lbl_contact.grid(row=3,column=0,pady=5,padx=10,sticky="w")        
        txt_contact=Entry(manage_frame,font=("arial",12),bd=2,relief=GROOVE,textvariable=self.contact)
        txt_contact.grid(row=3,column=1,pady=5,padx=20,sticky="w")
        
        lbl_dob=Label(manage_frame,text="DOB",font=("arial",14),bg="white")
        lbl_dob.grid(row=4,column=0,pady=5,padx=10,sticky="w")        
        txt_dob=Entry(manage_frame,font=("arial",12),bd=2,relief=GROOVE,textvariable=self.dob)
        txt_dob.grid(row=4,column=1,pady=5,padx=20,sticky="w")

        lbl_desg=Label(manage_frame,text="Designation",font=("arial",14),bg="white")
        lbl_desg.grid(row=5,column=0,pady=5,padx=10,sticky="w")        
        txt_desg=Entry(manage_frame,font=("arial",12),bd=2,relief=GROOVE,textvariable=self.desg)
        txt_desg.grid(row=5,column=1,pady=5,padx=20,sticky="w")
        
        lbl_jd=Label(manage_frame,text="Join Date",font=("arial",14),bg="white")
        lbl_jd.grid(row=6,column=0,pady=5,padx=10,sticky="w")        
        txt_jd=Entry(manage_frame,font=("arial",12),bd=2,relief=GROOVE,textvariable=self.jd)
        txt_jd.grid(row=6,column=1,pady=5,padx=20,sticky="w")

        lbl_email=Label(manage_frame,text="Email",font=("arial",14),bg="white")
        lbl_email.grid(row=7,column=0,pady=5,padx=10,sticky="w")        
        txt_email=Entry(manage_frame,font=("arial",12),bd=2,relief=GROOVE,textvariable=self.email)
        txt_email.grid(row=7,column=1,pady=5,padx=20,sticky="w")
        
        lbl_sal=Label(manage_frame,text="Salary",font=("arial",14),bg="white")
        lbl_sal.grid(row=8,column=0,pady=5,padx=10,sticky="w")        
        txt_sal=Entry(manage_frame,font=("arial",12),bd=2,relief=GROOVE,textvariable=self.sal)
        txt_sal.grid(row=8,column=1,pady=5,padx=20,sticky="w")
        
        lbl_add=Label(manage_frame,text="Address",font=("arial",14),bg="white")
        lbl_add.grid(row=9,column=0,pady=10,padx=10,sticky="w")        
        self.txt_add=Text(manage_frame,bd=2,width=24,height=4)
        self.txt_add.grid(row=9,column=1,pady=10,padx=10,)
        
        btn_frame=Frame(manage_frame,bd=4,relief=RIDGE, bg="White")
        btn_frame.place(x=9,y=490,width=430)
        
        addbtn=Button(btn_frame,text="Add",width=8,bg="skyblue",command= self.add_employee,font=("arial",10,"bold")).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_frame,text="Update",width=10,bg="green",command= self.update_employee,font=("arial",10,"bold")).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_frame,text="Delete",width=10,bg="red",command= self.delete_employee,font=("arial",10,"bold")).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_frame,text="Clear",width=10,bg="lightgray",command= self.reset,font=("arial",10,"bold")).grid(row=0,column=3,padx=10,pady=10)
  
        info_frame=Frame(self.root,bd=4,relief=RIDGE, bg="white")
        info_frame.place(x=500,y=90,width=800,height=560)
        
        lblsearch=Label(info_frame,text="Search By",font=("arial",14))
        lblsearch.grid(row=0,column=0,pady=10,padx=10,sticky="w")
        
        combo_search=ttk.Combobox(info_frame,width=10,font=("arial",14),state="readonly" ,textvariable=self.search_by)
        combo_search['values']=('name','contact','desgination','department')
        combo_search.grid(row=0,column=1,pady=10,padx=10,sticky="w")
         
        txt_search=Entry(info_frame,font=("arial",12),bd=2,relief=GROOVE,textvariable=self.search_text)
        txt_search.grid(row=0,column=3,pady=10,padx=20,sticky="w")
        
        btn_search=Button(info_frame,text="Search",width=10,pady=5,bg="lightcyan2",command=self.search).grid(row=0,column=4,padx=10,pady=10)
        btn_show=Button(info_frame,text="Show All",width=10,pady=5,bg="lightcyan",command=self.table_data).grid(row=0,column=5,padx=10,pady=10)
  
        table_frame=Frame(info_frame,bd=4,relief=RIDGE, bg="white")
        table_frame.place(x=10,y=70,width=770,height=480)
        
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.emp_table=ttk.Treeview(table_frame,columns=("eid","name","dept","contact","dob","designation","jd","salary","email","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.emp_table.xview)
        scroll_y.config(command=self.emp_table.yview)
        self.emp_table.heading("eid",text="Emp Id")
        self.emp_table.heading("name",text="Name")
        self.emp_table.heading("dept",text="Department")
        self.emp_table.heading("contact",text="Contact")
        self.emp_table.heading("dob",text="DOB")
        self.emp_table.heading("designation",text="Designation")        
        self.emp_table.heading("jd",text="Join Date")
        self.emp_table.heading("salary",text="Salary")
        self.emp_table.heading("email",text="Email")
        self.emp_table.heading("address",text="Address")
        self.emp_table['show']='headings'
        self.emp_table.column("eid",width=50)
        self.emp_table.column("name",width=100)
        self.emp_table.column("dept",width=100)
        self.emp_table.column("contact",width=100)
        self.emp_table.column("dob",width=100)
        self.emp_table.column("designation",width=100)
        self.emp_table.column("jd",width=100)
        self.emp_table.column("salary",width=50)
        self.emp_table.column("email",width=100)

        self.emp_table.column("address",width=50)
        self.emp_table.pack(fill=BOTH,expand=1)
        self.emp_table.bind("<ButtonRelease-1>",self.get_cursor)
        
    def add_employee(self):
        name=self.name.get() 
        dept=self.dept.get() 
        contact=self.contact.get() 
        dob= self.dob.get() 
        desg=self.desg.get() 
        jd=self.jd.get() 
        sal=self.sal.get() 
        email=self.email.get()
        address=self.txt_add.get('1.0',END)

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
        elif self.email.get()=="":
             messagebox.showinfo("Alert","Enter Email")
        elif self.sal.get()=="":
             messagebox.showinfo("Alert","Enter Salary")
        else:
            cursor.execute("SELECT * FROM `employee` WHERE `contact` = %s", [self.contact.get()])
            if cursor.fetchone() is not None:
                messagebox.showinfo("Message","Employee Already Exists")
            else:
                res=cursor.execute("INSERT INTO `employee` (`name`, `department`, `contact`, `dob`, `designation`, `join_date`, `salary`, `email`, address) VALUES(%s, %s, %s,%s,%s, %s, %s, %s,%s)", (str(name), str(dept), str(contact), str(dob),str(desg), str(jd), str(sal), str(email), str(address) ))
                messagebox.showinfo("Message","Employee Added Succesfully")
                
                con.commit()
                self.table_data()
                self.reset()
            
    def update_employee(self):
        name=self.name.get() 
        dept=self.dept.get() 
        contact=self.contact.get() 
        dob= self.dob.get() 
        desg=self.desg.get() 
        jd=self.jd.get() 
        sal=self.sal.get() 
        email=self.email.get()
        address=self.txt_add.get('1.0',END)

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
        elif self.email.get()=="":
             messagebox.showinfo("Alert","Enter Email")
        elif self.sal.get()=="":
             messagebox.showinfo("Alert","Enter Salary")
        else:
            res=cursor.execute("UPDATE `employee` SET `name`=%s,`department`=%s,`dob`=%s,`designation`=%s,`join_date`=%s,`salary`=%s,`email`=%s,`address`=%s WHERE `contact`=%s", (str(name), str(dept),  str(dob),str(desg), str(jd), str(sal), str(email), str(address),str(contact) ))
            messagebox.showinfo("Message","Employee Updated Succesfully")
                
            con.commit()
            self.table_data()
            self.reset()
        
    def delete_employee(self):
      
        cursor.execute("DELETE FROM `employee` WHERE `contact` = %s",[self.contact.get()])
        messagebox.showinfo("Message","Employee Deleted Succesfully")
        self.table_data()
        self.reset()
            
                
    def table_data(self):
        cursor.execute("SELECT * FROM `employee`")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.emp_table.delete(*self.emp_table.get_children())
            for row in rows:
                self.emp_table.insert('',END,values=row)
            con.commit()
            
    def search(self):
        
        cursor.execute("select * from employee where " + str(self.search_by.get()) +" like '%"+str(self.search_text.get())+"%'")
        #cursor.execute("SELECT * FROM `employee` WHERE" +str(self.search_by.get())+"Like '%"+str(self.search_text.get())+"%'")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.emp_table.delete(*self.emp_table.get_children())
            for row in rows:
                self.emp_table.insert('',END,values=row)
            con.commit()
                
    def get_cursor(self,ev):
        cursor_row=self.emp_table.focus()
        contents=self.emp_table.item(cursor_row)
        row = contents['values']
        self.name.set(row[1])
        self.dept.set(row[2])
        self.contact.set(row[3])
        self.dob.set(row[4])
        self.desg.set(row[5])
        self.jd.set(row[6])
        self.sal.set(row[7])
        self.email.set(row[8])
        self.txt_add.delete('1.0',END)
        self.txt_add.insert(END,row[9])
        
               
    def reset(self):
        
        self.name.set("") 
        self.dept.set("") 
        self.contact.set("") 
        self.dob.set("") 
        self.desg.set("") 
        self.jd.set("") 
        self.sal.set("") 
        self.email.set("")
        self.txt_add.delete('1.0',END)
root=Tk()
obj=manage_employee(root)
root.mainloop()




