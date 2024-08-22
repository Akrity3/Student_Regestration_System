#######~~~~~ADMIN_DASHBOARD~~~~~~############

from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from customtkinter import CTkImage

# Initialize the main window:
root = CTk()
root.geometry('1920x1080+0+0')
root.title('Student Registration System')
root.iconbitmap("logo.ico")
root._set_appearance_mode("light")

#adding mainframe:
ad_dashb_fr = CTkFrame(root,fg_color="#0D336B")
ad_dashb_fr.place(relwidth = 1, relheight = 1,relx=0,rely=0)
    

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

std_rd_btn = CTkButton(ad_dashb_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" Student Records ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Student records button 
std_rd_btn.place(x=60,y=100)


cng_pw_btn = CTkButton(ad_dashb_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" Change Password ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10)    #,command=cng_pass) #Change Password button 
cng_pw_btn.place(x=60,y=300)


#logOutButton:
crs_fr1_btn = CTkButton(ad_dashb_fr2, text='LogOut',font=("Times New Roman",19,"bold") ,text_color='#000000',fg_color="#F1BC60", bg_color='#2C87CF',width=130,height=45,hover_color="#E49C1F", corner_radius=10)   #,command=programm_cancel) #LogOut button
crs_fr1_btn.place(x=195, y=420)



root.mainloop()