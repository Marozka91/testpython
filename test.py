from tkinter import *

def aktivahen():
    aktiv = edit.get()
    print ('aktiv')("Приветствую вас")

#Создаем первое окно программы
w1 =Tk()
w1.geometry('500x200')
w1.config(bg='#272730')
w1.title('Mone_Biz')
w1.resizable(False,False)


#Надпись программы
t1 = Label(w1, text='Привет в новой программе по заработку', bg='#272730', fg='#3E9D34')
t1.config(font=('Verdana',15))
t1.pack()
t2 = Label(w1, text='В данной программе любой найдет заработок на свой вкус', bg='#272730', fg='#3E9D34')
t2.config(font=('Verdana',10))
t2.pack()
t3 = Label(w1, text='Авторизируйся:', bg='#272730', fg='#3E9D34')
t3.config(font=('Verdana',20))
t3.pack()
#Сщоздаем поле вода для активации

w1.mainloop()

