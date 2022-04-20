#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from ...models.Book import Book

class AddBookModal:
    def __init__(self, master=None):
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.title("Add Book")
        self.canvas1 = tk.Canvas(self.toplevel1)
        self.canvas1.configure(height="400", width="380")
        self.canvas1.pack(side="top")
        self.entry1 = ttk.Entry(self.toplevel1)
        self.entry1.place(anchor="nw", relx="0.280", rely="0.14", x="0", y="0")
        self.label1 = ttk.Label(self.toplevel1)
        self.label1.configure(text="Title: ")
        self.label1.place(anchor="nw", relx="0.05", rely="0.14", x="0", y="0")
        self.label2 = ttk.Label(self.toplevel1)
        self.label2.configure(compound="right", cursor="arrow", text="Author: ")
        self.label2.place(anchor="nw", relx="0.05", rely="0.23", x="0", y="0")
        self.entry2 = ttk.Entry(self.toplevel1)
        self.entry2.place(anchor="nw", relx="0.28", rely="0.23", x="0", y="0")
        self.entry3 = ttk.Entry(self.toplevel1)
        self.entry3.place(anchor="nw", relx="0.28", rely="0.32", x="0", y="0")
        self.label3 = ttk.Label(self.toplevel1)
        self.label3.configure(compound="center", cursor="arrow", text="ID: ")
        self.label3.place(anchor="nw", relx="0.05", rely="0.32", x="0", y="0")
        self.entry4 = ttk.Entry(self.toplevel1)
        self.entry4.place(anchor="nw", relx="0.28", rely="0.41", x="0", y="0")
        self.label4 = ttk.Label(self.toplevel1)
        self.label4.configure(compound="center", cursor="arrow", text="Publisher: ")
        self.label4.place(anchor="nw", relx="0.05", rely="0.50", x="0", y="0")
        self.entry5 = ttk.Entry(self.toplevel1)
        self.entry5.place(anchor="nw", relx="0.28", rely="0.50", x="0", y="0")
        self.label5 = ttk.Label(self.toplevel1)
        self.label5.configure(
            compound="center", cursor="arrow", font="TkDefaultFont", text="Edition: "
        )
        self.label5.place(anchor="nw", relx="0.05", rely="0.41", x="0", y="0")
        self.entry6 = ttk.Entry(self.toplevel1)
        self.entry6.place(anchor="nw", relx="0.28", rely="0.59", x="0", y="0")
        self.label6 = ttk.Label(self.toplevel1)
        self.label6.configure(compound="center", cursor="arrow", text="PublishDate: ")
        self.label6.place(anchor="nw", relx="0.05", rely="0.59", x="0", y="0")
        self.label7 = ttk.Label(self.toplevel1)
        self.label7.place(anchor="nw", relx="0.3", rely="0.05", x="0", y="0")
        self.toplevel1.configure(height="200", width="200")

        self.button1 = ttk.Button(self.toplevel1, command = self.insertBook)
        self.button1.configure(text="Submit")
        self.button1.place(anchor="nw", relx="0.13", rely="0.75", x="0", y="0")

        self.button2 = ttk.Button(self.toplevel1, command=self.goBack)
        self.button2.configure(text="Back")
        self.button2.place(anchor="nw", relx="0.42", rely="0.75", x="0", y="0")

        # Main widget
        self.mainwindow = self.toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def goBack(self):
        self.toplevel1.destroy()
    
    def insertBook(self):
        entries = [self.entry1, self.entry2, self.entry3, self.entry4, self.entry5, self.entry6]
        title = self.entry1.get()
        author = self.entry2.get()
        id = self.entry3.get()
        edition = self.entry4.get()
        publisher = self.entry5.get()
        publishDate = self.entry6.get()

        # Insert book into database
        b = Book(title = title, author = author, id = id, edition = edition, publisher = publisher, publishDate = publishDate)
        b.insert()
        print(b, end="")
        print(" Insertion successful")
        self.label7.configure(text = str(b) + " Insertion successful")

        for i in entries: 
            i.delete(0, 'end')

if __name__ == "__main__":  
    app = AddBookModal()
    app.run()
