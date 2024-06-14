import tkinter as tk 
from tk import * 
# from tkinter import ttk
# from tkinter import messagebox 
window = tk.Tk() #создаем окно
window.title('Телефонная книга')
window.geometry('600x600')

backgroundButtonColor = 'gray'
textColorButton = 'white'

frame = tk.Frame(
   window, #Обязательный параметр, который указывает окно для размещения Frame.
   padx = 10, #Задаём отступ по горизонтали.
   pady = 10 #Задаём отступ по вертикали.
)
frame.pack(expand=True) #Не забываем позиционировать виджет в окне. Здесь используется метод pack. С помощью свойства expand=True указываем, что Frame заполняет весь контейнер, созданный для него.

searchFrame = tk.Frame(
    window,
    padx = 10, #Задаём отступ по горизонтали.
    pady = 10 #Задаём отступ по вертикали.
)
searchFrame.pack(expand=True)

addAbonent = tk.Frame(
    window,
    padx = 10, #Задаём отступ по горизонтали.
    pady = 10 #Задаём отступ по вертикали.
)
addAbonent.pack(expand=True)
addAbonent.pack_forget()

allBookFrame = tk.Frame(
    window,
    padx = 10, #Задаём отступ по горизонтали.
    pady = 10 #Задаём отступ по вертикали.
)
allBookFrame.pack_forget()



def seeAllBook():
    frame.pack_forget()
    allBookFrame.pack()
    window.title('Весь справочник')

def getSearchFamilyFrame():
    frame.pack_forget()
    searchFrame.pack()
    window.title('Поиск по фамилии')

def getAddAbonentFrame():
    frame.pack_forget()
    addAbonent.pack()
    window.title('Добавить абонента')

def openWithReed():
    book = open('book.txt', 'r', encoding='utf-8')
    text = book.read()
    return text

def openWithWrite():
    book = open('book.txt', 'a', encoding='utf-8')
    text = []
    text.append(addFamilynameLabel_tf.get())
    text.append(addNameAbonentLabel_tf.get())
    text.append(addTelephonNumberLabel_tf.get())
    book.write('\n' + ' '.join(text))
    book.close()


searchFrame.pack_forget()

button_seeAllBook = tk.Button(
    frame,
    text='X         Отобразить весь справочник         X',
    command=lambda: seeAllBook()
)

button_seeAllBook.pack(
    ipadx=100,
    ipady=5,
    expand=True
)

button_seeAllBook.config(
    bg=backgroundButtonColor,
    fg=textColorButton
)

button_searchAbonentFamily = tk.Button(
    frame,
    text='X         Найти абонента по фамилии         X',
    bg=backgroundButtonColor,
    fg=textColorButton,
    command=lambda: getSearchFamilyFrame()
)

button_searchAbonentFamily.pack(
    ipadx=100,
    ipady=5,
    expand=True
)

button_searchTelephonNumber = tk.Button(
    frame,
    text='X         Найти с помощью номера телефона         X',
    bg=backgroundButtonColor,
    fg=textColorButton
)

button_searchTelephonNumber.pack(
    ipadx=78,
    ipady=5,
    expand=True
)

button_addAbonentOrChangeData = tk.Button(
    frame,
    text='X         Добавить абонента или изменить данные         X',
    bg=backgroundButtonColor,
    fg=textColorButton,
    command=lambda: getAddAbonentFrame()
)

button_addAbonentOrChangeData.pack(
    ipadx=66,
    ipady=5,
    expand=True
)

button_saveInTextFormat = tk.Button(
    frame,
    text='X         Сохранить в текстовом формате         X',
    bg=backgroundButtonColor,
    fg=textColorButton
)

button_saveInTextFormat.pack(
    ipadx=90,
    ipady=5,
    expand=True
)

button_exit = tk.Button(
    frame,
    text='X        Выход        X',
    command=lambda: frame.quit(),
    
)

button_exit.pack(
    ipadx=166,
    ipady=5,
    expand=True,
)

button_exit.config(
    bg=backgroundButtonColor,
    fg=textColorButton
)

searchLabel = tk.Label(
    searchFrame,
    text='Введите фамилию для поиска'
)
searchLabel.config(
    fg=textColorButton
)

search_tf = tk.Entry(
    searchFrame,

)
search_tf.grid(row=3, column=2)

allBookLabel = tk.Label(
    allBookFrame,
    text = openWithReed()
)
allBookLabel.pack()

addFamilynameLabel = tk.Label(
    addAbonent,
    text='Введите фамилию'
)
addFamilynameLabel.pack(
    ipadx=90,
    ipady=5,
    expand=True
)
addFamilynameLabel.grid(row=3, column=1)
addFamilynameLabel_tf = tk.Entry(
    addAbonent,
)
addFamilynameLabel_tf.grid(row=3, column=2)
addNameAbonentLabel = tk.Label(
    addAbonent,
    text='Введите имя'
)
addNameAbonentLabel.grid(row=4, column=1)
addNameAbonentLabel_tf = tk.Entry(
    addAbonent,
)
addNameAbonentLabel_tf.grid(row=4, column=2)
searchLabel.grid(row=3, column=1)
addTelephonNumberLabel = tk.Label(
    addAbonent,
    text='Введите номер телефона'
)
addTelephonNumberLabel.grid(row=5, column=1)
addTelephonNumberLabel_tf = tk.Entry(
    addAbonent,
)
addTelephonNumberLabel_tf.grid(row=5, column=2)
button_addAbonent = tk.Button(
    addAbonent,
    text='Сохранить абонента',
    bg=backgroundButtonColor,
    fg=textColorButton,
    command=lambda: openWithWrite()
)
button_addAbonent.grid(row=6, column=2)


window.mainloop() #Метод с помощью которого окно открывается и не закрывается, пока пользователь его не закроет

