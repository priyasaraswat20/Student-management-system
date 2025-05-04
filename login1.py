from tkinter import*
from tkinter import messagebox
def login():
  if usernameEntry.get()=='' or passwordEntry.get()=='':
      messagebox.showerror('Error','Fields cannot be empty')
  elif usernameEntry.get()=='priya' and passwordEntry.get()=='1234':
      messagebox.showinfo('Success','Welcome')
      window.destroy()
      import sms
  else:
      messagebox.showinfo('Error','please enter correct credentials')
window=Tk()
window.geometry('1280x700+0+0')
window.title('Login System of Management System')
window.resizable(False,False)
backgroundImage=PhotoImage(file='bg.png')
bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)
loginFrame=Frame(window,bg='white')
loginFrame.place(x=500,y=200)
logoImage=PhotoImage(file='logo.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
usernameImage=PhotoImage(file='')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)
usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5)
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordImage=PhotoImage(file='')
passwordLabel=Label(loginFrame,image=passwordImage,text='password',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)
passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5)
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=15,fg='white',bg='cornflowerblue',cursor='hand2',command=login)
loginButton.grid(row=3,column=1)

window.mainloop()