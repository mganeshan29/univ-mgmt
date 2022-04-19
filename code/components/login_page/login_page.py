import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as msg
from PIL import Image, ImageTk

from ...app import Application
from ...models.Faculty import Faculty
from ...models.Student import Student
from ..dashboard import dashboard
from ...helper import constants as const

class LoginPage:
    def __init__(self, master=None, role = const.STUDENT_ROLE):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.title("University Management System")
        
        login_container = tk.Canvas(self.toplevel1)
        login_container.configure(height='300', takefocus=False, width='600')
        login_container.pack(side='top')
        
        #fonts
        self.header_font = font.Font(family="Raleway", size=13, weight="bold")
        self.label_font = font.Font(family="Raleway", size=10, weight = "bold")
        self.text_font = font.Font(family="Raleway",size = 10)
        
        # #Image
        image = Image.open("code/images/College.jpeg")
        image = image.resize((300,300), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        image_label = ttk.Label(image = image)
        image_label.image = image
        image_label.place(relheight='1.0', relwidth='0.5', x='0', y='0')
        
        #LoginHeader
        login_header = tk.Message(self.toplevel1)
        login_header.configure(font = self.header_font, background='#ca0a4a', foreground='white', text='Login System', width='200')
        login_header.place(anchor='nw', relheight='0.20', relwidth='0.50', relx='0.50', rely='0.0', x='0', y='0')
        
        #NameEntry and message
        name_entry = ttk.Entry(self.toplevel1, font = self.text_font)
        name_entry.place(anchor='nw', height='19', relheight='0.0', relwidth='0.27', relx='0.68', rely='0.35', x='0', y='0')
        name_message = tk.Message(self.toplevel1)
        if(role == const.STUDENT_ROLE):
            enter_text = "Enter Roll No."
        elif (role == const.FACULTY_ROLE):
            enter_text = "Enter ID: "
        name_message.configure(text=enter_text,font = self.label_font, width='100')
        name_message.place(anchor='nw', relx='0.53', rely='0.35', x='0', y='0')
        
        #PasswordEnter and Message
        password_entry = ttk.Entry(self.toplevel1,font = self.text_font, show = "*")
        password_entry.place(anchor='nw', height='19', relheight='0.0', relwidth='0.27', relx='0.68', rely='0.53', x='0', y='0')
        password_message = tk.Message(self.toplevel1)
        password_message.configure(text='Password:',font = self.label_font, width='100')
        password_message.place(anchor='nw', relx='0.53', rely='0.53', x='0', y='0')
        
        #Login_Button and Cancel Button
        login_button = tk.Button(self.toplevel1,command = lambda:self.openDashboard(username = name_entry.get(), password = password_entry.get(), role = role))
        login_button.configure(text='Login', font = self.text_font, bg = "#ca0a4a", fg = "white", activebackground = "#C1174b")
        login_button.place(anchor='nw', height='30', relx='0.55', rely='0.7', width='250', x='0', y='0')
        
        cancel_button = tk.Button(self.toplevel1, command = lambda:self.goBack())
        cancel_button.configure(text='Cancel',font = self.text_font, bg = "white")
        cancel_button.place(anchor='nw', height='30', relx='0.55', rely='0.85', width='250', x='0', y='0')
        self.toplevel1.configure(height='200', width='200')

        # Main widget
        self.mainwindow = self.toplevel1
    
    def goBack(self):
        self.toplevel1.destroy()
        Application()

    def openDashboard(self, username = "", password = "", role = const.STUDENT_ROLE):
        if(role == const.STUDENT_ROLE):
            student = Student()
            s = student.authenticate(username, password)
            if s:
                print(s["rollNo"]+ " is Authenticated")
                self.toplevel1.destroy()
                dashboard.DashBoard(role = const.STUDENT_ROLE, title = s["name"], id = s['rollNo'])
                # dashboard.DashBoard(role="Student", rollNo=s["rollNo"])
            else:
                # msg.showinfo("Auth Error", "Enter the correct username and password")
                print("Invalid Credentials")
        elif(role == const.FACULTY_ROLE):
            faculty = Faculty()
            f = faculty.authenticate(username, password)
            if f:
                print(f["id"]+ " is Authenticated")
                self.toplevel1.destroy()
                dashboard.DashBoard(role=const.FACULTY_ROLE, id=f["id"], title = f['name'])
            else:
                msg.showinfo("Auth Error", "Enter the correct username and password")

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    app = LoginPage()
    app.run()
