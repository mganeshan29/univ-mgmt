import tkinter as tk
import tkinter.ttk as ttk

from ...models.FeeReport import FeeReport

class FeeReportTable:
  def __init__(self, master):
      self.root = master
      
      search_label = tk.Label(self.root, text = "Search:")
      search_label.place(anchor = "nw", rely = "0.33", relx = "0.64")
      
      self.search_entry = tk.Entry(self.root)
      self.search_entry.place(anchor = "nw", relx = '0.71', rely = '0.33')
      
      search_button = tk.Button(self.root, text = "Search", command = self.search)
      search_button.place(anchor="nw",  relx = '0.9', rely = '0.322')
      
      clear_search_button = tk.Button(self.root, text = "Clear", command = self.clear)
      clear_search_button.place(anchor="nw",  relx = '0.9', rely = '0.372')
      
      delete_button = tk.Button(self.root, text = "Delete", command = self.delete)
      delete_button.place(anchor="nw",  relx = '0.6', rely = '0.372')
      
 
      self.trv = ttk.Treeview(self.root, columns = (1,2,3,4,5,6,7,8), show = "headings", height = "6")
      self.trv.place(anchor='nw', height='45', rely='0.6',relwidth= "1", relheight = "0.4", x='0', y='0')
      
      self.s = FeeReport()
      rows = self.s.selectAll()
      
      self.trv.column("#0", width = 100, minwidth = 25)
      for i in range(1,9):
        self.trv.column(i , width = 100, minwidth = 25)

      self.trv.heading(1, text = "Roll No")
      self.trv.heading(2, text = "Receipt")
      self.trv.heading(3,  text = "Date")
      self.trv.heading(4, text = "Branch")
      self.trv.heading(5, text = "Semester")
      self.trv.heading(6, text = "Total Amount")
      self.trv.heading(7, text = "Paid Amount")
      self.trv.heading(8, text = "Due Amount")
      
      self.trv.bind('<Double 1>', self.getrow)
      
      self.updateTable(rows)
          
  def updateTable(self,rows):
    self.trv.delete(*self.trv.get_children())
    for i in rows:
      self.trv.insert(parent = '', index = 'end', values = i)
  
  def search(self):
    q = self.search_entry.get()
    if q[0] == 'r':
      rows = self.s.selectReceipt(q)
    else:
      rows = self.s.select(q)
    self.updateTable(rows)
    
  def clear(self):
    rows = self.s.selectAll()
    self.updateTable(rows)
    
  def getrow(self,event):
    rowId = self.trv.identify_row(event.y)
    item = self.trv.item(self.trv.focus())
    self.receipt = item['values'][1]
  
  def delete(self):
    self.s.deleteReceipt(self.receipt)
    rows = self.s.selectAll()
    self.updateTable(rows)
  
  
                          
            