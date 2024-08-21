
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Main Page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
from customtkinter import CTkImage

# Initialize the main window
root = CTk()
root.geometry('1920x1080+0+0')
root.title('Student Regestration System')
root.iconbitmap("logo.ico")

#getting screen size and with:
x=root.winfo_screenwidth()
y=root.winfo_screenheight()



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Admin_Signup~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
   Function for Admin signup frame 
   
    """
def admin_signup():

    global st_log_img, st_sign_bg_img,email_entry,phn_n_entry,pw_entry,f_nm_entry,l_nm_entry
    #Admin Signup Frame:
    adm_sign_fr = CTkFrame(root,fg_color="#FFFFFF")
    adm_sign_fr.place(relwidth = 1, relheight = 1)

    def back_hompg():  #function to open homepage when back button is clicked
        adm_sign_fr.place_forget()
        main()
        pass

    def adm_signup():   #Function to open security page after sigining up
        conn = sqlite3.connect('sms.db')   #creating database
        c = conn.cursor()  #'cursor()' for executing the queries
        c.execute("""
                CREATE TABLE IF NOT EXISTS admin (
                    first_name TEXT,
                    last_name TEXT,
                    email TEXT,
                    phone_number INT,
                    password TEXT,
                    sec_ans1 TEXT,
                    sec_ans2 TEXT                
                )
                """)
        conn.commit()
        
        global adm_emails
        c.execute("SELECT email FROM admin")
        adm_emails = c.fetchall()
        a=[]
        for email in adm_emails:
        #saving the changes made in the database
         a.append(email[0])
        conn.commit()

        #checking if the entry boxes are filled and entered the valid credentials
        if f_nm_entry.get() == '' or l_nm_entry.get() == '' or email_entry.get() == '' or phn_n_entry.get() == '' or pw_entry.get() == '' or f_nm_entry.get() == 'firstname' or l_nm_entry.get() == 'lastname' or email_entry  .get() == 'example@gmail.com':
                messagebox.showerror("Error", "Please fill all the required fields!")
        elif (f_nm_entry.get()).isalpha() == False or (l_nm_entry.get()).isalpha() == False:
            messagebox.showerror("Error", "Please enter valid first and last names!")    #show error for first and last names
        elif '@gmail.com.admin' not in email_entry.get() or len(email_entry.get()) <= 10 or ' ' in email_entry.get():
                messagebox.showerror("Error", "Please enter a valid email address!")     #show error for email entry
        elif len(phn_n_entry.get())!= 10 or phn_n_entry.get().isdigit()==False:
                messagebox.showerror("Error", "Please enter valid phone number!")       #show error for phone entry
        elif pw_entry.get() != cnf_pw_entry.get():     #Checking if password is same in password and confirm password entry
                messagebox.showerror("Error", "Passwords do not match!")
        elif len(pw_entry.get()) < 8 :
                messagebox.showerror("Error", "Password should be at least 8 characters long!")
        
        else:
                if email_entry.get() in a:
                    #show error
                    messagebox.showerror("Error", "Email already exists!")
                else:
                    messagebox.showinfo("Sucessful sign up!"," Now you need to fill the security questions for future security,incase you forget your password by filling the questions . ")
                    adm_sign_fr.place_forget()
                    Security_page()  
        conn.close()            



    
    def show_pass():
        """
            function to show and hide password
            """
            
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
    #First Name
    f_nm_entry = CTkEntry(st_sign_fr2, corner_radius=7, height=35, width=190, border_width=0, fg_color="white", text_color="black",placeholder_text="firstname")
    f_nm_entry.place(x=38, y=115)
    
    #Last Name
    l_nm_entry = CTkEntry(st_sign_fr2, corner_radius=7, height=35, width=190, border_width=0, fg_color="white", text_color="black",placeholder_text="lastname")
    l_nm_entry.place(x=265, y=115)
    
    #Email
    email_entry = CTkEntry(st_sign_fr2, corner_radius=7, height=35, width=420, border_width=0, fg_color="white", text_color="black",placeholder_text="example@gmail.com.admin")
    email_entry.place(x=38, y=185)
    
    #Phone Number
    phn_n_entry = CTkEntry(st_sign_fr2, corner_radius=7, height=35, width=420, border_width=0, fg_color="white", text_color="black",placeholder_text="phone number")
    phn_n_entry.place(x=38, y=255)
    
    #Password
    pw_entry = CTkEntry(st_sign_fr2, corner_radius=7, height=35, width=340, border_width=0, fg_color="white", text_color="black", show='*')  #showpassword
    pw_entry.place(x=38, y=325)
    
    #Confirm Password
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

    
    #Signup Button:
    ads_sign_btn = CTkButton(st_sign_fr2,text="SIGN UP",font=("Times New Roman",18,"bold"),text_color="white",bg_color="#1C5FA8",fg_color="#001437",corner_radius=16,width=200,height=40,command=adm_signup)
    ads_sign_btn.place(x=150,y=445)


    #back to homepage button:
    st_back_btn = CTkButton(adm_sign_fr,text="BACK",font=("Times New Roman",19),text_color="#001535",fg_color="#F1BC60",hover_color="#F5A417",width=75,height=25,corner_radius=7,command=back_hompg) #back to homepage 
    st_back_btn.place(x=1190,y=75)

  
pass







#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Admin_LogIn~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def admin_login():
    """" ADMIN LOGIN """
    
    global adm_bg_img,adl_bg_img,adl_email_entry
    
    adm_login_fr = CTkFrame(root,fg_color="#FFFFFF")
    adm_login_fr.place(relwidth = 1, relheight = 1)

    def reset_password():
        adm_login_fr.place_forget()
        reset_pw_page()
        
        
    
    
    #to open homepage when back button is clicked
    def adl_back():
        adm_login_fr.place_forget()
        main()

    #to show password:
    def show_pass():
        if adl_pw_entry.cget("show") == "*":
            adl_pw_entry.configure(show = '')
        else:
            adl_pw_entry.configure(show = '*')
            
            
    #to check login credentials:
    def login_check():
        email = adl_email_entry.get()
        password = adl_pw_entry.get()##################################################################################################################################3
        conn=sqlite3.connect("sms.db")
        c=conn.cursor()
        c.execute("SELECT password FROM admin WHERE email=? ",[email])
        admin=c.fetchone()
    
        # Sample check for credentials (you can replace it with actual logic)
        if email != "" or password ==  "":
          if password == admin[0]:
             messagebox.showinfo("Login Successful", "Welcome to The Grace Academy!")
             adm_login_fr.place_forget()
             admin_dashboard()
          else:
            messagebox.showerror("Login Error", "Enter valid email or password.")   
        else:
            messagebox.showerror("Login Error", "Enter all field")    
              

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
    adm_bg_img= ImageTk.PhotoImage(adm_bg_img)
    adm_logo_lbl = Label(adm_login_fr, image=adm_bg_img,bg="#FFFFFF")
    adm_logo_lbl.image=adm_logo_lbl
    adm_logo_lbl.place(x=0, y=3,width=150,height=90)

    #Adding picture: In ad_log_fr2
    adl_bg_img = Image.open('bg_signup.png')
    adl_bg_img = adl_bg_img.resize((757, 750))
    adl_bg_img = ImageTk.PhotoImage(adl_bg_img)
    
    stl_bg_img_lbl=Label(adm_log_fr2,image=adl_bg_img)
    stl_bg_img_lbl.image=adl_bg_img
    stl_bg_img_lbl.place(relheight=1,relwidth=1)
    

    #Contains in ad_log_fr1:
    #heading:
    adm_log_heading=Label(adm_log_fr1,text='THE GRACE ACADEMY',fg='#004367',bg='#FFFFFF' ,font=('Times New Roman',60))
    adm_log_heading.place(x='510',y='18',width='950',height='60')

    #quote:
    adl_quote=Label(adm_login_fr,text='"A Legacy Of Grace, A Future Of Success"',fg='#2171B1',bg="#FFFFFF" ,font=('Brush Script MT',25,"italic"))
    adl_quote.place(x=750,y=120) 
   
    
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

    #Don't Have Label:
    adl_click_lbl = CTkLabel(adm_log_fr3,text='Go to signup page ',text_color="#FFFFFF",fg_color='#1C5FA8', font=("Times New Roman",19,"italic"))
    adl_click_lbl.place(x=279,y=447)
    
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
    ad_fp_btn=CTkButton(adm_log_fr3,text="forgot password?",text_color="#FFFFFF",font=("Helvetica",17,"underline","italic"),fg_color="#1C5FA8",hover_color="#1C5FA8", corner_radius=19,command=reset_password) 
    ad_fp_btn.place(x=290,y=320)


    #Login Button:
    adl_login_btn=CTkButton(adm_log_fr3,text="Login",font=("Times New Roman",25,"bold"),fg_color="#001437",hover_color="#062B6B",width=350,height=40,corner_radius=20,command=login_check) 
    adl_login_btn.place(x=85,y=380)


    #back to homepage button:
    adl_back_btn = CTkButton(adm_login_fr,text="BACK",font=("Times New Roman",19),text_color="#001535",fg_color="#F1BC60",hover_color="#F5A417",width=75,height=25,corner_radius=7,command=adl_back) #back to homepage 
    adl_back_btn.place(x=1190,y=75)
    
    pass
    
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Security_Page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Security_page():
    """
       Function to create a security page
       """
    
    global security_pg_bg,security_pg_entry1,security_pg_entry2
    
    security_pg_frm=CTkFrame(root,fg_color="#FFFFFF")
    security_pg_frm.place(relwidth = 1, relheight = 1)


    def sec_ans_check():
        #this function is made to show a message when user clicks submit on the security question page
 
        #checking if the entry is filled or not

        if security_pg_entry1.get() == '' or security_pg_entry2.get() == '':

           messagebox.showerror("Error", "Please fill all the required fields!")

        elif security_pg_entry1.get().isalpha() == False:

            messagebox.showerror("Error", "Please enter a word in both fileds!")

        else:
 
           #inserting security answers to the database

            conn = sqlite3.connect("sms.db")

            c = conn.cursor()

            #updating security questions

            #inserting data into the database

            c.execute('''INSERT INTO admin(first_name,last_name,email,phone_number,password,sec_ans1,sec_ans2) VALUES (?,?,?,?,?,?,?)''',
                    ((f_nm_entry.get(),l_nm_entry.get(),email_entry.get(),phn_n_entry.get(),pw_entry.get(),security_pg_entry1.get(), security_pg_entry2.get())
                )
                    )

            conn.commit()
            conn.close()

            security_pg_frm.place_forget()  
            admin_login()       

            messagebox.showinfo("Successful Message ","Security questions Entry Successful !")

    pass

    #importing image:
    security_pg_bg = Image.open("Security_page_bg.png")
    security_pg_bg=security_pg_bg.resize((1920,1060))
    security_pg_bgtk=ImageTk.PhotoImage(security_pg_bg)
    label=Label(security_pg_frm,width=x,height=y,image=security_pg_bgtk)
    label.image = security_pg_bgtk
    label.place(relheight=1,relwidth=1)

    #Frame for labels:
    security_pg_label_fr=CTkFrame(security_pg_frm,fg_color="#000D18",bg_color="#000D18",height=360,width=430)
    security_pg_label_fr.place(x=670, y=150)

    #Heading:
    security_pg_label1=CTkLabel(security_pg_label_fr,text='  Security Questions',font=("Times New Roman",45,"bold"),text_color="#FFFFFF")
    security_pg_label1.place(x=20, y=10)

    #Label for question no. 1
    security_pg_label2=CTkLabel(security_pg_label_fr,text='1.What is your favourite colour?',font=("Times New Roman",20),text_color="#FFFFFF")
    security_pg_label2.place(x=70, y=90)

    #label for question no. 2
    security_pg_label3=CTkLabel(security_pg_label_fr,text='2. What kind of music do you like?',font=("Times New Roman",20),text_color="#FFFFFF")
    security_pg_label3.place(x=70, y=190)

    #Entry for question no. 1
    security_pg_entry1=CTkEntry(security_pg_label_fr,corner_radius=12,height=38,width=300,border_width=0,fg_color="white",text_color="black")
    security_pg_entry1.place(x=70, y=130)

    #Entry for question no. 2
    security_pg_entry2=CTkEntry(security_pg_label_fr,corner_radius=12,height=38,width=300,border_width=0,fg_color="white",text_color="black")
    security_pg_entry2.place(x=70, y=230)


    #Submit Button

    security_pg_btn=CTkButton(security_pg_label_fr,hover_color="#002234",fg_color="#004367",text="Submit",font=("Times New Roman",20,"bold"),bg_color="#000D18",width=100,height=30,corner_radius=10,command=sec_ans_check)
    security_pg_btn.place(x=170, y=300)
    
    
    
    
    
    Security_page()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Reset_Password~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def reset_pw_page():
    """
    Function to create a forget password page
    """
 
    global  reset_pw_bg_img 
    reset_pw_pg_frm=CTkFrame(root,fg_color="#FFFFFF")
    reset_pw_pg_frm.place(relwidth = 1, relheight = 1)


    #importing image:
    reset_pw_bg_img = Image.open("Security_page_bg.png")
    reset_pw_bg_img=reset_pw_bg_img.resize((1920,1060))
    reset_pw_bg_imgtk=ImageTk.PhotoImage(reset_pw_bg_img)
    label=Label(reset_pw_pg_frm,width=x,height=y,image=reset_pw_bg_imgtk)
    label.image = reset_pw_bg_imgtk
    label.place(relheight=1,relwidth=1)

        
      
    """this function opens the reset password page when called."""  
    def to_login():
       #fetch user data from user table
      conn = sqlite3.connect("sms.db")
      c = conn.cursor()
      c.execute("SELECT * FROM admin WHERE email = ?", (adl_email_entry.get(),))
      admin = c.fetchone()
        
      if reset_pw_pg_entry1.get() == '' or reset_pw_pg_entry2.get() == '' or reset_pw_pg_entry3.get() == '' or reset_pw_pg_entry4.get() == '':
            messagebox.showerror("Error","All fields are required.")
      elif (reset_pw_pg_entry1.get() or reset_pw_pg_entry2.get()).isalpha() == False:
            messagebox.showerror("Error","Entered a correct values in ENtry 1 and 2.")
      elif len(reset_pw_pg_entry4.get()) <= 8 or ' ' in reset_pw_pg_entry4.get():  # Conditions for new password
            messagebox.showerror("Error", "Please enter a valid email address!") 
      if reset_pw_pg_entry1.get() == admin[5] and reset_pw_pg_entry2.get() == admin[6] and reset_pw_pg_entry3.get() == admin[2]:
            
        
        
        
        
        
        
          reset_pw_pg_frm.place_forget()
          admin_login()



    pass

    #to show or hide password:
    def new_pass():
        if reset_pw_pg_entry4.cget("show") == "*":
            reset_pw_pg_entry4.configure(show = '')
        else:
            reset_pw_pg_entry4.configure(show = '*')


    #Frame for labels:
    reset_pw_pg_fr=CTkFrame(reset_pw_pg_frm,fg_color="#000D18",bg_color="#000D18",height=500,width=450)
    reset_pw_pg_fr.place(x=650, y=100)

    #Heading:
    reset_pw_pg_label1=CTkLabel(reset_pw_pg_fr,text='  Reset Your Password',font=("Times New Roman",40,"bold"),text_color="#FFFFFF")
    reset_pw_pg_label1.place(x=20, y=10)

    #Label for Email 
    reset_email=CTkLabel(reset_pw_pg_fr,text='Email',font=("Times New Roman",20),text_color="#FFFFFF")
    reset_email.place(x=60, y=255)

    #Label for question no. 1
    reset_pw_pg_label2=CTkLabel(reset_pw_pg_fr,text='1.What is your favourite colour?',font=("Times New Roman",20),text_color="#FFFFFF")
    reset_pw_pg_label2.place(x=60, y=75)

    #Label for question no. 2
    reset_pw_pg_label3=CTkLabel(reset_pw_pg_fr,text='2. What kind of music do you like?',font=("Times New Roman",20),text_color="#FFFFFF")
    reset_pw_pg_label3.place(x=60, y=165)

    #Label for New Password
    reset_pw_pg_label4=CTkLabel(reset_pw_pg_fr,text='New Password',font=("Times New Roman",20),text_color="#FFFFFF")
    reset_pw_pg_label4.place(x=60, y=345)

    #Entry box for question no 1
    reset_pw_pg_entry1=CTkEntry(reset_pw_pg_fr, corner_radius=7, height=35, width=320, border_width=0, fg_color="white", text_color="black")
    reset_pw_pg_entry1.place(x=60, y=110)

    #Entry box for question no 2
    reset_pw_pg_entry2=CTkEntry(reset_pw_pg_fr, corner_radius=7, height=35, width=320, border_width=0, fg_color="white", text_color="black")
    reset_pw_pg_entry2.place(x=60, y=200)

    #Entry box for email
    reset_pw_pg_entry3=CTkEntry(reset_pw_pg_fr, corner_radius=7, height=35, width=320, border_width=0, fg_color="white", text_color="black",show="*",placeholder_text="Email")
    reset_pw_pg_entry3.place(x=60, y=290)

    #Entry box for New Password
    reset_pw_pg_entry4=CTkEntry(reset_pw_pg_fr, corner_radius=7, height=35, width=250, border_width=0, fg_color="white", text_color="black",show="*",placeholder_text="New password")
    reset_pw_pg_entry4.place(x=60, y=380)


    
    #CheckButton:
    var1= IntVar()
    pw_c_btn = Checkbutton(reset_pw_pg_fr, text = 'Show',font=("Times New Roman",18,"bold"),activebackground="#000D18",variable = var1,bg="#000D18",  command = new_pass) #for confirm password
    pw_c_btn.place(x=480,y=575)


    #Submit Button
    fp_pg_btn=CTkButton(reset_pw_pg_fr,hover_color="#002234",fg_color="#004367",text="Submit",font=("Times New Roman",20,"bold"),bg_color="#000D18",width=100,height=30,corner_radius=10,command=to_login)
    fp_pg_btn.place(x=170, y=440)
        
    
    
    
    pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Admin_Dashboard~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def admin_dashboard():
    
    
    global img
    #adding mainframe:
    ad_dashb_fr = CTkFrame(root,fg_color="#0D336B")
    ad_dashb_fr.place(relwidth = 1, relheight = 1,relx=0,rely=0)
    
    def programm_cancel(): #logout button
        ad_dashb_fr.place_forget()
        main()
          
        pass
    
    def student_rcd():   #student records
        ad_dashb_fr.place_forget()
        student_records()
        
        pass
    
    
   
    
    def cng_pass(): #change password
        ad_dashb_fr.place_forget()
        change_password()
        pass
    

    #Left Top Frame:
    ad_dashb_fr1 = CTkFrame(root,fg_color="#2C87CF",bg_color="#0D336B",width=530, height=100,corner_radius=10)
    ad_dashb_fr1.place(x=20,y=25)

    #Right Frame:
    ad_dashb_fr3 =CTkFrame(root,fg_color="#2C87CF",bg_color="#0D336B",width=690,height=645,corner_radius=10)
    ad_dashb_fr3 .place(x=570,y=25)

    #inserting image in inner right frame:
    # Load the image
    img = Image.open("std_bg.png")

    # Resize the image if needed
    img = img.resize((1100, 1000))

    # Convert the image to CTkImage
    ctk_img = CTkImage(light_image=img, size=(700, 950))

    # Use CTkImage in the label
    img_lbl = CTkLabel(ad_dashb_fr3, image=ctk_img, text="  ")
    img_lbl.place(relheight=1, relwidth=1)


    #Label:
    ad_dash_lbl = CTkLabel(ad_dashb_fr1,text="  ADMIN  DASHBOARD",text_color="#FFFFFF",fg_color="#2C87CF",font=("Times New Roman",35,"bold"))  #Label of title in top frame
    ad_dash_lbl.place(x=60,y=25)


    #Left Bottom Frame:
    ad_dashb_fr2 = CTkFrame(root,fg_color="#2C87CF",bg_color="#0D336B",width=530, height=525,corner_radius=10)
    ad_dashb_fr2.place(x=20,y=145)

    #Button:
    std_rd_btn = CTkButton(ad_dashb_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" Student Records ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10,command=student_rcd) #Student records button 
    std_rd_btn.place(x=60,y=35)

    cng_pw_btn = CTkButton(ad_dashb_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" Change Password ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10,command=cng_pass) #Change Password button 
    cng_pw_btn.place(x=60,y=300)

    #logOutButton:
    crs_fr1_btn = CTkButton(ad_dashb_fr2, text='LogOut',font=("Times New Roman",19,"bold") ,text_color='#000000',fg_color="#F1BC60", bg_color='#2C87CF',width=130,height=45,hover_color="#E49C1F", corner_radius=10,command=programm_cancel) #LogOut button
    crs_fr1_btn.place(x=195, y=420)


    
    
    
    
    
    pass



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Student_Records~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def student_records():
    
    #mainFrame
    sr_record_fr= CTkFrame(root,fg_color="#FFFFFF")
    sr_record_fr.place(relwidth = 1, relheight = 1) 
    

    # Function to create the students table if it doesn't exist
    def create_students_table():
        conn = sqlite3.connect("sms.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                Students_ID INT,
                Students_Name TEXT,
                Date_Of_Birth TEXT,
                Gender TEXT,
                Email TEXT,
                Phone_Number TEXT,
                Guardians_Name TEXT,
                Address TEXT
            )
        """)
        conn.commit()
        conn.close()
    create_students_table()
    
    # Function to handle submission and storing of student details
    def submit_details():
        Students_ID = std_id_etr.get()
        Students_Name = std_name_etr.get()
        Date_Of_Birth = std_dob_etr.get()
        Gender = std_gender_etr.get()
        Email = std_email_etr.get()
        Phone_Number = std_phnN_etr.get()
        Guardians_Name = std_gN_etr.get()
        Address = std_adrs_etr.get()
    
        if '@gmail.com' not in Email:
            messagebox.showerror("Invalid Email", "Please enter a valid Email address.")
            return
    
        if not Phone_Number.isdigit():
            messagebox.showerror("Invalid Number", "Please enter a valid numeric phone number.")
            return
    
        conn = sqlite3.connect("sms.db")
        cursor = conn.cursor()
    
        cursor.execute("""
        INSERT INTO students (Students_ID, Students_Name, Date_Of_Birth, Gender, Email, Phone_Number, Guardians_Name, Address)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, 
        (Students_ID, Students_Name, Date_Of_Birth, Gender, Email, Phone_Number, Guardians_Name, Address))
        
        conn.commit()
        conn.close()
    
        clear_entries() 
    
        messagebox.showinfo('Success', 'Student details added successfully!')
    
    # Function to clear entries after submission
    def clear_entries():
        std_id_etr.delete(0, END)
        std_name_etr.delete(0, END)
        std_dob_etr.delete(0, END)
        std_gender_etr.delete(0, END)
        std_email_etr.delete(0, END)
        std_phnN_etr.delete(0, END)
        std_gN_etr.delete(0, END)
        std_adrs_etr.delete(0, END)
    
    # Define function to update data in the database
    def update_data():
        selected_item = student_table.selection()[0]
        values = student_table.item(selected_item, 'values')
    
        Students_ID = values[0]
        Students_Name = std_name_etr.get()
        Date_Of_Birth = std_dob_etr.get()
        Gender = std_gender_etr.get()
        Email = std_email_etr.get()
        Phone_Number = std_phnN_etr.get()
        Guardians_Name = std_gN_etr.get()
        Address = std_adrs_etr.get()
    
        conn = sqlite3.connect("sms.db")
        cursor = conn.cursor()
    
        cursor.execute("""
        UPDATE students SET Students_Name=?, Date_Of_Birth=?, Gender=?, Email=?, Phone_Number=?, Guardians_Name=?, Address=? WHERE Students_ID=?
        """, (Students_Name, Date_Of_Birth, Gender, Email, Phone_Number, Guardians_Name, Address, Students_ID))
    
        conn.commit()
        conn.close()
    
        populate_student_table()
    
        messagebox.showinfo('Success', 'Student details updated successfully!')
    
    # Define function to delete data from the database
    def delete_student():
        selected_item = student_table.selection()[0]
        selected_id = student_table.item(selected_item)['values'][0]
    
        conn = sqlite3.connect("sms.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE Students_ID=?", (selected_id,))
        conn.commit()
        conn.close()
    
        student_table.delete(selected_item)
    
        messagebox.showinfo('Success', 'Student details deleted successfully!')
    
    # Define function to fetch all data from the database
    def fetch_data_from_db():
        conn = sqlite3.connect('sms.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()
        conn.close()
        return records
    
    # Populate the Treeview with data from the database
    def populate_student_table():
        for row in student_table.get_children():
            student_table.delete(row)
        data = fetch_data_from_db()
        for record in data:
            student_table.insert('', 'end', values=record)
    

    # Adding main frame
    std_record_fr = CTkFrame(sr_record_fr, fg_color="#0D336B")
    std_record_fr.place(relwidth=1, relheight=1, relx=0, rely=0)
    
    # Top Frame
    std_record_fr1 = CTkFrame(sr_record_fr, fg_color="#2C87CF", bg_color="#0D336B", width=1240, height=45, corner_radius=10)
    std_record_fr1.place(x=20, y=15)
    
    # Left Frame
    std_record_fr2 = CTkFrame(sr_record_fr, fg_color="#2C87CF", bg_color="#0D336B", width=529, height=600, corner_radius=10)
    std_record_fr2.place(x=20, y=75)
    
    # Right Frame
    std_record_fr3 = CTkFrame(sr_record_fr, fg_color="#2C87CF", bg_color="#0D336B", width=690, height=600, corner_radius=10)
    std_record_fr3.place(x=570, y=75)
    
    # Inner Right Frame
    stdr_fr3_fr = CTkFrame(std_record_fr3, fg_color="#2C87CF", border_color="#0D336B", border_width=3, corner_radius=10, height=85, width=660)
    stdr_fr3_fr.place(x=15, y=9)
    
    # Label in top frame
    stdr_label_fr1 = CTkLabel(std_record_fr1, text='STUDENT RECORDS', text_color='#FFFFFF', font=("Times New Roman", 35, "bold"))
    stdr_label_fr1.place(x=440, y=0)
    
    # Labels and Entries in left frame
    std_id = CTkLabel(std_record_fr2, text="Student Id :", text_color="#FFFFFF", fg_color="#2C87CF", font=("Times New Roman", 20, "bold"))
    std_id.place(x=20, y=25)
    std_id_etr = CTkEntry(std_record_fr2, corner_radius=12, height=38, width=330, border_width=0, fg_color="white", text_color="black")
    std_id_etr.place(x=175, y=25)
    
    std_name = CTkLabel(std_record_fr2, text="Student Name :", text_color="#FFFFFF", fg_color="#2C87CF", font=("Times New Roman", 20, "bold"))
    std_name.place(x=20, y=85)
    std_name_etr = CTkEntry(std_record_fr2, corner_radius=12, height=38, width=330, border_width=0, fg_color="white", text_color="black")
    std_name_etr.place(x=175, y=85)
    
    std_DOB = CTkLabel(std_record_fr2, text="Date of Birth :", text_color="#FFFFFF", fg_color="#2C87CF", font=("Times New Roman", 20, "bold"))
    std_DOB.place(x=20, y=145)
    std_dob_etr = CTkEntry(std_record_fr2, corner_radius=12, height=38, width=330, border_width=0, fg_color="white", text_color="black")
    std_dob_etr.place(x=175, y=145)
    
    std_gender = CTkLabel(std_record_fr2, text="Gender :", text_color="#FFFFFF", fg_color="#2C87CF", font=("Times New Roman", 20, "bold"))
    std_gender.place(x=20, y=205)
    std_gender_etr = CTkEntry(std_record_fr2, corner_radius=12, height=38, width=330, border_width=0, fg_color="white", text_color="black")
    std_gender_etr.place(x=175, y=205)
    
    std_email = CTkLabel(std_record_fr2, text="Email :", text_color="#FFFFFF", fg_color="#2C87CF", font=("Times New Roman", 20, "bold"))
    std_email.place(x=20, y=265)
    std_email_etr = CTkEntry(std_record_fr2, corner_radius=12, height=38, width=330, border_width=0, fg_color="white", text_color="black")
    std_email_etr.place(x=175, y=265)
    
    std_phn_num = CTkLabel(std_record_fr2, text="Phone Number :", text_color="#FFFFFF", fg_color="#2C87CF", font=("Times New Roman", 20, "bold"))
    std_phn_num.place(x=20, y=325)
    std_phnN_etr = CTkEntry(std_record_fr2, corner_radius=12, height=38, width=330, border_width=0, fg_color="white", text_color="black")
    std_phnN_etr.place(x=175, y=325)
    
    std_guardians_nm = CTkLabel(std_record_fr2, text="Guardian's Name :", text_color="#FFFFFF", fg_color="#2C87CF", font=("Times New Roman", 20, "bold"))
    std_guardians_nm.place(x=20, y=385)
    std_gN_etr = CTkEntry(std_record_fr2, corner_radius=12, height=38, width=330, border_width=0, fg_color="white", text_color="black")
    std_gN_etr.place(x=175, y=385)
    
    std_adrs = CTkLabel(std_record_fr2, text="Address :", text_color="#FFFFFF", fg_color="#2C87CF", font=("Times New Roman", 20, "bold"))
    std_adrs.place(x=20, y=445)
    std_adrs_etr = CTkEntry(std_record_fr2, corner_radius=12, height=38, width=330, border_width=0, fg_color="white", text_color="black")
    std_adrs_etr.place(x=175, y=445)
    
    # Add, Update, Delete buttons in the left frame
    std_add_btn = CTkButton(std_record_fr2, width=130, height=32, text='ADD', corner_radius=10, font=("Times New Roman", 15, "bold"),text_color="#FFFFFF", fg_color="#0D336B", hover_color="orange", command=submit_details)
    std_add_btn.place(x=25, y=515)
    
    std_update_btn = CTkButton(std_record_fr2, width=130, height=32, text='UPDATE', corner_radius=10, font=("Times New Roman", 15, "bold"),text_color="#FFFFFF", fg_color="#0D336B", hover_color="orange", command=update_data)
    std_update_btn.place(x=195, y=515)
    
    std_delete_btn = CTkButton(std_record_fr2, width=130, height=32, text='DELETE', corner_radius=10, font=("Times New Roman", 15, "bold"),text_color="#FFFFFF", fg_color="#0D336B", hover_color="orange", command=delete_student)
    std_delete_btn.place(x=365, y=515)
    
    # Treeview in right frame to display student details
    student_table = ttk.Treeview(stdr_fr3_fr, columns=("id", "name", "dob", "gender", "email", "phone", "guardian", "address"), show='headings')

    student_table.heading('id', text="ID")
    student_table.heading('name', text="Name")
    student_table.heading('dob', text="DOB")
    student_table.heading('gender', text="Gender")
    student_table.heading('email', text="Email")
    student_table.heading('phone', text="Phone")
    student_table.heading('guardian', text="Guardian")
    student_table.heading('address', text="Address")
    student_table.pack(fill=BOTH, expand=TRUE)
    
    # Call the function to populate the treeview with data
    populate_student_table()
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass






#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Change_password_page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def change_password():
    
    
    #adding mainframe:
    ad_dashb_fr = CTkFrame(root,fg_color="#0D336B")
    ad_dashb_fr.place(relwidth = 1, relheight = 1,relx=0,rely=0)
    conn = sqlite3.connect("sms.db")
    c = conn.cursor()
    


    def current_pass():
    
        if cpw_etr.cget("show") == "*":
            cpw_etr.configure(show = '')
        else:
            cpw_etr.configure(show = '*')
        
        pass

    def new_pass():
        if npw_etr.cget("show") == "*":
            npw_etr.configure(show = '')
        else:
            npw_etr.configure(show = '*')
        
        pass

    def confirm_pass():
        if cn_pw_etr.cget("show") == "*":
            cn_pw_etr.configure(show = '')
        else:
            cn_pw_etr.configure(show = '*')
        
        pass


    #Left Top Frame:
    ad_dashb_fr1 = CTkFrame(root,fg_color="#2C87CF",bg_color="#0D336B",width=530, height=100,corner_radius=10)
    ad_dashb_fr1.place(x=20,y=25)

    #Label:
    ad_dash_lbl = CTkLabel(ad_dashb_fr1,text="ADMIN  DASHBOARD",text_color="#FFFFFF",fg_color="#2C87CF",font=("Times New Roman",35,"bold"))  #Label of title in top frame
    ad_dash_lbl.place(x=60,y=25)


    #Left Bottom Frame:
    ad_dashb_fr2 = CTkFrame(root,fg_color="#2C87CF",bg_color="#0D336B",width=530, height=525,corner_radius=10)
    ad_dashb_fr2.place(x=20,y=145)


    #Button:

    std_rd_btn = CTkButton(ad_dashb_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" Student Records ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Student records button 
    std_rd_btn.place(x=60,y=35)

    cng_pw_btn = CTkButton(ad_dashb_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" Change Password ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Student records button 
    cng_pw_btn.place(x=60,y=300)


    #logOutButton:
    crs_fr1_btn = CTkButton(ad_dashb_fr2, text='LogOut',font=("Times New Roman",19,"bold") ,text_color='#000000',fg_color="#F1BC60", bg_color='#2C87CF',width=130,height=45,hover_color="#E49C1F", corner_radius=10) #LogOut button
    crs_fr1_btn.place(x=195, y=420)


    #Right Frame:
    ad_dashb_fr3 =CTkFrame(ad_dashb_fr,fg_color="#2C87CF",bg_color="#0D336B",width=690,height=645,corner_radius=10)
    ad_dashb_fr3 .place(x=570,y=25)

    #Inner Right Frame:
    ad_dashb_fr4 = CTkFrame(ad_dashb_fr3,fg_color="#0F56A2",bg_color="#2C87CF",width=400, height=500,corner_radius=2)
    ad_dashb_fr4.place(x=160, y=80)

    #Contains in inner right frame:

    #adding label:
    cng_pw_lbl = CTkLabel(ad_dashb_fr4,text="Change Password",text_color="white",font=("Times New Roman",25,"bold") ,fg_color="#0F56A2")
    cng_pw_lbl.place(x=100,y=25)

    cn_pw_lbl = CTkLabel(ad_dashb_fr4,text="Confirm Your New Password",text_color="white",font=("Times New Roman",16) ,fg_color="#0F56A2")
    cn_pw_lbl.place(x=45,y=290)


    #adding entry:
    cpw_etr = CTkEntry(ad_dashb_fr4,corner_radius=12,height=38,width=240,border_width=0,fg_color="white",text_color="black",placeholder_text="Current Password",placeholder_text_color="grey",show="*")  
    cpw_etr.place(x=45,y=150)

    npw_etr = CTkEntry(ad_dashb_fr4,corner_radius=12,height=38,width=240,border_width=0,fg_color="white",text_color="black",placeholder_text="New Password",placeholder_text_color="grey", show='*')  
    npw_etr.place(x=45,y=240)

    cn_pw_etr = CTkEntry(ad_dashb_fr4,corner_radius=12,height=38,width=240,border_width=0,fg_color="white",text_color="black",placeholder_text="Type Your New Password",placeholder_text_color="grey", show='*')
    cn_pw_etr.place(x=45,y=330)

    #Button:
    submit_btn = CTkButton(ad_dashb_fr4,hover_color="#0D336B",fg_color="#1792F3",text=" Submit ",font=("Times New Roman", 19, "bold"),bg_color="#0F56A2",width=100,height=40,corner_radius=9) #Submit button
    submit_btn.place(x=140,y=420)

    #CheckButtons:
    var = IntVar()
    new_pw_btn = Checkbutton(ad_dashb_fr4, text = 'Show',font=("Times New Roman",18,"bold"),activebackground="#0F56A2",variable = var,bg="#0F56A2",  command = current_pass)  #for current password
    new_pw_btn.place(x=450,y=235)

    varr = IntVar()
    new_pw_btn = Checkbutton(ad_dashb_fr4, text = 'Show',font=("Times New Roman",18,"bold"),activebackground="#0F56A2",variable = varr,bg="#0F56A2",  command = new_pass)  #for new password
    new_pw_btn.place(x=450,y=370)

    varrr = IntVar()
    Cnew_btn = Checkbutton(ad_dashb_fr4, text = 'Show',font=("Times New Roman",18,"bold"),activebackground="#0F56A2",variable = varrr,bg="#0F56A2",  command = confirm_pass) #to confirm new password
    Cnew_btn.place(x=450,y=500)
    
    
    
    

    
    pass








#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Home_Page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def main():
    
    global bg_image, main_frame
    main_frame = CTkFrame(root)
    main_frame.place(relwidth = 1, relheight = 1)

    #importing image:
    bg_image = Image.open("homepage_bg.png")
    bg_image=bg_image.resize((1920,1060))
    bg_imagetk=ImageTk.PhotoImage(bg_image)
    label=Label(main_frame,width=x,height=y,image=bg_imagetk)
    label.place(relheight=1,relwidth=1)
    label.image = bg_imagetk

    #Frame: For Buttons:
    frame1=CTkFrame(main_frame,fg_color='#99D2DC',bg_color="#ADDEE9",height=390,width=400,corner_radius=20)
    frame1.place(x=440,y=180)

    #Frame: For heading
    frame2=Frame(main_frame,background='#008EAF',height=170,width=600)
    frame2.place(x=660, y=230)

    #For heading:
    heading=Label(frame2, text='THE GRACE ACADEMY', fg='#FFD495', bg='#008EAF', font=("Times New Roman", 38,"bold"))
    heading.place(x=5, y=5)

    motto=Label(frame2, text='"A Legacy of Grace, A Future of Success."', fg='#FFD495', bg='#008EAF', font=("Brush Script MT", 25,"italic") )
    motto.place(x=60,y=85)

    #For Buttons:
    Admin_SignUp=CTkButton(frame1, text='Admin SignUp ',font=('Times New Roman',35,"bold"),text_color="#0B4B5D",fg_color="#F1BC60",corner_radius=25,hover_color="#F3EBB7",width=300,height=40,command=admin_signup)
    Admin_SignUp=Admin_SignUp.place(x=50,y=160)

    Admin_LogIn=CTkButton(frame1, text=' Admin LogIn  ',font=('Times New Roman',35,"bold"),text_color="#0B4B5D",fg_color="#F1BC60",corner_radius=25,hover_color="#F3EBB7",width=300,height=40,command= admin_login)
    Admin_LogIn=Admin_LogIn.place(x=50,y=260)




main()


root.mainloop()