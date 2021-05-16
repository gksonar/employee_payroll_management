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
    
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll  System")
        self.root.geometry("1350x760+0+0")
        
        self.bg_icon=ImageTk.PhotoImage(file="images/Payrollfinal.jpg")
        self.employee_icon=ImageTk.PhotoImage(file="images/employee.png")
        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        
        title=Label(self.root,text="Employee Payroll System",font=("times new roman",30,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)        
        title.place(x=0,y=0,relwidth=1)
                
        view_frame=Frame(self.root,bg="white")
        view_frame.place(x=100,y=200)
        
        logolbl=Label(view_frame,text="",image=self.employee_icon,bd=0).grid(row=0,columnspan=2,pady=0)
        lbl_holiday=Label(view_frame,text="View Holiday",height=2,width=20,font=("arial",18,"bold"),bg="white",fg="red").grid(row=3,column=1,pady=0)


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






