from tkinter import *

root = Tk()
root.geometry('600x400+400+150')

# f_top = Frame(root)
# f_top.pack()
# f_bottom = Frame(root)
# f_bottom.pack()

f_top = LabelFrame(root, text='TOP Frame', padx=10, pady=10)
f_top.pack(padx=10)
f_bottom = LabelFrame(root, text='BOTTOM Frame', padx=10, pady=10)
f_bottom.pack()

l1 = Label(f_top, text='1', font='15', fg='#fff', bg='#3498db', width=8, height=4).pack(side=LEFT)
l2 = Label(f_top, text='2', font='15', fg='#fff', bg='#2ecc71', width=8, height=4).pack(side=LEFT)
l3 = Label(f_bottom, text='3', font='15', fg='#fff', bg='#f1c40f', width=8, height=4).pack(side=LEFT)
l4 = Label(f_bottom, text='4', font='15', fg='#fff', bg='#34495e', width=8, height=4).pack(side=LEFT)



root.mainloop()



