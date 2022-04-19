import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font
from PIL import Image, ImageTk

from ..dashboard import dashboard
from ...helper import constants as const
from ..login_page import login_page as lp


class mainWidget:
    def __init__(self, id, mainType, title, master=None, role = const.STUDENT_ROLE):
        # build ui
        self.root = master
        self.id = id
        self.role = role
        self.title = title
        
        logout_image = Image.open("code/images/LogOut.png")
        logout_image = logout_image.resize((40, 40), Image.ANTIALIAS)
        logout_image = ImageTk.PhotoImage(image=logout_image)
        
        previous_image = Image.open("code/images/previous.png")
        previous_image = previous_image.resize((40, 40), Image.ANTIALIAS)
        previous_image = ImageTk.PhotoImage(image=previous_image)
        
        
        self.canvas1 = tk.Canvas(self.root)
        self.canvas1.configure(background='white', height='600', relief='flat', width='800')
        self.canvas1.pack(side='top')
        
        
        self.header_font = font.Font(family="Raleway", size=13, weight="bold")
        self.label_font = font.Font(family="Raleway", size=10, weight = "bold")
        
        page_header = ttk.Label(self.root)
        page_header.configure(background='#ca0a4a')
        page_header.place(anchor='nw', height='120', width='800', x='0', y='0')

        
        dash_layer1 = ttk.Label(self.root)
        dash_layer1.configure(background='white')
        dash_layer1.place(anchor='nw', height='80', relx='0.31',
                          rely='0.04', width='270', x='0', y='0')
        dash_layer2 = ttk.Label(self.root)
        dash_layer2.configure(background='#ca0a4a')
        dash_layer2.place(anchor='nw', height='70', relx='0.317',
                          rely='0.05', width='260', x='0', y='0')
        
        dash_message = tk.Message(self.root)
        dash_message.configure(background='white', foreground='#ca0a4a',font = self.header_font, text=mainType, width='200')
        dash_message.place(anchor='nw', height='63', relx='0.322',
                           rely='0.057', width='253', x='0', y='0')
        
        x='0';y='0.2'
        
        if(mainType != "Fee Report"):
            fee_button = tk.Button(self.root, command = self.onOpenFeeReport)
            fee_button.configure(text='Fee Report', width='11',font = self.label_font, activebackground = "#cf235c", activeforeground = "white", fg = "white", bg = "#ca0a4a",bd = '2', highlightthickness= 0)
            fee_button.place(anchor='nw', height='45', rely='0.2', x='0', y='0')
            
        if(mainType != "Marksheet") :
            mark_button = tk.Button(self.root, command = self.onOpenMarks)
            mark_button.configure(text='Marksheet', width='11',font = self.label_font, activebackground = "#cf235c", activeforeground = "white", fg = "white",  bg = "#ca0a4a",bd = '2', highlightthickness= 0)
            mark_button.place(anchor='nw', height='45', relx='0.13', rely='0.2', x='0', y='0')
        else:
            x='0.13';y='0.2'
            
            
        if(mainType != "Library"):
            lib_button = tk.Button(self.root, command = self.onOpenLibrary)
            lib_button.configure(text='Library', width='11',font = self.label_font, activebackground = "#cf235c", activeforeground = "white", fg = "white",  bg = "#ca0a4a",bd = '2', highlightthickness= 0)
            lib_button.place(anchor='nw', height='45', relx='0.26', rely='0.2', x='0', y='0')
        else:
            x='0.26';y='0.2'
            
            
        if(mainType != "Profile"):
            profile_button = tk.Button(self.root, command = self.onOpenProfile)
            profile_button.configure(text='Profile', width='11',font = self.label_font, activebackground = "#cf235c", activeforeground = "white", fg = "white", bg = "#ca0a4a",bd = '2', highlightthickness= 0)
            profile_button.place(anchor='nw', height='45', relx='0.38', rely='0.2', x='0', y='0')
        else:
            x='0.38';y='0.2'
            
        active_button = tk.Button(self.root)
        active_button.configure(text=mainType, width='11',font = self.label_font, activebackground = "#d38a92", activeforeground ="#ca0a4a", bg = "#ea99a2", fg = "#ca0a4a",bd = '2', highlightthickness= 0)
        active_button.place(anchor='nw', height='45', relx=x, rely=y, x='0', y='0')
        
        logout_button = tk.Button(self.root,command = self.logout, bd = 0,highlightthickness=0,activebackground="#ca0a4a",bg="#ca0a4a", image=logout_image)
        logout_button.image = logout_image
        logout_button.place(anchor="nw", relx="0.9",
                            rely="0.055", x="0", y='0')
        
        previous_button = tk.Button(self.root,command = self.onOpenDashboard, bd = 0,highlightthickness=0,activebackground="#ca0a4a",bg="#ca0a4a", image=previous_image)
        previous_button.image = previous_image
        previous_button.place(anchor="nw", relx="0.04",
                            rely="0.055", x="0", y='0')
        
        self.root.configure(height='200', width='200')
        
        
    def logout(self):
        self.root.destroy()
        lp.LoginPage("Student")
        
        
    def onOpenProfile(self):
        self.canvas1.destroy()
        mainWidget(mainType = "Profile", master = self.root, id = self.id, title = self.title)    
        
    def onOpenLibrary(self):
        self.canvas1.destroy()
        mainWidget(mainType = "Library", master = self.root, id = self.id, title = self.title)
        
    def onOpenFeeReport(self):
        self.canvas1.destroy()
        mainWidget(mainType = "Fee Report", master = self.root, id = self.id, title = self.title)
    
    def onOpenMarks(self):
        self.canvas1.destroy()
        mainWidget(mainType = "Marksheet", master = self.root, id = self.id, title = self.title)
            
    def onOpenDashboard(self):
        self.root.destroy()
        dashboard.DashBoard(role = self.role, title = self.title, id = self.id)
        
        



