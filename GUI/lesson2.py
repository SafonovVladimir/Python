from tkinter import *

root = Tk()
root.title('My first GUI APP')
root.iconbitmap('python.ico')
root.geometry('300x200+400+150')
# root.resizable(False, False)

def btn_clicked_print():
    print('Clicked')

btn = Button(root, text = 'Button1', activebackground='gray', bg='white', command=btn_clicked_print)
btn.pack()


root.mainloop()