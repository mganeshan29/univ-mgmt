#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class FeereportmodalApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.label1 = ttk.Label(self.toplevel1)
        self.label1.configure(anchor="w", font="TkTextFont", text="Roll No")
        self.label1.place(anchor="nw", relx="0.20", rely="0.1", x="0", y="0")
        self.entry1 = ttk.Entry(self.toplevel1)
        self.entry1.place(anchor="nw", relx=".30", rely=".1", x="0", y="0")
        self.label2 = ttk.Label(self.toplevel1)
        self.label2.configure(background="#d9d9d9", text="Receipt")
        self.label2.place(anchor="nw", relx="0.20", rely="0.20", x="0", y="0")
        self.entry2 = ttk.Entry(self.toplevel1)
        self.entry2.place(anchor="nw", relx=".30", rely=".2", x="0", y="0")
        self.label4 = ttk.Label(self.toplevel1)
        self.label4.configure(text="Date")
        self.label4.place(anchor="nw", relx="0.20", rely="0.30", x="0", y="0")
        self.label5 = ttk.Label(self.toplevel1)
        self.label5.configure(text="Branch")
        self.label5.place(anchor="nw", relx="0.20", rely="0.4", x="0", y="0")
        self.entry4 = ttk.Entry(self.toplevel1)
        self.entry4.place(anchor="nw", relx=".30", rely=".3", x="0", y="0")
        self.label6 = ttk.Label(self.toplevel1)
        self.label6.configure(text="Semester")
        self.label6.place(anchor="nw", relx="0.20", rely="0.50", x="0", y="0")
        self.entry5 = ttk.Entry(self.toplevel1)
        self.entry5.place(anchor="nw", relx=".30", rely=".5", x="0", y="0")
        self.label7 = ttk.Label(self.toplevel1)
        self.label7.configure(text="Total Amt")
        self.label7.place(anchor="nw", relx="0.20", rely="0.60", x="0", y="0")
        self.entry6 = ttk.Entry(self.toplevel1)
        self.entry6.place(anchor="nw", relx=".30", rely=".6", x="0", y="0")
        self.label8 = ttk.Label(self.toplevel1)
        self.label8.configure(text="Paid Amt")
        self.label8.place(anchor="nw", relx="0.20", rely="0.70", x="0", y="0")
        self.entry7 = ttk.Entry(self.toplevel1)
        self.entry7.place(anchor="nw", relx=".30", rely=".7", x="0", y="0")
        self.label9 = ttk.Label(self.toplevel1)
        self.label9.configure(text="Due Amt")
        self.label9.place(anchor="nw", relx="0.20", rely="0.80", x="0", y="0")
        self.entry8 = ttk.Entry(self.toplevel1)
        self.entry8.place(anchor="nw", relx=".30", rely=".8", x="0", y="0")
        self.entry9 = ttk.Entry(self.toplevel1)
        self.entry9.place(anchor="nw", relx=".30", rely=".4", x="0", y="0")
        self.button1 = ttk.Button(self.toplevel1)
        self.button1.configure(default="active", state="normal", text="Submit")
        self.button1.place(anchor="nw", relx=".35", rely="0.90", x="0", y="0")
        self.button2 = ttk.Button(self.toplevel1)
        self.button2.configure(text="Back")
        self.button2.place(anchor="nw", relx=".2", rely=".9", x="0", y="0")
        self.toplevel1.configure(height="200", width="200")
        self.toplevel1.geometry("800x480")
        self.toplevel1.resizable(False, False)
        self.toplevel1.title("Fee Report")

        # Main widget
        self.mainwindow = self.toplevel1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = FeereportmodalApp()
    app.run()
