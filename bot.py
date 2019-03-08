from tkinter import *

def forbur():

    login = edit.get()

    if login == "aleksej":
       

    else:
        t1.config(text = 'Noy Login')

w2=Tk()
w2.geometry('200x80')

t1 = Label (w2, text='Enter login')
t1.pack()

edit = Entry (w2, width = 20)
edit.pack()

but = Button(w2, text = 'Enter', command = forbur)
but.pack()
w2.mainloop()