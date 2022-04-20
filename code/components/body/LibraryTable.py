import tkinter as tk
import tkinter.ttk as ttk

from ..modals.AddBookModal import AddBookModal
from ...models.Book import Book

class LibraryTable:
  def __init__(self, master):
      self.root = master
      
    #   search_label = tk.Label(self.root, text = "Search:")
    #   search_label.place(anchor = "nw", rely = "0.33", relx = "0.64")
      
    #   self.search_entry = tk.Entry(self.root)
    #   self.search_entry.place(anchor = "nw", relx = '0.71', rely = '0.33')
      
      add_book = tk.Button(self.root, text = "Add Book", command = self.addBook)
      add_book.place(anchor="nw",  relx = '0.75', rely = '0.22')
      
    #   clear_search_button = tk.Button(self.root, text = "Clear", command = self.clear)
    #   clear_search_button.place(anchor="nw",  relx = '0.9', rely = '0.372')
      
    #   delete_button = tk.Button(self.root, text = "Delete", command = self.delete)
    #   delete_button.place(anchor="nw",  relx = '0.6', rely = '0.372')
      
 
      self.trv = ttk.Treeview(self.root, columns = (1,2,3,4,5,6), show = "headings", height = "6")
      self.trv.place(anchor='nw', height='45', rely='0.6',relwidth= "1", relheight = "0.4", x='0', y='0')
      
      self.s = Book()
      rows = self.s.selectAll()
      
      self.trv.column("#0", width = 100, minwidth = 25)
      for i in range(1,7):
        self.trv.column(i , width = 100, minwidth = 25)

      self.trv.heading(1, text = "Title")
      self.trv.heading(2, text = "Author")
      self.trv.heading(3,  text = "ID")
      self.trv.heading(4, text = "Edition")
      self.trv.heading(5, text = "Publisher")
      self.trv.heading(6, text = "Publish Date")
      
      self.trv.bind('<Double 1>', self.getrow)
      
      self.updateTable(rows)
          
  def updateTable(self,rows):
    self.trv.delete(*self.trv.get_children())
    for i in rows:
      self.trv.insert(parent = '', index = 'end', values = i)
  
#   def search(self):
#     q = self.search_entry.get()
#     if q[0] == 'r':
#       rows = self.s.selectReceipt(q)
#     else:
#       rows = self.s.select(q)
#     self.updateTable(rows)

  def addBook(self):
    AddBookModal()
    
#   def clear(self):
#     rows = self.s.selectAll()
#     self.updateTable(rows)
    
  def getrow(self,event):
    rowId = self.trv.identify_row(event.y)
    item = self.trv.item(self.trv.focus())
    self.book = item['values'][1]
  
  def delete(self):
    self.s.deleteBook(self.book)
    rows = self.s.selectAll()
    self.updateTable(rows)
  
  
                          
            