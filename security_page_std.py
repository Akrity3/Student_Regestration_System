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

security_pg_frm=CTkFrame(root,fg_color="#FFFFFF")
security_pg_frm.place(relwidth = 1, relheight = 1)

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
security_pg_label1=CTkLabel(security_pg_label_fr,text='  Security Qusetions',font=("Times New Roman",45,"bold"),text_color="#FFFFFF")
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
security_pg_btn=CTkButton(security_pg_label_fr,hover_color="#002234",fg_color="#004367",text="Submit",font=("Times New Roman",20,"bold"),bg_color="#000D18",width=100,height=30,corner_radius=10)
security_pg_btn.place(x=170, y=300)


 
root.mainloop()