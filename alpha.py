from tkinter import *
from pymysql import *
from beta import *
from gamma import *
from tkinter import messagebox as msg

class Company(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.lblusername=Label(self,text='Username')
        self.lblpassword=Label(self,text='Password')
        
        self.txtusername=Entry(self)
        self.txtpassword=Entry(self,show='*')
        
        
        self.btnlogin=Button(self,text='Login',command=self.checkLogin)
        
        
        self.lblusername.grid(row=0,column=0)
        self.lblpassword.grid(row=1,column=0)
        self.txtusername.grid(row=0,column=1)
        self.txtpassword.grid(row=1,column=1)
        self.btnlogin.grid(columnspan=2)
        
        self.rowconfigure(0,pad=15)
        self.rowconfigure(1,pad=15)
        self.rowconfigure(2,pad=15)
        
        
        self.columnconfigure(0,pad=20)
        self.columnconfigure(1,pad=20)
        
        self.pack()
        
    def clear(self):
        self.txtusername.delete(0,'end')
        self.txtpassword.delete(0,'end')
        self.txtusername.focus()    
        
    def checkLogin(self):
        uid=self.txtusername.get()
        pwd=self.txtpassword.get()
        con=connect(db='ems',user='root',passwd='Sanjubaba@123',host='localhost')
        cur=con.cursor()
        try:
            cur.execute("select usertype from login where username='%s' and password='%s'"%(uid,pwd))
            rs=cur.fetchall()
            if rs[0][0]=='admin':
                    self.clear()
                    root1=Tk()
                    obj1=Admin(root1)
                    root1.geometry('350x350')
                    root1.title('Admin Login')
                    root1.mainloop()
            if rs[0][0]=='user':
                self.clear()
                root2=Tk()
                obj=EmployeeLogin(root2)
                root2.geometry('350x350')
                root2.title('Employee Login')
                root2.mainloop()
            
        except:
            self.clear()
            msg.showerror('error box','either username or password incorrect')
            
                       
root=Tk()
obj=Company(root)
root.geometry('350x350')
root.title('Company')
root.mainloop()

        