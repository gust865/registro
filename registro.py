
# Let's import tkinter 
from tkinter import *
#import tkinter as tk
 
# Manipulate data from registration fields 
def send_data():
  username_info = username.get()
  password_info = password.get()
  email_info = email.get()
  age_info = str(age.get())
  print(username_info,"\t", password_info,"\t", email_info,"\t", age_info)
 
#  Open and write data to a file
  file = open(r"C:\Users\gusta\OneDrive\Escritorio\registro\user.txt", "a+")
  file.write(username_info)
  file.write("\t")
  file.write(password_info)
  file.write("\t")
  file.write(email_info)
  file.write("\t")
  file.write(age_info)
  file.write("\t\n")
  file.close()
  print(" Nuevo usuario registrado. Username: {} | email: {}   ".format(username_info, email_info))
 
#  Delete data from previous event
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  email_entry.delete(0, END)
  age_entry.delete(0, END)

# Create new instance - Class Tk()  
mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("Registro formulario - Python + Tkinter")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = Label(text = "Welcome ", font = ("Cambria", 18), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()

# Define Label Fields 
username_label = Label(text = "Username", bg = "#FFEEDD")
username_label.place(x = 22, y = 70)
password_label = Label(text = "Password", bg = "#FFEEDD")
password_label.place(x = 22, y = 130)
email_label = Label(text = "Email", bg = "#FFEEDD")
email_label.place(x = 22, y = 190)
age_label = Label(text = "Age", bg = "#FFEEDD")
age_label.place(x = 22, y = 250)
 
# Get and store data from users 
username = StringVar()
password = StringVar()
email = StringVar()
age = StringVar()
 
username_entry = Entry(textvariable = username, width = "40")
password_entry = Entry(textvariable = password, width = "40",  show = "*")
email_entry = Entry(textvariable = email, width = "40")
age_entry = Entry(textvariable = age, width = "40")
 
username_entry.place(x = 22, y = 100)
password_entry.place(x = 22, y = 160)
email_entry.place(x = 22, y = 220)
age_entry.place(x = 22, y = 280)
 
# Login Button
Login_btn = Button(mywindow,text = "Login", width = "30", height = "2", command = send_data, bg = "#00CD63")
Login_btn.place(x = 22, y = 320)

mywindow.mainloop()