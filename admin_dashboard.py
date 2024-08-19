#######~~~~~ADMIN_DASHBOARD~~~~~~############

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

#adding mainframe:
ad_dashb_fr = CTkFrame(root,fg_color="#0D336B")
ad_dashb_fr.place(relwidth = 1, relheight = 1,relx=0,rely=0)

#Left Top Frame:
ad_dashb_fr1 = CTkFrame(root,fg_color="#2C87CF",bg_color="#0D336B",width=530, height=100,corner_radius=10)
ad_dashb_fr1.place(x=20,y=25)

#Right Frame:
ad_dashb_fr3 =CTkFrame(root,fg_color="#2C87CF",bg_color="#0D336B",width=690,height=645,corner_radius=10)
ad_dashb_fr3 .place(x=570,y=25)

#Label:
ad_dash_lbl = CTkLabel(ad_dashb_fr1,text="ADMIN  DASHBOARD",text_color="#FFFFFF",fg_color="#2C87CF",font=("Times New Roman",35,"bold"))  #Label of title in top frame
ad_dash_lbl.place(x=60,y=25)


#Left Bottom Frame:
ad_dashb_fr2 = CTkFrame(root,fg_color="#2C87CF",bg_color="#0D336B",width=530, height=525,corner_radius=10)
ad_dashb_fr2.place(x=20,y=145)

#Button:

std_rd_btn = CTkButton(ad_dashb_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" Student Records ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Student records button 
std_rd_btn.place(x=60,y=35)

my_crs_btn = CTkButton(ad_dashb_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" My Courses ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #My Courses button 
my_crs_btn.place(x=60,y=120)

ntc_brd_btn = CTkButton(ad_dashb_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" Notice Board ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Notice Board button 
ntc_brd_btn.place(x=60,y=210)

cng_pw_btn = CTkButton(ad_dashb_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" Change Password ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Change Password button 
cng_pw_btn.place(x=60,y=300)


#logOutButton:
crs_fr1_btn = CTkButton(ad_dashb_fr2, text='LogOut',font=("Times New Roman",19,"bold") ,text_color='#000000',fg_color="#F1BC60", bg_color='#2C87CF',width=130,height=45,hover_color="#E49C1F", corner_radius=10) #LogOut button
crs_fr1_btn.place(x=195, y=420)










root.mainloop()