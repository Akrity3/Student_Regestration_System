#######~ADMIN LOGIN~###########

from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
 
 
# Initialize the main window
root = CTk()
root.geometry('1920x1080+0+0')
root.title('Student Management System')
root.iconbitmap("logo.ico")
root._set_appearance_mode("light")
# root.config(bg='#FFFFFF')

adm_login_fr = CTkFrame(root,fg_color="#FFFFFF")
adm_login_fr.place(relwidth = 1, relheight = 1)


#to show password:
def show_pass():
    if adl_pw_entry.cget("show") == "*":
        adl_pw_entry.configure(show = '')
    else:
        adl_pw_entry.configure(show = '*')
            
#message box is shown after clicking login butto
def login_check():
  email=adl_email_entry.get()
  password=adl_pw_entry.get()
  #checking login credentials
  if email == "" or password*6 == "":
      messagebox.showerror("Error","Insufficient credentials")

  else:
      try: 
          conn = sqlite3.connect("sms.db")   # Connect to the database (create if not exists)
          c = conn.cursor()   

          # Fetch the record with the matching email and password
          c.execute("SELECT * FROM admin WHERE email = ? and password = ?", (adl_email_entry.get(), adl_pw_entry.get()))
          result = c.fetchone()
               
          # Check if a result was found
          if result is not None:
          # Assuming the email is in the 3rd column and the password in the 4th column 
           global a_email, a_password
           if adl_email_entry.get() == result[2] and adl_pw_entry.get() == result[3]:
                        u_email = adl_email_entry.get()
                        u_password = adl_pw_entry.get()
                        messagebox.showinfo("Successful Message", "Login Successful!")
                        # adm_login_fr.place_forget()
                        # admin_dashboard()     
           else:
               messagebox.showerror("Error", "Invalid email or password.")
          else:
             messagebox.showerror("Error", "Invalid email or password.")
      
      except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
      finally:
          conn.commit()   # Commit changes and close connection
          conn.close()
login_check()


#ad_log_fr1: for heading
adm_log_fr1 = Frame(adm_login_fr,bg='#FFFFFF', highlightbackground="#0F56A2", highlightthickness=2,width=2000, height=100,bd=0)
adm_log_fr1.place(x=0, y=0)

#ad_log_fr2:for picture
adm_log_fr2= CTkFrame(adm_login_fr,fg_color='#FFFFFF',corner_radius=0 ,width=504, height=500)
adm_log_fr2.place(x=127, y=140)


#ad_fr3: for labels 
adm_log_fr3= CTkFrame(adm_login_fr,fg_color='#1C5FA8',corner_radius=0 ,width=504, height=500)
adm_log_fr3.place(x=630, y=140)


#For Logo:
adm_bg_img = Image.open('G&A.png')
adm_bg_img = adm_bg_img.resize((110,90))   #adjusting the size of logo
adm_bg_img = ImageTk.PhotoImage(adm_bg_img)
label = Label(adm_login_fr, image=adm_bg_img,bg="#FFFFFF")
label.place(x=0, y=3,width=150,height=90)

#Contains in ad_log_fr1:
#heading:
adm_log_heading=Label(adm_log_fr1,text='THE GRACE ACADEMY',fg='#004367',bg='#FFFFFF' ,font=('Times New Roman',60))
adm_log_heading.place(x='510',y='18',width='950',height='60')

#quote:
adl_quote=Label(adm_login_fr,text='"A Legacy Of Grace, A Future Of Success"',fg='#2171B1',bg="#FFFFFF" ,font=('Brush Script MT',25,"italic"))
adl_quote.place(x=750,y=120) 

#Adding picture: In ad_log_fr2
adl_bg_img = Image.open("bg_login.png")
adl_bg_img=adl_bg_img.resize((754,750))
adl_bg_imgtk=ImageTk.PhotoImage(adl_bg_img)

label=Label(adm_log_fr2,image=adl_bg_imgtk)
label.place(relheight=1,relwidth=1)

#Adding labels: In adm_log_fr3
#labels:
ad_login_lbl1=CTkLabel(adm_log_fr3,text='  ADMIN LOGIN',bg_color="#1C5FA8",fg_color='#1C5FA8', font=("Times New Roman",35,"bold"))
ad_login_lbl1.place(x=120,y=10)

ad_login_lbl2=Label(adm_log_fr3,text='Email',fg='#000000',bg='#1C5FA8', font=("Times New Roman",19,"bold"))
ad_login_lbl2.place(x=125,y=110)

ad_login_lbl3=Label(adm_log_fr3,text='Password',fg='#000000',bg='#1C5FA8', font=("Times New Roman",19,"bold"))
ad_login_lbl3.place(x=125,y=270)

ad_login_lbl4=Label(adm_log_fr3,text='Don\'t have account?',fg='white',bg='#1C5FA8', font=("Regular",16,'italic'))
ad_login_lbl4.place(x=200,y=680)

#entry:
adl_email_entry= CTkEntry(adm_log_fr3,corner_radius=12,height=40,width=300,border_width=0,fg_color="white",text_color="black",placeholder_text="Email",placeholder_text_color="#0E304B") #for email
adl_email_entry.place(x=85,y=110)

adl_pw_entry= CTkEntry(adm_log_fr3,fg_color='white',corner_radius=12,height=40,width=300,border_width=0,text_color="black",placeholder_text="Password",placeholder_text_color="#0E304B",show="*") #for password
adl_pw_entry.place(x=85,y=215)

#checkbutton:
var = IntVar()
ad_login_c1 = Checkbutton(adm_log_fr3, text = 'Show Password',font=("Times New Roman",16),activebackground="#1C5FA8",variable = var,bg="#1C5FA8",  command = show_pass)
ad_login_c1.place(x=130,y=400)

#Button:
#forget password:
ad_fp_btn=CTkButton(adm_log_fr3,text="forgot password?",text_color="#FFFFFF",font=("Helvetica",17,"underline","italic"),fg_color="#1C5FA8",hover_color="#1C5FA8", corner_radius=19,command="reset_password") 
ad_fp_btn.place(x=290,y=320)


#Login Button:
adl_login_btn=CTkButton(adm_log_fr3,text="Login",font=("Times New Roman",25,"bold"),fg_color="#001437",hover_color="#062B6B",width=350,height=40,corner_radius=20,command=login_check) 
adl_login_btn.place(x=85,y=380)

#click Button:
adl_click_btn = CTkButton(adm_log_fr3,text="<Click Here>",font=("Times New Roman",19,"bold"),text_color="#001437",fg_color="#1C5FA8",hover_color="#",width=20,height=20) 
adl_click_btn.place(x=274,y=447)

#back to homepage button:
adl_back_btn = CTkButton(adm_login_fr,text="BACK",font=("Times New Roman",19),text_color="#001535",fg_color="#F1BC60",hover_color="#F5A417",width=75,height=25,corner_radius=7) #back to homepage 
adl_back_btn.place(x=1190,y=75)


root.mainloop()





