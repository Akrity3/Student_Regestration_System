######~~~~Admin_SignUp_Page~~~~~#######
 
from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


 
# Initialize the main window:
root = CTk()
root.geometry('1920x1080+0+0')
root.title('Student Management System')
root.iconbitmap("logo.ico")
root._set_appearance_mode("light")

adm_sign_fr = CTkFrame(root,fg_color="#FFFFFF")
adm_sign_fr.place(relwidth = 1, relheight = 1)


#to show password:
def show_pass():
    if pw_entry.cget("show") == "*":
        pw_entry.configure(show = '')
    else:
        pw_entry.configure(show = '*')

#to show confirm_pass:
def confirm_pass():
    if cnf_pw_entry.cget("show") == "*":
        cnf_pw_entry.configure(show = '')
    else:
        cnf_pw_entry.configure(show = '*')


#Frame for the header: Frame1
st_sign_fr1 = Frame(adm_sign_fr,bg='#FFFFFF', highlightbackground="#0F56A2", highlightthickness=2,width=2000, height=100)
st_sign_fr1.place(x=0, y=0)

# Frame for the sign-up form: Left Frame :Frame2
st_sign_fr2= CTkFrame(adm_sign_fr,fg_color='#1C5FA8',corner_radius=0 ,width=504, height=500)
st_sign_fr2.place(x=127, y=140)

#Image frame: Right Frame :Frame 3
st_sign_fr3= CTkFrame(adm_sign_fr,corner_radius=0 ,width=504, height=500)
st_sign_fr3.place(x=630, y=140)

#For Logo:
st_log_img = Image.open('G&A.png')
st_log_img = st_log_img.resize((110,90))   #adjusting the size of logo
st_log_img = ImageTk.PhotoImage(st_log_img)

st_sign_label = Label(st_sign_fr1, image=st_log_img,bg="#FFFFFF") 
st_sign_label.place(x=0, y=1,width=150,height=90)
 
 
# Adding picture in frame3:
st_sign_bg_img = Image.open('bg_signup.png')
st_sign_bg_img = st_sign_bg_img.resize((757, 750))
st_sign_bg_img = ImageTk.PhotoImage(st_sign_bg_img)
 
label=Label(st_sign_fr3,image=st_sign_bg_img)
label.place(relheight=1,relwidth=1) 
 
 
# Heading:
# Adding Label: In top frame
ads_heading=CTkLabel(st_sign_fr1,text='THE GRACE ACADEMY',text_color='#004367',fg_color='#FFFFFF' ,font=('Times New Roman',50,"bold"),width=600,height=30) #Heading
ads_heading.place(x=300,y=3)
 
quote = Label(adm_sign_fr, text='"A Legacy of Grace, A Future of Success."', fg='#2171B1', bg='#FFFFFF',font=('Brush Script MT',25,"italic")) #moto
quote.place(x=780, y=100)


#Adding Label: In left frame
main_lbl=CTkLabel(st_sign_fr2, text='    Admin SignUp', text_color='white', font=('Times New Roman', 40,"bold"))
main_lbl.place(x=90, y=6)

f_nm_lbl = CTkLabel(st_sign_fr2, text='First Name', text_color='black', font=('Times New Roman', 18,"bold"))
f_nm_lbl.place(x=38, y=90)
 
l_nm_lbl = CTkLabel(st_sign_fr2, text='Last Name', text_color='black', font=('Times New Roman', 18,"bold"))
l_nm_lbl.place(x=265, y=90)
 
email_lbl = CTkLabel(st_sign_fr2, text='Email', text_color='black', font=('Times New Roman', 18,"bold"))
email_lbl.place(x=38, y=160)
 
phn_n_lbl = CTkLabel(st_sign_fr2, text='Enter Your Phone Number', text_color='black', font=('Times New Roman', 18,"bold"))
phn_n_lbl.place(x=38, y=230)
 
pw_lbl = CTkLabel(st_sign_fr2, text='Create Password', text_color='black', font=('Times New Roman', 18,"bold"))
pw_lbl.place(x=38, y=300)
 
cnf_pw_lbl = CTkLabel(st_sign_fr2, text='Confirm Password', text_color='black', font=('Times New Roman', 18,"bold"))
cnf_pw_lbl.place(x=38, y=370)
 
# Entry box:
f_nm_entry = CTkEntry(st_sign_fr2, corner_radius=7, height=35, width=190, border_width=0, fg_color="white", text_color="black")
f_nm_entry.place(x=38, y=115)
 
l_nm_entry = CTkEntry(st_sign_fr2, corner_radius=7, height=35, width=190, border_width=0, fg_color="white", text_color="black")
l_nm_entry.place(x=265, y=115)
 
email_entry = CTkEntry(st_sign_fr2, corner_radius=7, height=35, width=420, border_width=0, fg_color="white", text_color="black")
email_entry.place(x=38, y=185)
 
phn_n_entry = CTkEntry(st_sign_fr2, corner_radius=7, height=35, width=420, border_width=0, fg_color="white", text_color="black")
phn_n_entry.place(x=38, y=255)
 
pw_entry = CTkEntry(st_sign_fr2, corner_radius=7, height=35, width=340, border_width=0, fg_color="white", text_color="black", show='*')  #showpassword
pw_entry.place(x=38, y=325)
 
cnf_pw_entry = CTkEntry(st_sign_fr2, corner_radius=7, height=35, width=340, border_width=0, fg_color="white", text_color="black", show='*') #showpassword
cnf_pw_entry.place(x=38, y=395)

#Buttons:
#CheckButton:

var = IntVar()
pw_c_btn = Checkbutton(st_sign_fr2, text = 'Show',font=("Times New Roman",18,"bold"),activebackground="#1C5FA8",variable = var,bg="#1C5FA8",  command = show_pass)  #for password
pw_c_btn.place(x=590,y=495)

varr = IntVar()
pw_c_btn = Checkbutton(st_sign_fr2, text = 'Show',font=("Times New Roman",18,"bold"),activebackground="#1C5FA8",variable = varr,bg="#1C5FA8",  command = confirm_pass) #for confirm password
pw_c_btn.place(x=590,y=595)

# Back To Login Button: 
ads_back_btn = CTkButton(st_sign_fr2,text="Back To LogIn",font=("Times New Roman",18,"bold"),text_color="white",bg_color="#1C5FA8",fg_color="#001437",width=200,height=40,corner_radius=16)
ads_back_btn.place(x=38,y=445)
 
#Signup Button:
ads_sign_btn = CTkButton(st_sign_fr2,text="SIGN UP",font=("Times New Roman",18,"bold"),text_color="white",bg_color="#1C5FA8",fg_color="#001437",corner_radius=16,width=200,height=40)
ads_sign_btn.place(x=270,y=445)


#back to homepage button:
st_back_btn = CTkButton(adm_sign_fr,text="BACK",font=("Times New Roman",19),text_color="#001535",fg_color="#F1BC60",hover_color="#F5A417",width=75,height=25,corner_radius=7) #back to homepage 
st_back_btn.place(x=1190,y=75)


  
# Keep the window open
root.mainloop()

 
 
 
 
 
 
 