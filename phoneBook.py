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

def seeAllBook():
    frame.pack_forget()
    window.title('Весь справочник')

def getSearchFamilyFrame():
    frame.pack_forget()
    searchFrame.pack()
    window.title('Поиск по фамилии')

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
    fg=textColorButton
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

searchLabel.grid(row=3, column=1)
window.mainloop() #Метод с помощью которого окно открывается и не закрывается, пока пользователь его не закроет

