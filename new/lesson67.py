from tkinter import *

root = Tk()
root.geometry('400x300+500+200')

def f_event(event, key):
    print(event)
    print(f"{key} Click")


# l = Label(root, bg="blue")
# l.pack(fill=X, expand=1)
# l.bind("<Button-1>", f_event)

e = Entry(root, justify=CENTER, font="Arial 15")
e.pack(fill=X, expand=1, padx=10, ipady=10)
e.bind("<Button-1>", lambda event, key="Left": f_event(event, key))
e.bind("<Button-3>", lambda event, key="Right": f_event(event, key))


root.mainloop()
