from tkinter import *

def aktivahen():
    login = edit.get()

    if login =='Aleksej':
      t1.config(text='helloy Aleksej')

    else:
      t1.config(text='login')

#Создаем первое окно программы
w1 =Tk()
w1.geometry('500x200')
w1.config(bg='#272730')
w1.title('Mone_Biz')
w1.resizable(False,False)

#Надпись программы
def Label_t1():
    t1 = Label( w1, text='Привет в новой программе по заработку', bg='#272730', fg='#3E9D34' )
    t1.config( font=('Verdana', 15) )
    t1.pack()



Label_t1()


def Lebel_t2():
    t2 = Label( w1, text='В данной программе любой найдет заработок на свой вкус', bg='#272730', fg='#3E9D34' )
    t2.config( font=('Verdana', 10) )
    t2.pack()


Lebel_t2()


def Lebel_t3():
    t3 = Label( w1, text='Авторизируйся:', bg='#272730', fg='#3E9D34' )
    t3.config( font=('Verdana', 20) )
    t3.pack()


Lebel_t3()

#Сщоздаем поле вода для активации
edit = Entry (w1, width =40,bg='#E0E0E6')
edit.pack()

#Создаем кнопку аторизации
but = Button(w1, text = 'Присоедениться', command = aktivahen)
but.pack()

w1.mainloop()

