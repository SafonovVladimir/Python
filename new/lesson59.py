from tkinter import *

root = Tk()
root.geometry('400x400+400+150')

# l1 = Label(root, text='Hello World!', bg='#3498db', fg='white', font='16', padx=20, pady=8)
# l1.place(x=0, y=0)
#
l2 = Label(root, bg='#000')
l2.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

# bnt1 = Button(text='Button 1', bg='#3498db', fg='#fff', font='16', padx=20, pady=8)
# bnt1.place(x=0, y=0)
#
# bnt2 = Button(text='Button 2', bg='#2ecc71', fg='#fff', font='16', padx=20, pady=8)
# bnt2.place(relx=0.5, rely=0.5, anchor='center')
#
# bnt3 = Button(text='Button 3', bg='#f1c40f', fg='#fff', font='16', padx=20, pady=8)
# bnt3.place(relx=1, rely=1, anchor='se')

root.mainloop()
