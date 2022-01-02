from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql                                      

class Login:
   def __init__(self,root):
      self.root=root
      self.root.title("Doctor appoitment booking")
      self.root.geometry("1366x700+0+0")
      self.root.resizable(False,False)
      self.loginform()
   def loginform(self):
      Frame_login=Frame(self.root,bg="sky blue")
      Frame_login.place(x=0,y=0,height=700,width=1366)      
      self.img=ImageTk.PhotoImage(file="vara.jpg")
      img=Label(Frame_login,image=self.img).place(x=220,y=10,width=1366,height=700)      
      frame_input=Frame(self.root,bg='white')
      frame_input.place(x=320,y=130,height=450,width=350)
      label1=Label(frame_input,text="For doctor appointment Login Here",font=('impact',16),
                   fg="green",bg='white')
      label1.place(x=17,y=30)
      label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),
                   fg='green',bg='white')
      label2.place(x=30,y=95)
      self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"),
                       bg='light grey')
      self.email_txt.place(x=30,y=145,width=270,height=35)      
      label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),
                   fg='green',bg='white')
      label3.place(x=30,y=195)
      self.password=Entry(frame_input,font=("times new roman",15,"bold"),
                        bg='lightgray')
      self.password.place(x=30,y=245,width=270,height=35)   
      btn1=Button(frame_input,text="forgot password?",cursor='hand2',
                  font=('calibri',10),bg='white',fg='black',bd=0)
      btn1.place(x=125,y=305)
      btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",
                  font=("times new roman",15),fg="blue",bg="grey",
                  bd=0,width=15,height=1)
      btn2.place(x=90,y=340)        
      btn3=Button(frame_input,command=self.Register,text="Not Registered?register"
                  ,cursor="hand2",font=("calibri",10),bg='white',fg="red",bd=0)
      btn3.place(x=110,y=390)                                                                    #login page
   def login(self):
      if self.email_txt.get()=="" or self.password.get()=="":
         messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
         try:
            con=pymysql.connect(host='localhost',user='root',password='varaprasad',
                                database='madicalbooking')
            cur=con.cursor()
            cur.execute('select * from register where emailid=%s and password=%s'
                        ,(self.email_txt.get(),self.password.get()))
            row=cur.fetchone()
            if row==None:
               messagebox.showerror('Error','Invalid Username And Password'
                                    ,parent=self.root)
               self.loginclear()
               self.email_txt.focus()
            else:
               self.appscreen()
               con.close()
         except Exception as es:
            messagebox.showerror('Error',f'Error Due to : {str(es)}'
                                 ,parent=self.root)                                                    #login page and shows the message box(pop-up)
   def Register(self):
      Frame_login1=Frame(self.root,bg="white")
      Frame_login1.place(x=0,y=0,height=700,width=1366)      
      self.img=ImageTk.PhotoImage(file="picture.jpg")
      img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=1366,height=700)      
      frame_input2=Frame(self.root,bg='white')
      frame_input2.place(x=320,y=130,height=450,width=630)
      label1=Label(frame_input2,text="Register Here",font=('impact',20,'bold'),
                   fg="black",bg='white')
      label1.place(x=45,y=20)
      label2=Label(frame_input2,text="Username",font=("Goudy old style",20,"bold"),
                   fg='black',bg='white')
      label2.place(x=30,y=95)
      self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),
                       bg='lightgray')
      self.entry.place(x=30,y=145,width=270,height=35)      
      label3=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"),
                   fg='black',bg='white')
      label3.place(x=30,y=195)
      self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),
                        bg='lightgray')
      self.entry2.place(x=30,y=245,width=270,height=35)
      label4=Label(frame_input2,text="Email-id",font=("Goudy old style",20,"bold"),
                   fg='black',bg='white')
      label4.place(x=330,y=95)
      self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),
                       bg='lightgray')
      self.entry3.place(x=330,y=145,width=270,height=35)
      label5=Label(frame_input2,text="Confirm Password",
                   font=("Goudy old style",20,"bold"),fg='black',bg='white')
      label5.place(x=330,y=195)
      self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),
                       bg='lightgray')
      self.entry4.place(x=330,y=245,width=270,height=35)
      btn2=Button(frame_input2,command=self.register,text="Register"
                  ,cursor="hand2",font=("times new roman",15),fg="white",
                  bg="orangered",bd=0,width=15,height=1)
      btn2.place(x=90,y=340)       
      btn3=Button(frame_input2,command=self.loginform,
                  text="Already Registered?Login",cursor="hand2",
                  font=("calibri",10),bg='white',fg="red",bd=0)
      btn3.place(x=110,y=390)                                                                                   #registeration page
   def register(self):
      if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":
         messagebox.showerror("Error","All Fields Are Required",parent=self.root)
      elif self.entry2.get()!=self.entry4.get():
         messagebox.showerror("Error","Password and Confirm Password Should Be Same"
                              ,parent=self.root)
      else:
         try:
            con=pymysql.connect(host="localhost",user="root",password="varaprasad",
                                database="madicalbooking")
            cur=con.cursor()
            cur.execute("select * from register where emailid=%s"
                        ,self.entry3.get())
            row=cur.fetchone()
            if row!=None:
               messagebox.showerror("Error"
               ,"User already Exist,Please try with another Email"
                                    ,parent=self.root)
               self.regclear()
               self.entry.focus()
            else:
               cur.execute("insert into register values(%s,%s,%s,%s)"
                           ,(self.entry.get(),self.entry3.get(),
                           self.entry2.get(),
                           self.entry4.get()))
               con.commit()
               con.close()
               messagebox.showinfo("Success","Register Succesfull"
                                   ,parent=self.root)
               self.regclear()
         except Exception as es:
            messagebox.showerror("Error",f"Error due to:{str(es)}"
                                 ,parent=self.root)
   def appscreen(self):
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=1366)      
      label1=Label(text="List of the Doctors",font=('impact',25),
                   fg="black",bg='white')
      label1.place(x=500,y=30)
      self.img=ImageTk.PhotoImage(file="aasish.jpg",)
      img=Label(image=self.img).place(x=10,y=100,width=250,height=300)
      label2=Label(Frame_login,text="Mr.Aasish"
                   ,font=('times new roman',25),
                   fg="black",bg='white')
      label2.place(x=345,y=100)
      label3=Label(Frame_login,text="Pschiatrists"
                   ,font=('times new roman',25),
                   fg="black",bg='white')
      label3.place(x=345,y=160)
      label4=Label(Frame_login,text="30 years experience in KGH hospital(vizag)"
                   ,font=('times new roman',25),
                   fg="black",bg='white')
      label4.place(x=345,y=220)
      label5=Label(Frame_login,text="(please select the doctor)"
                   ,font=('times new roman',10),
                   fg="grey",bg='white')
      label5.place(x=420,y=275)
      chk_state=BooleanVar()
      chk_state.set(True)
      chk=Checkbutton(text='select',var=chk_state)
      chk.place(x=350,y=275)
      label4=Label(Frame_login,text="Time slots:"
                   ,font=('times new roman',25),
                   fg="black",bg='white')
      label4.place(x=345,y=300)
      btn2=Button(Frame_login,text="Logout",command=self.loginform,cursor="hand2",
                  font=("times new roman",15),fg="red",bg="white",
                  bd=0,width=15,height=1)
      btn2.place(x=1220,y=10)
      rad1=Radiobutton(text="10am to 11am",font="green",fg="green",value=1)
      rad2=Radiobutton(text="11am to 12am",font="green",fg="green",value=2)
      rad3=Radiobutton(text="12am to 1pm",font="green",fg="green",value=3)
      rad4=Radiobutton(text="6pm to 7pm",font="green",fg="green",value=4)
      rad5=Radiobutton(text="7pm to 8pm",font="green",fg="green",value=5)
      rad6=Radiobutton(text="8pm to 9pm",font="green",fg="green",value=6)
      rad1.place(x=500,y=315)
      rad2.place(x=700,y=315)
      rad3.place(x=900,y=315)
      rad4.place(x=500,y=375)
      rad5.place(x=700,y=375)
      rad6.place(x=900,y=375)
      btn5=Button(text="submit",command=self.dialogue,cursor="hand2",
                  font=("times new roman",15),fg="red",bg="light grey",
                  bd=0,width=15,height=1)
      btn5.place(x=650,y=450)                                                         #application page

      
   def dialogue(self):
      chk_state=BooleanVar()
      chk_state.set(True)
      chk=Checkbutton(text='yes',var=chk_state,font="green",bg="white")
      chk.place(x=500,y=550)
      chk_state=BooleanVar()
      chk_state.set(True)
      chk=Checkbutton(text='no',var=chk_state,font="green",bg="white")
      chk.place(x=600,y=550)
      label5=Label(text="Are u sure?"
                   ,font=('times new roman',25),
                   fg="black",bg='white')
      label5.place(x=100,y=540)                                                        #appoitment status
      

   
   def regclear(self):
      self.entry.delete(0,END)
      self.entry2.delete(0,END)
      self.entry3.delete(0,END)
      self.entry4.delete(0,END)
   def loginclear(self):
      self.email_txt.delete(0,END)
      self.password.delete(0,END)
root=Tk()
ob=Login(root)
root.mainloop()                                           #end..............
