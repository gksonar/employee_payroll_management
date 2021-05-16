import sys
import os
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
class login_system:
    def show_ui(self):
        root.destroy();
        os.system('python employee.py');
        
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
        
        logolbl=Label(Login_Frame,text="Employee Login",font=("ARIAL",20,"bold"),bd=0,bg="white",fg="Blue").grid(row=0,columnspan=2,pady=20)
        
        lbleid=Label(Login_Frame,text="Employee id",compound=LEFT,font=("times new roman",20,"bold")).grid(row=1,column=0,padx=20,pady=10)
        txteid=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)
        
        lblcontact=Label(Login_Frame,text="Contact No",compound=LEFT,font=("times new roman",20,"bold")).grid(row=2,column=0,padx=20,pady=10)
        txtcontact=Entry(Login_Frame,bd=5, show="*",textvariable=self.upass,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)
        
        btn_emp_log=Button(Login_Frame,text="Login", command=self.login,width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=20)
        reset = Button(Login_Frame,text = "Reset", command =self.reset_values,width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=0,padx=10,pady=20)
         
    
    def login(self):
        uname=self.uname.get();
        upass=self.upass.get();
        cursor.execute("SELECT * FROM Employee WHERE eid=%s AND  contact = %s", [uname,upass]);
        if(self.uname.get()=="" or self.upass.get()==""):
            messagebox.showerror("Error", "All fields are Empty!!")
        elif cursor.fetchone() is not None:
            messagebox.showinfo("Sucessfull Login",f"Successfull !!! Welcome ")
            self.show_ui();
            
        else:
            messagebox.showerror("Error","Invalid Username or Password")
    def reset_values(self):
        self.uname.set("")
        self.upass.set("")
    def checkUser(self):
        print(cursor.fetchone());
   
     
        
root=Tk()
obj=login_system(root)
root.mainloop()
