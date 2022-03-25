from tkinter import *
from datetime import datetime

time = datetime.now().strftime("%H:%M")
clicks = 0
a = 5
b = 10

root = Tk()
root.title('Counter: ')
root.iconbitmap('python.ico')
root.geometry('300x200+400+150')


def btn_clicked_print():
    btn['text'] = time


def btn_click_plus():
    global a, b
    root.title(f'Counter: {a + b}')
    print(f'Counter: {a + b}')


def btn_click_minus():
    global a, b
    root.title(f'Counter: {b - a}')
    print(f'Counter: {b - a}')


def btn_click_mul():
    global a, b
    root.title(f'Counter: {b * a}')
    print(f'Counter: {a * b}')


def btn_click_div():
    global a, b
    root.title(f'Counter: {b // a}')
    print(f'Counter: {b // a}')


btn_plus = Button(root, text='+', width=5, activebackground='gray', bg='white', command=btn_click_plus)
btn_minus = Button(root, text='-', width=5, activebackground='gray', bg='white', command=btn_click_minus)
btn_mul = Button(root, text='*', width=5, activebackground='gray', bg='white', command=btn_click_mul)
btn_div = Button(root, text='/', width=5, activebackground='gray', bg='white', command=btn_click_div)
btn_plus.pack()
btn_minus.pack()
btn_mul.pack()
btn_div.pack()

root.mainloop()
