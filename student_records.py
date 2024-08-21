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
 
# Run the main loop
root.mainloop()
 

# import tkinter as tk
# from tkinter import ttk
# import customtkinter as ctk
# import sqlite3
# from tkinter import messagebox
 
# def setup_student_management():
#     # Connect to the database
#     conn = sqlite3.connect('sms.db')
#     cursor = conn.cursor()
 
#     # Create table if not exists
#     cursor.execute('''CREATE TABLE IF NOT EXISTS students
#                     (student_id INTEGER PRIMARY KEY,
#                     student_name TEXT,
#                     DOB TEXT,
#                     Gender TEXT,
#                     email TEXT,
#                     phone_number TEXT,
#                     Parents_name TEXT,
#                     address TEXT)''')
#     conn.commit()
 
#     # Create and configure the tree view
#     tree = ttk.Treeview(root, columns=("ID", "Name", "DOB", "Gender", "Email", "Phone", "Parent", "Address"), show="headings")
#     for col in tree["columns"]:
#         tree.heading(col, text=col)
#         tree.column(col, width=100)
 
#     tree.pack(pady=20)
 
#     # Entry fields
#     entries = {}
#     fields = ["student_id", "student_name", "DOB", "Gender", "email", "phone_number", "Parents_name", "address"]
#     for field in fields:
#         label = ctk.CTkLabel(root, text=field)
#         label.pack()
#         entry = ctk.CTkEntry(root)
#         entry.pack()
#         entries[field] = entry
 
#     # CRUD Functions
#     def add_student():
#         values = [entries[field].get() for field in fields]
#         cursor.execute('''INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', values)
#         conn.commit()
#         messagebox.showinfo("Success", "Student added successfully!")
#         refresh_tree()
 
#     def update_student():
#         values = [entries[field].get() for field in fields]
#         cursor.execute('''UPDATE students SET student_name=?, DOB=?, Gender=?, email=?, 
#                         phone_number=?, Parents_name=?, address=? WHERE student_id=?''', 
#                         values[1:] + [values[0]])
#         conn.commit()
#         messagebox.showinfo("Success", "Student updated successfully!")
#         refresh_tree()
 
#     def delete_student():
#         student_id = entries['student_id'].get()
#         cursor.execute("DELETE FROM students WHERE student_id=?", (student_id,))
#         conn.commit()
#         messagebox.showinfo("Success", "Student deleted successfully!")
#         refresh_tree()
 
#     def search_student():
#         email = entries['email'].get()
#         cursor.execute("SELECT * FROM students WHERE email=?", (email,))
#         result = cursor.fetchone()
#         if result:
#             for i, field in enumerate(fields):
#                 entries[field].delete(0, tk.END)
#                 entries[field].insert(0, result[i])
#             messagebox.showinfo("Success", "Student found!")
#         else:
#             messagebox.showinfo("Not Found", "No student found with this email.")
 
#     def refresh_tree():
#         for item in tree.get_children():
#             tree.delete(item)
#         cursor.execute("SELECT * FROM students")
#         for row in cursor.fetchall():
#             tree.insert("", "end", values=row)
 
#     # Buttons
#     add_btn = ctk.CTkButton(root, text="Add", command=add_student)
#     update_btn = ctk.CTkButton(root, text="Update", command=update_student)
#     delete_btn = ctk.CTkButton(root, text="Delete", command=delete_student)
#     search_btn = ctk.CTkButton(root, text="Search", command=search_student)
#     refresh_btn = ctk.CTkButton(root, text="Refresh", command=refresh_tree)
 
#     add_btn.pack(pady=5)
#     update_btn.pack(pady=5)
#     delete_btn.pack(pady=5)
#     search_btn.pack(pady=5)
#     refresh_btn.pack(pady=5)
 
#     refresh_tree()
 
#     return conn, cursor
 
# # Usage
# root = tk.Tk()
# root.title("Student Management System")
# conn, cursor = setup_student_management()
# root.mainloop()
 
# # Don't forget to close the connection when the application exits
# conn.close()
 

 
 

 