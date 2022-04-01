from tkinter import *
import time


def tick():
    watch.after(100, tick)
    watch['text'] = time.strftime('%H:%M:%S')

# def tick():
#     label.after(200, tick)
#     label['text'] = time.strftime('%H:%M:%S')


root = Tk()
watch = Label(root, font="Arial 70")
watch.pack()


# label = Label(font='sans 20')
# label.pack()
watch.after_idle(tick)
root.mainloop()
