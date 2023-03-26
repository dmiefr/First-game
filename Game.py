from tkinter import * # импортируем все
import random, time

def bros():
    x = random.choice(['b1.png', 'b2.png', 'b3.png', 'b4.png','b5.png',
                       'b6.png'])
    return x

def img(event):
    global b1, b2
    for i in range(18):
        b1 = PhotoImage(file = (bros()))
        b2 = PhotoImage(file = (bros()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time. sleep(0.12)

root = Tk() # стандартная переменная для окна с указанием класса Tk
root.geometry('800x400') # геометрия окна
root.title('Игра в кости. Сделай бросок!')
root.resizable(height = False, width = False) # ограничение размеров окна
root.iconphoto(True, PhotoImage(file = ('iconka.png'))) # размещаем изображение png с  помощью класса пфотоимэйдж 
font = PhotoImage(file = ('holst.png')) # фон 
Label(root, image = font).pack() # размещение по центру на окне, создание метки просто
lab1 = Label(root) # создание метки через переменную
lab1.place(relx = 0.3, rely = 0.5, anchor = CENTER) # расположение по осям икс и игрик от нуля до одного
lab2 = Label(root) # создание метки через переменную
lab2.place(relx = 0.7, rely = 0.5, anchor = CENTER)
######Button(root, text = 'Бросок', command = img).pack() # под холстом
root.bind('<1>', img) # обработчик событий передает функции аргумент поэтому добавим в img event
img('event') # что бы при запуске метки были не видимы

root.mainloop() # замкнем цикл

#  далее открыть терминал компьюетра
# командой pip install pyinstaller  скачиваем библиотеку
# проверяем версию программы командой pyinstaller --version
# командой pyinstaller Game.py превращаем файл игры и игру exe в папке build а затем создает папку с игрой в папке dist
# build удаляем, из dist достаем папку с игрой перемещая туда все програмные файлы и изображения

# для замены иконки программы в терминале pyinstaller -F -- icon=iconka.ico Game.py







