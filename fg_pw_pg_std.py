######~~~~Security_Page_for_student~~~~~#######
 
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

reset_pw_pg_frm=CTkFrame(root,fg_color="#FFFFFF")
reset_pw_pg_frm.place(relwidth = 1, relheight = 1)

#importing image:
reset_pw_bg_img = Image.open("Security_page_bg.png")
reset_pw_bg_img=reset_pw_bg_img.resize((1920,1060))
reset_pw_bg_imgtk=ImageTk.PhotoImage(reset_pw_bg_img)
label=Label(reset_pw_pg_frm,width=x,height=y,image=reset_pw_bg_imgtk)
label.image = reset_pw_bg_imgtk
label.place(relheight=1,relwidth=1)


#to show password:
def new_pass():
    if reset_pw_pg_entry3.cget("show") == "*":
        reset_pw_pg_entry3.configure(show = '')
    else:
        reset_pw_pg_entry3.configure(show = '*')

#to show confirm_pass:
def confirm_pass():
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

#Label for question no. 1
reset_pw_pg_label2=CTkLabel(reset_pw_pg_fr,text='1.What is your favourite colour?',font=("Times New Roman",20),text_color="#FFFFFF")
reset_pw_pg_label2.place(x=60, y=75)

#Label for question no. 2
reset_pw_pg_label3=CTkLabel(reset_pw_pg_fr,text='2. What kind of music do you like?',font=("Times New Roman",20),text_color="#FFFFFF")
reset_pw_pg_label3.place(x=60, y=165)

#Label for New Password
reset_pw_pg_label4=CTkLabel(reset_pw_pg_fr,text='New Password',font=("Times New Roman",20),text_color="#FFFFFF")
reset_pw_pg_label4.place(x=60, y=255)

#Label for Confirm Password
reset_pw_pg_label5=CTkLabel(reset_pw_pg_fr,text='Confirm Password',font=("Times New Roman",20),text_color="#FFFFFF")
reset_pw_pg_label5.place(x=60, y=345)

#Entry box for question no 1
reset_pw_pg_entry1=CTkEntry(reset_pw_pg_fr, corner_radius=7, height=35, width=320, border_width=0, fg_color="white", text_color="black")
reset_pw_pg_entry1.place(x=60, y=110)

#Entry box for question no 2
reset_pw_pg_entry2=CTkEntry(reset_pw_pg_fr, corner_radius=7, height=35, width=320, border_width=0, fg_color="white", text_color="black")
reset_pw_pg_entry2.place(x=60, y=200)

#Entry box for new password
reset_pw_pg_entry3=CTkEntry(reset_pw_pg_fr, corner_radius=7, height=35, width=250, border_width=0, fg_color="white", text_color="black",show="*",placeholder_text="new password")
reset_pw_pg_entry3.place(x=60, y=290)

#Entry box foe Confirm Password
reset_pw_pg_entry4=CTkEntry(reset_pw_pg_fr, corner_radius=7, height=35, width=250, border_width=0, fg_color="white", text_color="black",show="*",placeholder_text="confirm password")
reset_pw_pg_entry4.place(x=60, y=380)


 
#CheckButton:
var1 = IntVar()
pw_c_btn = Checkbutton(reset_pw_pg_fr, text = 'Show',font=("Times New Roman",18,"bold"),activebackground="#000D18",variable = var1,bg="#000D18",  command = new_pass)  #for new password
pw_c_btn.place(x=480,y=440)

var2 = IntVar()
pw_c_btn = Checkbutton(reset_pw_pg_fr, text = 'Show',font=("Times New Roman",18,"bold"),activebackground="#000D18",variable = var2,bg="#000D18",  command = confirm_pass) #for confirm password
pw_c_btn.place(x=480,y=575)


 
 
root.mainloop()