"""STUDENT LOGIN PAGE"""

from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


 
# Initialize the main window:
root = CTk()
root.geometry('1920x1080+0+0')
root.title('Student Management System')
root.iconbitmap("logo.ico")
root.config(bg='#FFFFFF')
root._set_appearance_mode("light")

#Main frame:
stu_login_fr = CTkFrame(root,fg_color="#FFFFFF")
stu_login_fr.place(relwidth = 1, relheight = 1)


#To hide or show password:
def show_pass():
    if password_entry.cget("show") == "*":
        password_entry.configure(show = '')
    else:
        password_entry.configure(show = '*')
        
        
#To check login credentials:
def login_check():
    email = email_entry.get()
    password = password_entry.get()
    
   
    # Sample check for credentials (you can replace it with actual logic)
    if email == "example@gmail.com" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome to The Grace Academy!")
    else:
        messagebox.showerror("Login Error", "Insufficient credentials")    


#Frame1:for heading
st_log_fr1 = Frame(stu_login_fr,bg='#FFFFFF', highlightbackground="#0F56A2", highlightthickness=2,width=2000, height=100,bd=0)
st_log_fr1.place(x=0, y=0)

#Frame2:for picture
st_log_fr2= CTkFrame(stu_login_fr,fg_color='#FFFFFF',corner_radius=0 ,width=504, height=500)
st_log_fr2.place(x=127, y=140)


#Frame3: for labels 
st_log_fr3= CTkFrame(stu_login_fr,fg_color='#1C5FA8',corner_radius=0 ,width=504, height=500)
st_log_fr3.place(x=630, y=140)

#For Logo:
st_log_img = Image.open('G&A.png')
st_log_img = st_log_img.resize((110,90))   #adjusting the size of logo
st_log_img = ImageTk.PhotoImage(st_log_img)
label = Label(stu_login_fr, image=st_log_img,bg="#FFFFFF")
label.place(x=0, y=3,width=150,height=90)
label.image=st_log_img


#Contains in Frame1:
#heading:
heading=Label(st_log_fr1,text='THE GRACE ACADEMY',fg='#004367',bg='#FFFFFF' ,font=('Times New Roman',60))
heading.place(x='500',y='18',width='950',height='60')

#quote:
moto=Label(stu_login_fr,text='"A Legacy Of Grace, A Future Of Success"',fg='#2171B1',bg="#FFFFFF" ,font=('Brush Script MT',25,"italic"))
moto.place(x=750,y=120) 

#Adding picture: In frame2
bg_image = Image.open("bg_login.png")
bg_image=bg_image.resize((754,750))
bg_imagetk=ImageTk.PhotoImage(bg_image)

label=Label(st_log_fr2,image=bg_imagetk)
label.place(relheight=1,relwidth=1)

#Adding labels: In st_log_fr3
#Labels:
login=CTkLabel(st_log_fr3,text='STUDENT LOGIN',bg_color="#1C5FA8",fg_color='#1C5FA8', font=("Times New Roman",35,"bold"))
login.place(x=120,y=10)

email=Label(st_log_fr3,text='Email',fg='#000000',bg='#1C5FA8', font=("Times New Roman",19,"bold"))
email.place(x=125,y=110)

pw=Label(st_log_fr3,text='Password',fg='#000000',bg='#1C5FA8', font=("Times New Roman",19,"bold"))
pw.place(x=125,y=270)

acc=Label(st_log_fr3,text='Don\'t have account?',fg='white',bg='#1C5FA8', font=("Regular",16,'italic'))
acc.place(x=200,y=680)

#Entry:
email_entry= CTkEntry(st_log_fr3,corner_radius=12,height=40,width=300,border_width=0,fg_color="white",text_color="black",placeholder_text="Email",placeholder_text_color="#0E304B") #for email
email_entry.place(x=85,y=110)

password_entry= CTkEntry(st_log_fr3,fg_color='white',corner_radius=12,height=40,width=300,border_width=0,text_color="black",placeholder_text="Password",placeholder_text_color="#0E304B",show="*") #for password
password_entry.place(x=85,y=215)

#Checkbutton:
var = IntVar()
c1 = Checkbutton(st_log_fr3, text = 'Show Password',font=("Times New Roman",16),activebackground="#1C5FA8",variable = var,bg="#1C5FA8",  command = show_pass)
c1.place(x=130,y=400)

#Button:
#Forget password:
fp_btn=CTkButton(st_log_fr3,text="forgot password?",text_color="#FFFFFF",font=("Helvetica",17,"underline","italic"),fg_color="#1C5FA8",hover_color="#1C5FA8", corner_radius=19) #opens reset password page
fp_btn.place(x=290,y=320)

#Login Button:
login_btn=CTkButton(st_log_fr3,text="Login",font=("Times New Roman",25,"bold"),fg_color="#001437",hover_color="#062B6B",width=350,height=40,corner_radius=20,command=login_check) #admin dashboard
login_btn.place(x=85,y=380)

#Click Button:
click_btn = CTkButton(st_log_fr3,text="<Click Here>",font=("Times New Roman",19,"bold"),text_color="#001437",fg_color="#1C5FA8",hover=0,width=20,height=20) #opens signup page
click_btn.place(x=274,y=447)

#Back to homepage button:
st_back_btn = CTkButton(stu_login_fr,text="BACK",font=("Times New Roman",19),text_color="#001535",fg_color="#F1BC60",hover_color="#F5A417",width=75,height=25,corner_radius=7) #back to homepage 
st_back_btn.place(x=1190,y=75)


root.mainloop()





