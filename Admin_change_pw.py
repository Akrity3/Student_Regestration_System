#######~~~~~ADMIN_DASHBOARD~~~~~~############

from tkinter import *
from customtkinter import *
from tkinter import messagebox
import sqlite3
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

# def checking():
#  if cpw_etr.get() == '' or npw_etr.get() == '' or asec_entry3.get() == '':
#             tk.messagebox.showerror("Error","All fields are required.")
#  elif (cpw_etr.get()).isdigit() == False:
#             tk.messagebox.showerror("Error","Entered value must be a number.")
#  if cpw_etr.get() == admin_data[4] and npw_etr.get() == admin_data[5] and asec_entry3.get() == admin_data[6]:
#             global ulogin_etr2,areset_pass_frame,alogin_etr1,alogin_etr2,areset_pass_main_frame
#             asign_sec_qsn_frame.place_forget()
# pass


#Left Top Frame:
ad_dashb_fr1 = CTkFrame(root,fg_color="#2C87CF",bg_color="#0D336B",width=530, height=100,corner_radius=10)
ad_dashb_fr1.place(x=20,y=25)

#Label:
ad_dash_lbl = CTkLabel(ad_dashb_fr1,text="ADMIN  DASHBOARD",text_color="#FFFFFF",fg_color="#2C87CF",font=("Times New Roman",35,"bold"))  #Label of title in top frame
ad_dash_lbl.place(x=60,y=25)


#Left Bottom Frame:
ad_dashb_fr2 = CTkFrame(root,fg_color="#2C87CF",bg_color="#0D336B",width=530, height=525,corner_radius=10)
ad_dashb_fr2.place(x=20,y=145)



def gotorecord():
   root.destroy()
   pass
#Button:

std_rd_btn = CTkButton(ad_dashb_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" Student Records ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10, command = gotorecord) #Student records button 
std_rd_btn.place(x=60,y=120)

# my_crs_btn = CTkButton(ad_dashb_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" My Courses ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Student records button 
# my_crs_btn.place(x=60,y=120)

# ntc_brd_btn = CTkButton(ad_dashb_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" Notice Board ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Student records button 
# ntc_brd_btn.place(x=60,y=210)

cng_pw_btn = CTkButton(ad_dashb_fr2,hover_color="#0D336B",fg_color="#0D3380",text=" Change Password ",font=("Times New Roman", 20, "bold"),bg_color="#2C87CF",width=400,height=50,corner_radius=10) #Student records button 
cng_pw_btn.place(x=60,y=250)


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

cpw_lbl = CTkLabel(ad_dashb_fr4,text="Enter Your Current Password",text_color="white",font=("Times New Roman",16) ,fg_color="#0F56A2")
cpw_lbl.place(x=45,y=110)

npw_lbl = CTkLabel(ad_dashb_fr4,text="Enter Your New Password",text_color="white",font=("Times New Roman",16) ,fg_color="#0F56A2")
npw_lbl.place(x=45,y=200)

cn_pw_lbl = CTkLabel(ad_dashb_fr4,text="Confirm Your New Password",text_color="white",font=("Times New Roman",16) ,fg_color="#0F56A2")
cn_pw_lbl.place(x=45,y=290)


#adding entry:
cpw_etr = CTkEntry(ad_dashb_fr4,corner_radius=12,height=38,width=240,border_width=0,fg_color="white",text_color="black",placeholder_text="Current Password",placeholder_text_color="grey",show="*")  
cpw_etr.place(x=45,y=150)

npw_etr = CTkEntry(ad_dashb_fr4,corner_radius=12,height=38,width=240,border_width=0,fg_color="white",text_color="black",placeholder_text="New Password",placeholder_text_color="grey", show='*')  
npw_etr.place(x=45,y=240)

cn_pw_etr = CTkEntry(ad_dashb_fr4,corner_radius=12,height=38,width=240,border_width=0,fg_color="white",text_color="black",placeholder_text="Type Your New Password",placeholder_text_color="grey", show='*')
cn_pw_etr.place(x=45,y=330)



#-------------------------------------------------------------------------------------------------------------------#
def backend():
   conn = sqlite3.connect('sms.db')
   c = conn.cursor()
   c.execute('SELECT password FROM admin')
   passwords = c.fetchall()
   conn.close()
   if cpw_etr.get() == '' or npw_etr.get() == '' or cn_pw_etr.get() == '':
      messagebox.showerror('Error', 'Please enter all fields! ')
   elif len(npw_etr.get()) < 8 :
      messagebox.showerror('Error', 'Password must be of 8 characters!')
   elif npw_etr.get() != cn_pw_etr.get():
      messagebox.showerror('Error', 'passwords did not match!')
   else:
      if passwords is not None:
         conn = sqlite3.connect('sms.db')
         c = conn.cursor()
         c.execute('UPDATE admin SET password = ? WHERE password = ?',(npw_etr.get(), cpw_etr.get()))
         messagebox.showinfo('Success', 'Password changed successfully!')
         conn.commit()
         conn.close()
         root.destroy()
         import Main_page
      else:
         messagebox.showerror('Error', 'password did not match with the existing password !')
         
      
      
   
      
      

   
   
#-------------------------------------------------------------------------------------------------------------------#


#Button:
submit_btn = CTkButton(ad_dashb_fr4,hover_color="#0D336B",fg_color="#1792F3",text=" Submit ",font=("Times New Roman", 19, "bold"),bg_color="#0F56A2",width=100,height=40,corner_radius=9, command = backend) #Submit button
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



root.mainloop()