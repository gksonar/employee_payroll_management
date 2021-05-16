import os
import sys
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
class manage_holiday:
    def disp_dashboard(self):
        root.destroy();
        root.destroy();
        os.system('python hr.py');
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll  System")
        self.root.geometry("1350x760+0+0")
        
        self.bg_icon=ImageTk.PhotoImage(file="images/Payrollfinal.jpg")
        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        
        title=Label(self.root,text="Employee Payroll System",font=("times new roman",30,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)        
        title.place(x=0,y=0,relwidth=1)
        
        manage_frame=Frame(self.root,bd=4,relief=RIDGE, bg="white")
        manage_frame.place(x=20,y=90,width=450,height=560)
        
        m_title=Label(manage_frame,text="Manage Holiday",height=2,width=20,font=("arial",18,"bold"),bg="white",fg="red")
        m_title.grid(row=0,columnspan=2,pady=10)
        
        self.hdate=StringVar()
        self.hid=StringVar()
        self.hdesc=StringVar()
        
        lbl_hid=Label(manage_frame,text="Holiday ID",font=("arial",14))
        lbl_hid.grid(row=1,column=0,pady=5,padx=10)        
        txt_hid=Entry(manage_frame,font=("arial",12),bd=5,relief=GROOVE,textvariable=self.hid)
        txt_hid.grid(row=1,column=1,pady=5,padx=20,sticky="w")        
               
        lbl_date=Label(manage_frame,text="Date",font=("arial",14))
        lbl_date.grid(row=2,column=0,pady=5,padx=10)        
        txt_date=Entry(manage_frame,font=("arial",12),bd=5,relief=GROOVE,textvariable=self.hdate)
        txt_date.grid(row=2,column=1,pady=5,padx=20,sticky="w") 
        
        self.lbl_desc=Label(manage_frame,text="Description",font=("arial",14))
        self.lbl_desc.grid(row=3,column=0,pady=10,padx=10,sticky="w")        
        self.txt_desc=Text(manage_frame,bd=2,width=23,height=4)
        self.txt_desc.grid(row=3,column=1,pady=10,padx=20)
        
        btn_frame=Frame(manage_frame,bd=4,relief=RIDGE, bg="White")
        btn_frame.place(x=9,y=490,width=430)
        
        add_btn=Button(btn_frame,text="Add",width=8,bg="skyblue",font=("arial",10,"bold"),command=self.add_holiday).grid(row=0,column=0,padx=10,pady=10)
        update_btn=Button(btn_frame,text="Update",width=10,bg="green",font=("arial",10,"bold"),command=self.update_holiday).grid(row=0,column=1,padx=10,pady=10)
        delete_btn=Button(btn_frame,text="Delete",width=10,bg="red",font=("arial",10,"bold"),command=self.delete_holiday).grid(row=0,column=2,padx=10,pady=10)
        clear_btn=Button(btn_frame,text="Clear",width=10,bg="lightgray",font=("arial",10,"bold"),command=self.reset).grid(row=0,column=3,padx=10,pady=10)
  
        detail_frame=Frame(self.root,bd=4,relief=RIDGE, bg="white")
        detail_frame.place(x=500,y=90,width=800,height=560)
        
        lbl_search=Label(detail_frame,text="Search By",font=("arial",14))
        lbl_search.grid(row=0,column=0,pady=10,padx=10,sticky="w")
        
        self.search_by=ttk.Combobox(detail_frame,width=10,font=("arial",14),state="readonly")
        self.search_by['values']=('hid','hdate','hdescription')
        self.search_by.grid(row=0,column=1,pady=10,padx=10,sticky="w")
         
        self.search_text=Entry(detail_frame,font=("arial",12),bd=5,relief=GROOVE)
        self.search_text.grid(row=0,column=3,pady=10,padx=20,sticky="w")
        
        btn_search=Button(detail_frame,text="Search",width=10,pady=5,bg="lightcyan2",command=self.search).grid(row=0,column=4,padx=10,pady=10)
        btn_show=Button(detail_frame,text="Show All",width=10,pady=5,bg="lightcyan",command=self.table_data).grid(row=0,column=5,padx=10,pady=10)
  
        table_frame=Frame(detail_frame,bd=4,relief=RIDGE, bg="white")
        table_frame.place(x=10,y=70,width=770,height=480)
        
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.holiday_table=ttk.Treeview(table_frame,columns=("hid","hdate","hdescription"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.holiday_table.xview)
        scroll_y.config(command=self.holiday_table.yview)
        self.holiday_table.heading("hid",text="Sr No ")
        self.holiday_table.heading("hdate",text="Date")
        self.holiday_table.heading("hdescription",text="Description")
        self.holiday_table['show']='headings'
        self.holiday_table.column("hid",width=50)
        self.holiday_table.column("hdate",width=50)
        self.holiday_table.column("hdescription",width=350)            
        self.holiday_table.pack(fill=BOTH,expand=1)
        self.holiday_table.bind("<ButtonRelease-1>",self.get_cursor)
               
    def add_holiday(self):
        hdate=self.hdate.get() 
        hid=self.hid.get() 
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
                res=cursor.execute("INSERT INTO `holiday` (`hid`,`hdate`, `hdescription`) VALUES(%s, %s)",(str(hid),str(hdate), str(desc)))
                messagebox.showinfo("Message","Holiday Added Succesfully")
                
                con.commit()                
                self.reset()
                
                
    def update_holiday(self):
        hdate=self.hdate.get() 
        hid=self.hid.get() 
        desc=self.txt_desc.get('1.0',END)

        if self.hdate.get()=="":
             messagebox.showinfo("Alert","Enter Date")
        elif self.txt_desc.get('1.0',END)=="":
             messagebox.showinfo("Alert","Enter Description")
        else:

            res=cursor.execute("UPDATE `holiday` SET `hdate`=%s,`hdescription`=%s WHERE `hid`=%s", (str(hdate), str(desc), str(hid)))
            messagebox.showinfo("Message","Holiday Updated Succesfully")
                
            con.commit()
            self.table_data()
            self.reset()
        
    def delete_holiday(self):
      
        cursor.execute("DELETE FROM `holiday` WHERE `hid` = %s",[self.hid.get()])
        messagebox.showinfo("Message","Holiday Deleted Succesfully")
        self.table_data()
        self.reset()
            
    def search(self):
        
        cursor.execute("select * from holiday where " + str(self.search_by.get()) +" like '%"+str(self.search_text.get())+"%'")
        #cursor.execute("SELECT * FROM `employee` WHERE" +str(self.search_by.get())+"Like '%"+str(self.search_text.get())+"%'")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.holiday_table.delete(*self.holiday_table.get_children())
            for row in rows:
                self.holiday_table.insert('',END,values=row)
            con.commit()
                
    def table_data(self):
        cursor.execute("SELECT * FROM `holiday`")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.holiday_table.delete(*self.holiday_table.get_children())
            for row in rows:
                self.holiday_table.insert('',END,values=row)
            con.commit()
            
    def reset(self):
        self.hid.set("")
        self.hdate.set("") 
        self.txt_desc.delete('1.0',END)
        
    def get_cursor(self,ev):
        cursor_row=self.holiday_table.focus()
        contents=self.holiday_table.item(cursor_row)
        row = contents['values']
        self.hid.set(row[0])
        self.hdate.set(row[1])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[2])      
    
root=Tk()
obj=manage_holiday(root)
root.mainloop()





