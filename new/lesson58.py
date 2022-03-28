from tkinter import *

root = Tk()
# root.geometry('600x400+400+150')

# f = Frame(root, pady=10)
# f.pack()
#
# btn_list = [
#     '7', '8', '9',
#     '4', '5', '6',
#     '1', '2', '3',
#     '0'
# ]
#
# row = 0
# column = 0
#
# for i in btn_list:
#     if i == '0':
#         Button(f, text=i, padx=10, pady=5).grid(row=row, columnspan=3)
#     else:
#         Button(f, text=i, padx=10, pady=5).grid(row=row, column=column)
#     column += 1
#     if column == 3:
#         column = 0
#         row += 1



# bnt7 = Button(f, text='7', padx=10, pady=5).grid(row=0, column=0)
# bnt8 = Button(f, text='8', padx=10, pady=5).grid(row=0, column=1)
# bnt9 = Button(f, text='9', padx=10, pady=5).grid(row=0, column=2)
#
# bnt4 = Button(f, text='4', padx=10, pady=5).grid(row=1, column=0)
# bnt5 = Button(f, text='5', padx=10, pady=5).grid(row=1, column=1)
# bnt6 = Button(f, text='6', padx=10, pady=5).grid(row=1, column=2)
#
# bnt1 = Button(f, text='1', padx=10, pady=5).grid(row=2, column=0)
# bnt2 = Button(f, text='2', padx=10, pady=5).grid(row=2, column=1)
# bnt3 = Button(f, text='3', padx=10, pady=5).grid(row=2, column=2)
#
# bnt0 = Button(f, text='0', padx=10, pady=5).grid(row=3, column=1)

l_user = Label(root, text='Login:').grid(row=0, column=0, padx=10, pady=10, sticky=W)
e_user = Entry(root).grid(row=0, column=1, padx=10, columnspan=2, sticky=W+E)

l_pass = Label(root, text='Password:').grid(row=1, column=0, padx=10, sticky=W)
e_pass = Entry(root, show="*").grid(row=1, column=1, padx=10, columnspan=2, sticky=W+E)

bnt_Login = Button (root, text = 'Вход', padx=5).grid(row=2, column=0, pady=10, padx=10, sticky=W)
bnt_reg = Button (root, text = 'Регистрация', padx=5).grid(row=2, column=1, pady=10)
bnt_forgot = Button (root, text = 'Забыли пароль', padx=5).grid(row=2, column=2, padx=10)



root.mainloop()



