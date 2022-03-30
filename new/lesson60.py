from tkinter import *

root = Tk()
root.geometry('600x400+400+150')

f_menu = Frame(root, bg='#1F252A', height=40)
f_text = Frame(root, bg='white')
f_menu.pack(fill=X)
f_text.pack(fill=BOTH, expand=1)

l_menu = Label(f_menu, text='Menu', bg='#2B3239', fg='#C6DEC1', font='Arial 10')
l_menu.place(x=10, y=10)

t = Text(f_text, bg='#343D46', fg='#C6DEC1', padx=10, pady=10, wrap=WORD, insertbackground='#EDA756')
t.pack(fill=BOTH, expand=1)

scrollbar = Scrollbar(t)
scrollbar.pack(side=RIGHT, fill=Y)




root.mainloop()
