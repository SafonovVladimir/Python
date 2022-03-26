from tkinter import *

root = Tk()
root.title('Rainbow')
root.iconbitmap('python.ico')
root.geometry('600x400+400+150')

l = Label(root, text="Поле ввода")
l.pack()

e = Entry(root)
e.insert((0), 'Hello ')
e.insert((6), 'World')
e.pack()

root.mainloop()
