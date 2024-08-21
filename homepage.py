#~~~~~~~~~~~~~~HomePage~~~~~~~~~~~~~#
from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Initialize the main window
root = CTk()
root.geometry('1920x1080+0+0')
root.title('Student Management System')
root.iconbitmap("logo.ico")

#For background Image:
x=root.winfo_screenwidth()
y=root.winfo_screenheight()

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
Admin_SignUp=CTkButton(frame1, text='Admin SignUp ',font=('Times New Roman',35,"bold"),text_color="#0B4B5D",fg_color="#F1BC60",corner_radius=25,hover_color="#F3EBB7",width=300,height=40)
Admin_SignUp=Admin_SignUp.place(x=50,y=160)

Admin_LogIn=CTkButton(frame1, text=' Admin LogIn  ',font=('Times New Roman',35,"bold"),text_color="#0B4B5D",fg_color="#F1BC60",corner_radius=25,hover_color="#F3EBB7",width=300,height=40)
Admin_LogIn=Admin_LogIn.place(x=50,y=260)


root.mainloop()
