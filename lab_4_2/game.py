from random import randrange as rnd, choice
import tkinter as tk
import math
import time


def main(amount, c):
    global root, canvas, score, pause_change, data, n, color
    root = tk.Tk()
    root.title("Пушка")
    n = amount
    color = c
    score = 0
    data=[i for i in range (n*10)]
    pause_change = 1
    root.geometry('1000x600')
    canvas = tk.Canvas(root, bg=color)
    canvas.pack(fill=tk.BOTH, expand=1)
    canvas.create_line(815, 0, 815, 600)


class Target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.type = rnd(1, 3)
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(15, 50)
        self.vx = rnd(1, 10)
        self.vy = rnd(1, 10)
        self.color = choice(['aquamarine', 'coral', 'pink', 'purple1', 'salmon', 'goldenrod', 'maroon1'])
        if self.type == 2:
            self.id = canvas.create_rectangle(0, 0, 0, 0)
        if self.type == 1:
            self.id = canvas.create_oval(0, 0, 0, 0)
        canvas.coords(self.id, x-r, y-r, x+r, y+r)
        canvas.itemconfig(self.id, fill=self.color)

    def set_coords(self):
        canvas.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r)

    def move(self):
        if self.x >= 800 or self.x <= 0:
            self.vx = -self.vx
        if self.y >= 600 or self.y <= 0:
            self.vy = -self.vy
        self.x += self.vx
        self.y += self.vy
        self.set_coords()


def pause(event):
    global targets, pause_change, data
    pause_change = -pause_change
    k = 0
    if pause_change < 0:
        for i in targets:
            k += 1
            data[k] = i.vx
            i.vx = 0
            k += 1
            data[k] = i.vy
            i.vy = 0
    else:
        for i in targets:
            k += 1
            i.vx = data[k]
            k += 1
            i.vy = data[k]


def click(event):
    global score, targets, sc, check
    for t in targets:
        if (event.x - t.x) ** 2 + (event.y - t.y) ** 2 <= (t.r) ** 2 and t.live == 1 and t.type == 1:
            score += 1
            check -= 1
            canvas.delete(sc)
            sc = canvas.create_text(940, 400, text="Очки: " + str(score), font='28')
            t.live = 0
            canvas.delete(t.id)
            canvas.update()
        if t.type == 2 and t.live == 1 and event.x <= t.x + t.r and event.x >= t.x - t.r \
                and event.y <= t.y + t.r and event.y >= t.y - t.r:
            score += 5
            check -= 1
            canvas.delete(sc)
            sc = canvas.create_text(940, 400, text="Очки: " + str(score), font='28')
            t.live = 0
            canvas.delete(t.id)
            canvas.update()

def new_game():
    global score, targets, n, sc, check
    check = n
    l = tk.Label(text='Вы проиграли', bg=color, font='arial 14')
    targets = []
    for i in range(n):
        targets += [Target()]
    root.bind('<KeyPress-p>', pause)
    root.bind('<Button-1>', click)
    sc = canvas.create_text(940, 400, text="Очки: " + str(score), font='28')
    while check != 0:
        for t in targets:
            t.move()
        canvas.update()
        time.sleep(0.03)
    canvas.delete(sc)
    new_game()

def scores():
    global score
    return score