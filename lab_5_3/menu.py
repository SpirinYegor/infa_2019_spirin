import tkinter as tk
import game
n = 2
color = '#206999'
def Menu():
    global root1, button1, button2, highscores, button3, color, button4, men, button5
    root1 = tk.Tk()
    root1.title("Пушка")
    root1.geometry("1000x600")
    highscores = []
    k = 0
    with open('highscores.txt') as f:
        for line in f:
            highscores.append(line.split())
            k += 1
    for i in range(k):
        highscores[i][0] = int(highscores[i][0])
    men = tk.Canvas(root1, bg=color)
    men.pack(fill=tk.BOTH, expand=1)
    button1 = tk.Button(text='Новая игра', width=20, height=3, font='arial 14')
    button1.place(x=250, y=175)
    button1.bind('<Button-1>', clicked1)
    button2 = tk.Button(text='Выход из игры', width=20, height=3, font='arial 14')
    button2.place(x=250, y=325)
    button2.bind('<Button-1>', end)
    button3 = tk.Button(text='Таблица рекордов', width=20, height=3, font='arial 14')
    button3.place(x=500, y=100)
    button3.bind('<Button-1>', clickedscores)
    button4 = tk.Button(text='Инструкция', width=20, height=3, font='arial 14')
    button4.place(x=500, y=250)
    button4.bind('<Button-1>', instruction)
    button5 = tk.Button(text='Настройки', width=20, height=3, font='arial 14')
    button5.place(x=500, y=400)
    button5.bind('<Button-1>', settings)


def clicked1(event):
    global button1, button2, txt, button3, button4, button5
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    txt = tk.Entry(width=46)
    txt.place(x=300, y=300)
    l1 = tk.Label(text='Введите имя', font='arial 14', bg=color)
    l1.place(x=380, y=250)
    l2 = tk.Label(text='Нажмите enter, чтобы продолжить', font='arial 14', bg=color)
    l2.place(x=290, y=350)
    root1.bind('<Return>', start)


def start(event):
    global root1, txt, name
    name = txt.get()
    root1.destroy()
    game.main(n)
    button = tk.Button(text='Вернуться в меню', width=15, height=2, font='arial 14')
    button.place(x=820, y=10)
    button.bind('<Button-1>', clickedmenu)
    game.new_game()


def end(event):
    root1.destroy()


def clickedmenu(event):
    global name, score, highscores
    score=game.scores()
    highscores.append([score, name])
    highscores = sorted(highscores, reverse=True, key=lambda i: i[0])
    with open('highscores.txt', 'w') as f:
        for i in highscores:
            f.writelines(str(i[0]))
            f.writelines(' ')
            f.writelines(str(i[1]))
            f.writelines('\n')
    game.root.destroy()
    Menu()


def clickedscores(event):
    global button1, button2, button3, button4, button5
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    y1 = 0
    x1 = 100
    with open('highscores.txt') as f:
        for line in f:
            if y1 == 550:
                x1 += 150
                y1 = 50
            else:
                y1 += 50
            l = line.split()
            labe = tk.Label(text=l, font='arial 14', bg=color)
            labe.place(x=x1, y=y1)
    button = tk.Button(text="Меню", width=5, height=2, font='arial 14')
    button.place(x=900, y=50)
    button.bind('<Button-1>', back_to_menu)


def back_to_menu(event):
    root1.destroy()
    Menu()


def back_to_menu_s(event):
    global txt, n
    n = txt.get()
    if n == '':
        n=2
    n=int(n)
    root1.destroy()
    Menu()


def instruction(event):
    global button1, button2, txt, button3, men, button4, button5
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    men.create_text(400, 40, text='Инструкция', font='arial 50')
    men.create_text(400, 100, text='За каждое попадание начисляется по одному очку.     ', font='arial 20')
    men.create_text(410, 150, text='Передвигайте пушку с помощью клавиш вверх и вниз.   ', font='arial 20')
    men.create_text(380, 200, text='Если цель попадет в пушку, вы проиграете.           ', font='arial 20')
    men.create_text(410, 240, text="Игру можно поставить на паузу с помощью клавиши 'P'.", font='arial 20')
    button = tk.Button(text="Меню", width=5, height=2, font='arial 14')
    button.place(x=900, y=50)
    button.bind('<Button-1>', back_to_menu)


def settings(event):
    global button1, button2, button3, button4, button5, txt, color, var, root1, l1
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    var = tk.IntVar()
    var.set(0)
    txt = tk.Entry(width=45)
    txt.place(x=540, y=300)
    l1 = tk.Label(text='Количество мишеней', font='arial 14', bg=color)
    l1.place(x=580, y=250)
    button = tk.Button(text="Меню", width=5, height=2, font='arial 14')
    button.place(x=900, y=50)
    button.bind('<Button-1>', back_to_menu_s)
    red = tk.Radiobutton(text="Желтый", variable=var, value=0)
    green = tk.Radiobutton(text="Зеленый", variable=var, value=1)
    blue = tk.Radiobutton(text="Синий", variable=var, value=2)
    cyan = tk.Radiobutton(text='Исходный', variable=var, value=3)
    buttonx = tk.Button(text='Изменить', command=change)
    red.place(x=240, y=240)
    green.place(x=240, y=260)
    blue.place(x=240, y=280)
    cyan.place(x=240, y=300)
    buttonx.place(x=240, y=320)


def change():
    global men, var, color, l1
    if var.get() == 0:
        color = 'yellow'
    elif var.get() == 1:
        color = 'green'
    elif var.get() == 2:
        color = 'blue'
    elif var.get() == 3:
        color = '#206969'
    men['bg'] = color
    l1['bg'] = color
