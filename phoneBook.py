import tkinter as tk 
from tk import * 
# from tkinter import ttk
from tkinter import messagebox 
import os
window = tk.Tk() #создаем окно
window.title('Телефонная книга')
window.geometry('600x600')

backgroundButtonColor = 'gray'
textColorButton = 'white'
'''
Фреймы
'''
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

searchTelephonFrame = tk.Frame(
    window,
    padx = 10, #Задаём отступ по горизонтали.
    pady = 10 #Задаём отступ по вертикали.
)
searchTelephonFrame.pack_forget()

saveDocumentFrame = tk.Frame(
    window,
    padx = 10, #Задаём отступ по горизонтали.
    pady = 10 #Задаём отступ по вертикали.
)
saveDocumentFrame.pack_forget()

def changeFrame(thisFrame, toFrame):
    thisFrame.pack_forget()
    toFrame.pack()

def openWithReed():
    book = open('book.txt', 'r', encoding='utf-8')
    text = book.read()
    book.close()
    return text

def listToDict(textInbook):
    abonents = textInbook.split('\n')
    dictAbonents = {}
    for i in abonents:
        keyFirst = i.split(('.'*10))
        dictAbonents[keyFirst[0]] = keyFirst[1]
    return dictAbonents

def saveDocument(adress):
    saveBook = open((adress+'/saveBook.txt'), 'w', encoding='utf-8')
    saveBook.write(openWithReed())
    saveBook.close()

def openWithWrite():
    textInbook = openWithReed()
    text = []
    text.append(addFamilynameLabel_tf.get())
    text.append(addNameAbonentLabel_tf.get())
    text.append(addTelephonNumberLabel_tf.get())
    
    dictAbonents = listToDict(textInbook)

    dictAbonents[(text[0] + ' ' + text[1])] = text[2]
    book = open('book.txt', 'w', encoding='utf-8')
    strigWrite = '\n'.join(f'{key}..........{value}' for key, value in dictAbonents.items())
    book.write(strigWrite)
    book.close()


def search(searchBy, whatSearch):
    book = openWithReed()
    dictBook = listToDict(book)
    text = ''
    if searchBy == 'lastNameOrName':
        for key, value in dictBook.items():
            listKey = key.split(' ')
            for i in listKey:
                if i == whatSearch:
                    text += key + ' ' + value + '\n'
    elif searchBy == 'telephon':
        for key, value in dictBook.items():
            if value == whatSearch:
                text += key + ' ' + value + '\n'
    if len(text) < 1:
        return 'Не найдено'
    return text

searchFamily = lambda what: search('lastNameOrName', what)
searchTelephon = lambda what: search('telephon', what)

searchFrame.pack_forget()

'''
Главная страница
'''

button_seeAllBook = tk.Button(
    frame,
    text='X         Отобразить весь справочник         X',
    command=lambda: changeFrame(frame, allBookFrame)
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
    text='X         Найти абонента по фамилии или имени         X',
    bg=backgroundButtonColor,
    fg=textColorButton,
    command=lambda: changeFrame(frame, searchFrame)
)

button_searchAbonentFamily.pack(
    ipadx=69,
    ipady=5,
    expand=True
)

button_searchTelephonNumber = tk.Button(
    frame,
    text='X         Найти с помощью номера телефона         X',
    bg=backgroundButtonColor,
    fg=textColorButton,
    command=lambda: changeFrame(frame, searchTelephonFrame)
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
    command=lambda: changeFrame(frame, addAbonent)
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
    fg=textColorButton,
    command=lambda: changeFrame(frame, saveDocumentFrame)
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
'''
Поиск по фамилии
'''
searchLabel = tk.Label(
    searchFrame,
    text='Введите фамилию или имя для поиска',
    font=('Times New Roman', 14)
)
searchLabel.config(
    fg=textColorButton
)
searchLabel.grid(row=3, column=1)

search_tf = tk.Entry(
    searchFrame,
    font=('Times New Roman', 14)

)
search_tf.grid(row=3, column=2)

button_searchByFamily = tk.Button(
    searchFrame,
    text='X         Найти         X',
    command=lambda: messagebox.showinfo('bmi-pythonguides', searchFamily(search_tf.get())),
    bg=backgroundButtonColor,
    fg=textColorButton,
)

button_searchByFamily.grid(row=4,  column=2)

button_downSearchFamily = tk.Button(
    searchFrame,
    text='X         Назад         X',
    command=lambda: changeFrame(searchFrame, frame),
    bg=backgroundButtonColor,
    fg=textColorButton,
)

button_downSearchFamily.grid(row=5, column=2)

'''
Поиск по номеру телефона
'''
searchByTelephonLabel = tk.Label (
    searchTelephonFrame,
    text='Введите номер телефона для поиска',
    font=('Times New Roman', 14)
)
searchByTelephonLabel.grid(row=1, column=1)
searchByTelephonLabel_tk = tk.Entry(
    searchTelephonFrame,
    font=('Times New Roman', 14)
)
searchByTelephonLabel_tk.grid(row=1, column=2)

button_searchByTelephon = tk.Button(
    searchTelephonFrame,
    text='X        Найти         X',
    font=('Times New Roman', 14),
    command=lambda: messagebox.showinfo('bmi-pythonguides', searchTelephon(searchByTelephonLabel_tk.get())),
    bg=backgroundButtonColor,
    fg=textColorButton,
)
button_searchByTelephon.grid(row=2, column=2)
button_searchByTelephonDown = tk.Button(
    searchTelephonFrame,
    text='X        Назад         X',
    command=lambda: changeFrame(searchTelephonFrame, frame),
    bg=backgroundButtonColor,
    fg=textColorButton,
    font=('Times New Roman', 14),
)
button_searchByTelephonDown.grid(row=3, column=2)

'''
Показать всю книгу
'''

allBookLabel = tk.Label(
    allBookFrame,
    text = openWithReed(),
    justify='left',
    font=('Times New Roman', 14)
)
allBookLabel.pack()

button_downAllBook = tk.Button(
    allBookFrame,
    text='Назад',
    command=lambda: changeFrame(allBookFrame, frame),
    bg=backgroundButtonColor,
    fg=textColorButton,
)

button_downAllBook.pack(
    ipadx=66,
    ipady=5,
    expand=True
)

'''
Добавить или изменить данные:
'''
addFamilynameLabel = tk.Label(
    addAbonent,
    text='Введите фамилию',
    font=('Times New Roman', 14)
)
addFamilynameLabel.pack(
    ipadx=90,
    ipady=5,
    expand=True
)
addFamilynameLabel.grid(row=3, column=1)
addFamilynameLabel_tf = tk.Entry(
    addAbonent,
    font=('Times New Roman', 14)
)
addFamilynameLabel_tf.grid(row=3, column=2)
addNameAbonentLabel = tk.Label(
    addAbonent,
    text='Введите имя',
    font=('Times New Roman', 14)
)
addNameAbonentLabel.grid(row=4, column=1)
addNameAbonentLabel_tf = tk.Entry(
    addAbonent,
    font=('Times New Roman', 14)
)
addNameAbonentLabel_tf.grid(row=4, column=2)

addTelephonNumberLabel = tk.Label(
    addAbonent,
    text='Введите номер телефона',
    font=('Times New Roman', 14)
)
addTelephonNumberLabel.grid(row=5, column=1)
addTelephonNumberLabel_tf = tk.Entry(
    addAbonent,
    font=('Times New Roman', 14)
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
button_downAddAbonent = tk.Button(
    addAbonent,
    text='X           Назад           X',
    bg=backgroundButtonColor,
    fg=textColorButton,
    command=lambda: changeFrame(addAbonent, frame)
)
button_downAddAbonent.grid(row=7, column=2)

'''
Сохранить документ
'''
saveDocumentLabel = tk.Label(
    saveDocumentFrame,
    text='Адрес',
    font=('Times New Roman', 14)
)
saveDocumentLabel.grid(row=1, column=1)
saveDocumentLabel_tk = tk.Entry(
    saveDocumentFrame,
    font=('Times New Roman', 14),
    width=50
)
saveDocumentLabel_tk.insert(0, os.getcwd())
saveDocumentLabel_tk.grid(row=1, column=2)
button_saveDocument = tk.Button(
    saveDocumentFrame,
    text='X    Сохранить     X',
    bg=backgroundButtonColor,
    fg=textColorButton,
    command=lambda: saveDocument(saveDocumentLabel_tk.get())
)
button_saveDocument.grid(row=2, column=2)
button_saveDocumentDown = tk.Button(
    saveDocumentFrame,
    text='X         Назад         X',
    bg=backgroundButtonColor,
    fg=textColorButton,
    command=lambda: changeFrame(saveDocumentFrame, frame)
)
button_saveDocumentDown.grid(row=3, column=2)
window.mainloop() #Метод с помощью которого окно открывается и не закрывается, пока пользователь его не закроет

