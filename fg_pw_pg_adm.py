######~~~~Security_Page_for_admin~~~~~#######
 
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

#For background Image:
x=root.winfo_screenwidth()
y=root.winfo_screenheight()

adm_reset_pw_pg_frm=CTkFrame(root,fg_color="#FFFFFF")
adm_reset_pw_pg_frm.place(relwidth = 1, relheight = 1)

#importing image:
adm_reset_pw_bg_img = Image.open("Security_page_bg.png")
adm_reset_pw_bg_img=adm_reset_pw_bg_img.resize((1920,1060))
adm_reset_pw_bg_imgtk=ImageTk.PhotoImage(adm_reset_pw_bg_img)

adm_rp_label=Label(adm_reset_pw_pg_frm,width=x,height=y,image=adm_reset_pw_bg_imgtk)
adm_rp_label.image = adm_reset_pw_bg_imgtk
adm_rp_label.place(relheight=1,relwidth=1)


#to show password:
def new_pass():
    if adm_reset_pw_pg_entry3.cget("show") == "*":
        adm_reset_pw_pg_entry3.configure(show = '')
    else:
        adm_reset_pw_pg_entry3.configure(show = '*')

#to show confirm_pass:
def confirm_pass():
    if adm_reset_pw_pg_entry4.cget("show") == "*":
        adm_reset_pw_pg_entry4.configure(show = '')
    else:
        adm_reset_pw_pg_entry4.configure(show = '*')




#Frame for labels:
adm_reset_pw_pg_fr=CTkFrame(adm_reset_pw_pg_frm,fg_color="#000D18",bg_color="#000D18",height=500,width=450)
adm_reset_pw_pg_fr.place(x=650, y=100)

#Heading:
adm_reset_pw_pg_label1=CTkLabel(adm_reset_pw_pg_fr,text='  Reset Your Password',font=("Times New Roman",40,"bold"),text_color="#FFFFFF")
adm_reset_pw_pg_label1.place(x=20, y=10)

#Label for question no. 1
adm_reset_pw_pg_label2=CTkLabel(adm_reset_pw_pg_fr,text='1.What is your favourite colour?',font=("Times New Roman",20),text_color="#FFFFFF")
adm_reset_pw_pg_label2.place(x=60, y=75)

#Label for question no. 2

adm_reset_pw_pg_label3=CTkLabel(adm_reset_pw_pg_fr,text='2. What kind of music do you like?',font=("Times New Roman",20),text_color="#FFFFFF")
adm_reset_pw_pg_label3.place(x=60, y=165)

#Label for New Password

adm_reset_pw_pg_label4=CTkLabel(adm_reset_pw_pg_fr,text='New Password',font=("Times New Roman",20),text_color="#FFFFFF")
adm_reset_pw_pg_label4.place(x=60, y=255)

#Label for Confirm Password

adm_reset_pw_pg_label5=CTkLabel(adm_reset_pw_pg_fr,text='Confirm Password',font=("Times New Roman",20),text_color="#FFFFFF")
adm_reset_pw_pg_label5.place(x=60, y=345)

#Entry box for question no 1

adm_reset_pw_pg_entry1=CTkEntry(adm_reset_pw_pg_fr, corner_radius=7, height=35, width=320, border_width=0, fg_color="white", text_color="black")
adm_reset_pw_pg_entry1.place(x=60, y=110)

#Entry box for question no 2

adm_reset_pw_pg_entry2=CTkEntry(adm_reset_pw_pg_fr, corner_radius=7, height=35, width=320, border_width=0, fg_color="white", text_color="black")
adm_reset_pw_pg_entry2.place(x=60, y=200)

#Entry box for new password

adm_reset_pw_pg_entry3=CTkEntry(adm_reset_pw_pg_fr, corner_radius=7, height=35, width=250, border_width=0, fg_color="white", text_color="black",show="*",placeholder_text="new password")
adm_reset_pw_pg_entry3.place(x=60, y=290)

#Entry box for Confirm Password

adm_reset_pw_pg_entry4=CTkEntry(adm_reset_pw_pg_fr, corner_radius=7, height=35, width=250, border_width=0, fg_color="white", text_color="black",show="*",placeholder_text="confirm password")
adm_reset_pw_pg_entry4.place(x=60, y=380)


 
#CheckButton:

var1 = IntVar()
adm_new_pw_btn = Checkbutton(adm_reset_pw_pg_fr, text = 'Show',font=("Times New Roman",18,"bold"),activebackground="#000D18",variable = var1,bg="#000D18",  command = new_pass)  #for new password
adm_new_pw_btn.place(x=480,y=440)

var2 = IntVar()
adm_pw_c_btn = Checkbutton(adm_reset_pw_pg_fr, text = 'Show',font=("Times New Roman",18,"bold"),activebackground="#000D18",variable = var2,bg="#000D18",  command = confirm_pass) #for confirm password
adm_pw_c_btn.place(x=480,y=575)



 
root.mainloop()