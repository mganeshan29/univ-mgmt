import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font
from PIL import Image, ImageTk


class DashBoard:
    def __init__(self, master=None):
        # build ui
        root = tk.Tk() if master is None else tk.Toplevel(master)
        root.title("University Management System")

        canvas1 = tk.Canvas(root)
        canvas1.configure(background='white', height='500', width='800')
        canvas1.pack(side='top')
        
        self.header_font = font.Font(family = "Raleway", size = 13, weight = "bold")
        self.button_font = font.Font(family = "Raleway", size = 10, weight = "bold")
        

        lib_image = Image.open("code/images/Library.png")
        lib_image = lib_image.resize((210, 245), Image.ANTIALIAS)
        lib_image = ImageTk.PhotoImage(image=lib_image)

        fee_image = Image.open("code/images/FeeReport.png")
        fee_image = fee_image.resize((210, 245), Image.ANTIALIAS)
        fee_image = ImageTk.PhotoImage(image=fee_image)

        mark_image = Image.open("code/images/MarkSheet.png")
        mark_image = mark_image.resize((210, 245), Image.ANTIALIAS)
        mark_image = ImageTk.PhotoImage(image=mark_image)

        logout_image = Image.open("code/images/LogOut.png")
        logout_image = logout_image.resize((40, 40), Image.ANTIALIAS)
        logout_image = ImageTk.PhotoImage(image=logout_image)

        page_header = ttk.Label(root)
        page_header.configure(background='#ca0a4a')
        page_header.place(anchor='nw', height='100', width='800', x='0', y='0')

        dash_layer1 = ttk.Label(root)
        dash_layer1.configure(background='white')
        dash_layer1.place(anchor='nw', height='100', relx='0.25',
                          rely='0.1', width='300', x='0', y='0')
        dash_layer2 = ttk.Label(root)
        dash_layer2.configure(background='#ca0a4a')
        dash_layer2.place(anchor='nw', height='90', relx='0.257',
                          rely='0.11', width='290', x='0', y='0')
        dash_message = tk.Message(root, font = self.header_font)
        dash_message.configure(
            background='white', foreground='#ca0a4a', text='Dashboard', width='200')
        dash_message.place(anchor='nw', height='80', relx='0.263',
                           rely='0.12', width='280', x='0', y='0')

        profile_button = tk.Button(root, font = self.button_font, bg="white", fg="#ca0a4a")
        profile_button.configure(text='View Profile')
        profile_button.place(anchor='nw', height='40',
                             relx='0.7', rely='0.055', width='130', x='0', y='0')

        mark_button = tk.Button(root, bg="white", image=mark_image)
        mark_button.image = mark_image
        mark_button.place(anchor='nw', height='250', relx='0.05',
                          rely='0.37', width='210', x='0', y='0')

        library_button = tk.Button(root, bg="white", image=lib_image)
        library_button.image = lib_image
        library_button.place(anchor='nw', height='250',
                             relx='0.38', rely='0.37', width='210', x='0', y='0')

        fee_button = tk.Button(root, bg="white", image=fee_image)
        fee_button.image = fee_image
        fee_button.place(anchor='nw', height='250', relx='0.7',
                         rely='0.37', width='210', x='0', y='0')

        logout_button = tk.Button(root,bd = 0,highlightthickness=0,activebackground="#ca0a4a",bg="#ca0a4a", image=logout_image)
        logout_button.image = logout_image
        logout_button.place(anchor="nw", relx="0.9",
                            rely="0.055", x="0", y='0')

        root.configure(height='200', width='200')

        root.mainloop()
