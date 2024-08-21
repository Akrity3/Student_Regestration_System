from tkinter import *
from customtkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk
from customtkinter import CTkImage
 
# Initialize the main window
root = CTk()
root.geometry('1920x1080+0+0')
root.title('Student Management System')
root._set_appearance_mode("light")



# upperframe
frame=CTkFrame(master=root, fg_color="#153519", corner_radius=0)
frame.place(x =0,y =0, w=1920, h=160)
 

#insert image
pil_image1 = Image.open("dashicon.png")
 
# imageresize
pil_image1 = pil_image1.resize((150,150))
 
# Convert the PIL image to a PhotoImage object
photo_image = ImageTk.PhotoImage(pil_image1)
 
# Create a Label widget to display the image
label = tk.Label(root, image=photo_image)
label.place(x=20, y=14, w=133, h=133)
 
#to prevent images from being garbage collected
label=pil_image1
 
 
 
# frame
frame=customtkinter.CTkFrame(master=root, fg_color="#000000",bg_color="#FFFFFF", corner_radius=20)
frame.place(x =417,y =251, w=1250, h=670)
 
#possible destination frame
frame3=customtkinter.CTkFrame(master=root, fg_color="#000000", corner_radius=0)
frame3.place(x =0,y =128, w=380, h=130)
 
#destinations frame
frame4=customtkinter.CTkFrame(master=root, fg_color="#99B104",corner_radius=0)
frame4.place(x =0,y =232, w=380, h=818)
 
# “I now walk into the wild.”
label1 = CTkLabel(master=root, text="“I now walk into the wild.”", font=("Bold Italic", 20, "bold"), text_color="#000000",fg_color="#FFFFFF")
label1.place(x=330, y=130, w=310, h=68)
 
#Hi, User*
label1 = CTkLabel(master=root, text="Hi, User*", font=("Calibri", 35, "bold"), text_color="#FFFFFF", fg_color="#153519")
label1.place(x=1300, y=50, w=182, h=38)
 
#  ― Jon Krakauer,
label1 = CTkLabel(master=root, text=" ― Jon Krakauer,", font=("Bold Italic", 20, ), text_color="#000000",fg_color="#FFFFFF")
label1.place(x=1143, y=172, w=200, h=25)
 
#  Into the Wild
label1 = CTkLabel(master=root, text="Into the Wild", font=("Bold Italic", 20, "underline"), text_color="#000000",fg_color="#FFFFFF")
label1.place(x=1300, y=172, w=168, h=28)
 
#welcome back
label1 = CTkLabel(master=root, text="Welcome back!", font=("Inter", 26, "bold"), text_color="#FFFFFF", fg_color="#000000")
label1.place(x=10, y=145, w=360, h=36)
 
#BOSS
label1 = CTkLabel(master=root, text="BOSS", font=("Inter", 26, "bold"), text_color="#FFFFFF", fg_color="#000000")
label1.place(x=10, y=185, w=360, h=36)
 
#Welcome to
label1 = CTkLabel(master=root, text="Welcome to", font=("Inter", 20), text_color="#FFFFFF", fg_color="#153519")
label1.place(x=100, y=40, w=150, h=36)
 
#Ghumna Jau
label1 = CTkLabel(master=root, text="Ghumna Jau", font=("Inter", 20,"bold"), text_color="#FFFFFF", fg_color="#153519")
label1.place(x=100, y=65, w=150, h=36)
 
 
#Dashboard
bookingdate_btn=CTkButton(master=root, text="Dashboard",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#99B104",hover_color="#738600",bg_color="#99B104", corner_radius=0,command=dash)
bookingdate_btn.place(x=0, y=250, w=380,h=117)
bookingdate_indicate=tk.Label( bg="#FFFFFF")
bookingdate_indicate.place(x=0, y=315, w=8, h=117)
 
#Client
clientid_btn=CTkButton(master=root, text="Client",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#738600",hover_color="#000000",bg_color="#99B104", corner_radius=0)
clientid_btn.place(x=0, y=343, w=380,h=117)
clientid_indicate=tk.Label( bg="#FFFFFF")
clientid_indicate.place(x=0, y=430, w=8, h=117)
 
#SEARCH
label1 = CTkLabel(master=root, text="Search", font=("Inter", 30, "bold"), text_color="#FFFFFF", fg_color="#000000")
label1.place(x=858, y=262, w=128, h=55)
 
# frame
frame1=customtkinter.CTkFrame(master=root, fg_color="#FFFFFF",bg_color="#000000", corner_radius=20)
frame1.place(x =460,y =320, w=1150, h=180)
#First name
label1 = CTkLabel(master=root, text="First name", font=("Inter", 19, "bold"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=490, y=330, w=130, h=34)
entry1=CTkEntry(master=root, placeholder_text="Enter your first name",fg_color="#000000",bg_color="#FFFFFF")
entry1.place(x=600, y=330, w=407,h=34)
btn1=CTkButton(master=root, text="Search",font=("Calibri",19, "bold"),text_color="#000000",fg_color="#FFFFFF",bg_color="#FFFFFF")
btn1.place(x=1273, y=344, w=115,h=23)
 
 
label1 = CTkLabel(master=root, text="Last name", font=("Inter", 19, "bold"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=490, y=360, w=130, h=34)
entry1=CTkEntry(master=root, placeholder_text="Enter your last name",fg_color="#000000",bg_color="#FFFFFF")
entry1.place(x=600, y=360, w=407,h=34)
btn2=CTkButton(master=root, text="Search",font=("Calibri",19, "bold"),text_color="#000000",fg_color="#FFFFFF",bg_color="#FFFFFF")
btn2.place(x=1273, y=384, w=115,h=23)
 
label1 = CTkLabel(master=root, text="Email", font=("Inter", 19, "bold"), text_color="#000000", fg_color="#FFFFFF")
label1.place(x=490, y=390, w=90, h=34)
entry1=CTkEntry(master=root, placeholder_text="Enter your email",fg_color="#000000",bg_color="#FFFFFF")
entry1.place(x=600, y=390, w=407,h=34)
btn3=CTkButton(master=root, text="Search",font=("Calibri",19, "bold"),text_color="#000000",fg_color="#FFFFFF",bg_color="#FFFFFF")
btn3.place(x=1273, y=419, w=115,h=23)
 
 
 
frame2=customtkinter.CTkFrame(master=root, fg_color="#FFFFFF",bg_color="#000000", corner_radius=20)
frame2.place(x =460,y =475, w=1150, h=310)
 
 
 
 
 
 
 
# Table
table=ttk.Treeview(frame2, columns=('first','last','ph. no','password', 'location'),show='headings')
table.heading('first', text='First name')
table.heading('last', text='Last name')
table.heading('ph. no', text='Phone no')
table.heading('password', text='Password')
table.heading('location', text='Location')
table.place(x =0,y =0, w=1150,h=33)
 
 
 
 
#Location
location_btn=CTkButton(master=root, text="Location",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#99B104",hover_color="#738600",bg_color="#99B104", corner_radius=0,command=location)
location_btn.place(x=0, y=436, w=380,h=117)
location_indicate=tk.Label( bg="#FFFFFF")
location_indicate.place(x=0, y=546, w=8, h=117)
 
#Exit
transport_btn=CTkButton(master=root, text="EXIT",font=("Inter",28, "bold"),text_color="#FFFFFF",fg_color="#99B104",hover_color="#738600",bg_color="#99B104", corner_radius=0, command=logout)
transport_btn.place(x=0, y=529, w=380,h=117)
transport_indicate=tk.Label( bg="#FFFFFF")
transport_indicate.place(x=0, y=662, w=8, h=117)
 
 
btn4=CTkButton(master=root, text="Clear",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#FFFFFF")
btn4.place(relx = 0.38, rely = 0.5)
 
btn5=CTkButton(master=root, text="All data",font=("Calibri",19, "bold"),text_color="#FFFFFF",fg_color="#000000",bg_color="#FFFFFF")
btn5.place(relx = 0.48, rely = 0.5)
 
btn1=CTkButton(master=root, text="Update",font=("Calibri",19, "bold"),text_color="#000",fg_color="#FFFFFF",bg_color="#000000", command="")
btn1.place(relx = 0.3, rely = 0.87)
 
btn2=CTkButton(master=root, text="Delete",font=("Calibri",19, "bold"),text_color="#000000",fg_color="#AEAEAE",bg_color="#000000")
btn2.place(relx = 0.4, rely = 0.87)
 
btn3=CTkButton(master=root, text="Exit",font=("Calibri",19, "bold"),text_color="#000000",fg_color="#AEAEAE",bg_color="#000000")
btn3.place(relx = 0.5, rely = 0.87)
 
 
root.mainloop()
 
 