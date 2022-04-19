import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font
from PIL import Image, ImageTk

from ...helper import constants as const
from ..login_page import login_page as LP

class DashBoard:
    def __init__(self, title='', master=None, role = const.STUDENT_ROLE):
        if (role == const.STUDENT_ROLE):
            self.title = title
            # build ui
            self.root = tk.Tk() if master is None else tk.Toplevel(master)
            self.root.title("University Management System")

            canvas1 = tk.Canvas(self.root)
            canvas1.configure(background='white', height='600', width='800')
            canvas1.pack(side='top')

            self.header_font = font.Font(family="Raleway", size=13, weight="bold")
            self.button_font = font.Font(family="Raleway", size=10, weight="bold")

            lib_image = Image.open("code/images/Library.png")
            lib_image = lib_image.resize((188, 188), Image.ANTIALIAS)
            lib_image = ImageTk.PhotoImage(image=lib_image)

            fee_image = Image.open("code/images/FeeReport.png")
            fee_image = fee_image.resize((188, 188), Image.ANTIALIAS)
            fee_image = ImageTk.PhotoImage(image=fee_image)

            mark_image = Image.open("code/images/MarkSheet.png")
            mark_image = mark_image.resize((188, 188), Image.ANTIALIAS)
            mark_image = ImageTk.PhotoImage(image=mark_image)
            
            profile_image = Image.open("code/images/viewProfile.png")
            profile_image = profile_image.resize((188, 188), Image.ANTIALIAS)
            profile_image = ImageTk.PhotoImage(image=profile_image)
            
            logOut_image = Image.open("code/images/LogingOut.png")
            logOut_image = logOut_image.resize((188, 188), Image.ANTIALIAS)
            logOut_image = ImageTk.PhotoImage(image=logOut_image)

            page_header = ttk.Label(self.root)
            page_header.configure(background='#ca0a4a')
            page_header.place(anchor='nw', height='100', width='800', x='0', y='0')

            dash_layer1 = ttk.Label(self.root)
            dash_layer1.configure(background='white')
            dash_layer1.place(anchor='nw', height='100', relx='0.31',
                            rely='0.08', width='300', x='0', y='0')
            dash_layer2 = ttk.Label(self.root)
            dash_layer2.configure(background='#ca0a4a')
            dash_layer2.place(anchor='nw', height='90', relx='0.317',
                            rely='0.09', width='290', x='0', y='0')
            dash_message = tk.Message(self.root, font=self.header_font)
            dash_message.configure(
                background='white', foreground='#ca0a4a', text='Welcome '+self.title, width='200')
            dash_message.place(anchor='nw', height='80', relx='0.323',
                            rely='0.10', width='280', x='0', y='0')

            mark_button = tk.Button(self.root, bg="white", image=mark_image)
            mark_button.image = mark_image
            mark_button.place(anchor='nw', height='188', relx='0.05',
                            rely='0.27', width='188', x='0', y='0')

            library_button = tk.Button(self.root, bg="white", image=lib_image)
            library_button.image = lib_image
            library_button.place(anchor='nw', height='188',
                                relx='0.38', rely='0.27', width='188', x='0', y='0')

            fee_button = tk.Button(self.root, bg="white", image=fee_image)
            fee_button.image = fee_image
            fee_button.place(anchor='nw', height='188', relx='0.7',
                            rely='0.27', width='188', x='0', y='0')
            
            profile_button = tk.Button(self.root, bg="white", image=profile_image)
            profile_button.image = profile_image
            profile_button.place(anchor='nw', height='188', relx='0.05',
                            rely='0.65', width='188', x='0', y='0')
            
            logout_button = tk.Button(self.root, bg="white", image=logOut_image, command=self.logout)
            logout_button.image = logOut_image
            logout_button.place(anchor='nw', height='188', relx='0.38',
                            rely='0.65', width='188', x='0', y='0')

            self.root.configure(height='200', width='200')
            self.root.mainloop()

    def logout(self):
        self.root.destroy()
        LP.LoginPage()
