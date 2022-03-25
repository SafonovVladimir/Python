from tkinter import *

a = 5
b = 10

root = Tk()
root.title('Counter: ')
root.iconbitmap('python.ico')
root.geometry('500x300+400+150')


def btn_click_plus():
    global a, b
    l['text'] = a + b
    # print(f'Counter: {a + b}')


def btn_click_eql():
    l['text'] = entry_text
    print(f'Counter: {entry_text}')


l = Label(root, text='0', bg='black', fg='white', width=30, height=5, anchor='se')
l.pack()

btn_plus = Button(root, text='+', width=5, activebackground='gray', bg='white', command=btn_click_plus)
btn_plus.pack()

btn_eql = Button(root, text='=', width=5, activebackground='gray', bg='white', command=btn_click_eql)
btn_eql.pack()

ent = Entry(root)
# print(entry_text) 
ent.pack()
entry_text = ent.get()

root.mainloop()











