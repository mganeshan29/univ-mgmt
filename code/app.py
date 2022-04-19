import tkinter as tk
import tkinter.ttk as ttk
from .components.login_page import login_page
from .helper import constants as const


class Application:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.title("University Management System")
        canvas1 = tk.Canvas(self.toplevel1)
        canvas1.configure(background='white', height='350', width='300')
        canvas1.pack(side='top')
        
        Header = tk.Message(self.toplevel1)
        Header.configure(background='#ca0a4a', foreground='white' ,text='Welcome!!', width='100')
        Header.place(anchor='nw', relheight='0.25', relwidth='1.0', x='0', y='0')
        
        identity_label = ttk.Label(self.toplevel1)
        identity_label.configure(text='You are',background = 'white')
        identity_label.place(anchor='nw', relx='0.11', rely='0.32', x='0', y='0')
        
        faculty_button = tk.Button(self.toplevel1, command = lambda:self.openLogin(roleLogin = const.FACULTY_ROLE), activebackground = "#a2083b", activeforeground = "white")
        faculty_button.configure(text='faculty', background = "#ca0a4a",foreground = "black")
        faculty_button.place(anchor='nw', relheight='0.12', relwidth='0.8', relx='0.1', rely='0.47', x='0', y='0')
        
        student_button = tk.Button(self.toplevel1, command = lambda:self.openLogin(roleLogin = const.STUDENT_ROLE), activebackground = "#a2083b", activeforeground = "white")
        student_button.configure(text='Student', background = "#ca0a4a",foreground = "black")
        student_button.place(anchor='nw', relheight='0.12', relwidth='0.8', relx='0.1', rely='0.77', x='0', y='0')
        
        or_label = ttk.Label(self.toplevel1)
        or_label.configure(text='OR', background = 'white')
        or_label.place(anchor='nw', relx='0.47', rely='0.65', x='0', y='0')
        
        self.toplevel1.configure(height='200', width='200')
        # Main widget
        self.mainwindow = self.toplevel1
        
    def openLogin(self,roleLogin):
      self.toplevel1.destroy()
      login_page.LoginPage(role = roleLogin)
    
    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    app = Application()
    app.run()

