from tkinter import *
from tkinter import ttk

root = Tk()
root.resizable(False, False)
root.geometry('400x300+500+200')

# s = ttk.Style()
# # print(s.theme_names(), s.theme_use())
# s.theme_use('xpnative')
# print(s.theme_names(), s.theme_use())


# Button(root, text='Button 1', padx=40, pady=5).pack(pady=10)
# ttk.Button(root, text='Button 2', width=21).pack()
#
# Entry(root).pack(pady=10)
# ttk.Entry(root).pack()

def choose(event):
    print(select.get())

select = ttk.Combobox(root, values=["January", "February", "March", "April"])
select.place(relx=0.5, rely=0.5, anchor=CENTER)
select.current(0)
select.bind("<<ComboboxSelected>>", choose)

root.mainloop()
