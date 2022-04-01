from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk

root = ThemedTk(theme="radiance")
root.geometry("400x300+500+250")


ttk.Button(root, text="Quit", command=root.destroy).pack()
ttk.Entry(root).pack()


root.mainloop()