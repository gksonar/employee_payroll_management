import os
import sys
from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk

class login_system:
    def disp_sc(self):
        os.system('python edit_data.py');
    def disp_view(self):
        os.system('python view_holidays.py')
    def disp_gen(self):
        os.system('python generate_payslip.py')
    def disp_apply(self):
        os.system('python apply_leave.py');
    def __init__(self,root):
        self.root=root
        self.root.title("Shop System")
        self.root.geometry("1350x768+0+0")
        
        self.bg_icon=ImageTk.PhotoImage(file="images/Payrollfinal.jpg")   
        self.employee_icon=ImageTk.PhotoImage(file="images/employee.png")
        self.hr_icon=ImageTk.PhotoImage(file="images/hr1.png")
        
        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        title=Label(self.root,text="Employee Payroll System",font=("arial",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        
        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=550,y=100)      
        btn_log=Label(Login_Frame,text="Employee",height=2,width=20,font=("arial",18,"bold"),bg="white",fg="red").grid(row=3,column=0,pady=0)


        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=560,y=250)      
        btn_log=Button(Login_Frame,text="Edit Data",command=self.disp_sc,height=2,width=20,font=("arial",16,"bold"),bg="yellow",fg="red").grid(row=3,column=0,pady=0)
        
        
        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=560,y=400)      
        btn_log=Button(Login_Frame,text="View Holidays",command=self.disp_view,height=2,width=20,font=("arial",16,"bold"),bg="yellow",fg="red").grid(row=3,column=0,pady=0)
        
        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=560,y=550)
        btn_log1=Button(Login_Frame,text="Generate Payslip",command=self.disp_gen,height=2,width=20,font=("arial",16,"bold"),bg="yellow",fg="red").grid(row=3,column=0,pady=0)

        
           
    def login(self):
#         with sqlite3.connect("abc.db")as db :
#             cursur=db.cursor()
#         find_user=("select * from user where username=? AND password=?")
#         cursur.execute(find_user,[(self.uname.get()),(self.upass.get())])
#         result=cursur.fetchall()
#         if result:
#             messagebox.showinfo("Sucessfull",f"welcome {self.uname.get()}")
#         else:
#              messagebox.showerror("Error","Invalid Username and Password")
        if(self.uname.get()=="" or self.upass.get()==""):
            messagebox.showerror("Error", "All fields are Empty!!")
        elif (self.uname.get()=="shop" and self.upass.get()=="1234"):
            messagebox.showinfo("Sucessfull",f"welcome {self.uname.get()}")
            self.abc()
        else:
            messagebox.showerror("Error","Invalid Username and Password")
    def reset_values(self):
        self.uname.set("")
        self.upass.set("")  
root=Tk()
obj=login_system(root)
root.mainloop()
