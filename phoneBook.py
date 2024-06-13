import tkinter as tk 
from tk import * #импорт всего
from tkinter import messagebox #импорт модулей
window = tk.Tk() #создаем окно
window.title('Телефонная книга')
window.geometry('600x600')
window.mainloop() #Метод с помощью которого окно открывается и не закрывается, пока пользователь его не закроет
frame = tk.Frame(
   window, #Обязательный параметр, который указывает окно для размещения Frame.
   padx = 10, #Задаём отступ по горизонтали.
   pady = 10 #Задаём отступ по вертикали.
)
frame.pack(expand=True) #Не забываем позиционировать виджет в окне. Здесь используется метод pack. С помощью свойства expand=True указываем, что Frame заполняет весь контейнер, созданный для него.
