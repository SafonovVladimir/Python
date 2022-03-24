from tkinter import *
from tkinter import ttk

root = Tk()
# frm = ttk.Frame(root, padding=100)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.title('My first GUI APP')
root.iconbitmap('python.ico')
root.geometry('600x400+400+150')
root.resizable(False, False)
# root.config(bg='#000')
# root['bg'] = 'red'

root.mainloop()
