from random import randrange as rnd, choice
import tkinter as tk
import math
import time


def main(amount, c):
    global root, canvas, gun, score, gy, pause_change, data, n, color
    root = tk.Tk()
    root.title("Пушка")
    n = amount
    color=c
    score = 0
    data=[i for i in range (n*10)]
    pause_change = 1
    root.geometry('1000x600')
    canvas = tk.Canvas(root, bg=color)
    canvas.pack(fill=tk.BOTH, expand=1)
    gun = Gun()
    gy = 1
    canvas.create_line(815, 0, 815, 600)
    bullet = 0
    balls = []


class Ball():
    def __init__(self, x=40, y=450, vx=0, vy=0):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = vx
        self.vy = vy
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canvas.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 80

    def set_coords(self):
        canvas.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.live >= 0:
            if self.x >= 800:
                self.vx = -self.vx
                self.x = 800-self.r
            if self.y >= 600:
                self.vy = -self.vy
                self.y = 600-self.r
                self.live -= 5
            if self.x <= 0:
                self.vx = -self.vx
                self.x = self.r
            else:
                self.vy -= gy
                self.vy *= 0.98
                self.vx *= 0.99
                self.x += self.vx
                self.y -= self.vy
            self.set_coords()

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if math.sqrt((self.x-obj.x)*(self.x-obj.x)+(self.y-obj.y)*(self.y-obj.y)) <= self.r+obj.r:
            return True
        else:
            return False


class Gun():
    def __init__(self):
        self.upon = 0
        self.updown = 0
        self.f2_power = 10
        self.f2_on = 0
        self.vy = 5
        self.angle = 1
        self.x = 20
        self.y = 450
        self.x1 = 50
        self.y1 = 420
        self.id = canvas.create_line(self.x, self.y, self.x1, self.y1, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet, pause_change
        bullet += 1
        r = 5
        self.angle = math.atan((event.y - self.y) / (event.x - self.x))
        x = 20 + max(self.f2_power, 20) * math.cos(self.angle)
        y = self.y + max(self.f2_power, 20) * math.sin(self.angle)
        vx = self.f2_power * math.cos(self.angle)
        vy = - self.f2_power * math.sin(self.angle)
        if pause_change > 0:
            new_ball = Ball(x, y, vx, vy)
            balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.angle = math.atan((event.y - self.y) / (event.x - 20))
        if self.f2_on:
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')
        self.x1 = 20 + max(self.f2_power, 20) * math.cos(self.angle)
        self.y1 = self.y + max(self.f2_power, 20) * math.sin(self.angle)
        canvas.coords(self.id, 20, self.y, self.x1, self.y1)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')

    def up_start(self, event):
        self.upon = 1

    def moveup(self):
        if self.upon == 1:
            if self.y >= 10:
                canvas.update()
                self.y -= self.vy

    def up_finish(self, event):
        self.upon = 0

    def down_start(self, event):
        self.updown = 1

    def movedown(self):
        if self.updown == 1:
            if self.y <= 590:
                canvas.update()
                self.y += self.vy

    def down_finish(self, event):
        self.updown = 0

    def hittest(self, obj):
        if math.sqrt((self.x1-obj.x)*(self.x1-obj.x)+(self.y1-obj.y)*(self.y1-obj.y)) <= obj.r:
            return True
        else:
            return False


class Target():
    def __init__(self):
        self.points = 0
        self.live = 1
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(15, 50)
        self.vx = rnd(1, 10)
        self.vy = rnd(1, 10)
        self.color = choice(['aquamarine', 'coral', 'pink', 'purple1', 'salmon', 'goldenrod', 'maroon1'])
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
    global balls, targets, gun, pause_change, data, gy
    pause_change = -pause_change
    k = 0
    if pause_change < 0:
        for i in balls:
            k += 1
            data[k] = i.vx
            i.vx = 0
            k += 1
            data[k] = i.vy
            i.vy = 0
        for i in targets:
            k += 1
            data[k] = i.vx
            i.vx = 0
            k += 1
            data[k] = i.vy
            i.vy = 0
        gy=0
        gun.vy=0
    else:
        for i in balls:
            k += 1
            i.vx = data[k]
            k += 1
            i.vy = data[k]
        for i in targets:
            k += 1
            i.vx = data[k]
            k += 1
            i.vy = data[k]
        gy = 1
        gun.vy = 5

def new_game():
    global gun, balls, bullet, score, targets, n
    bullet = 0
    check = n
    l = tk.Label(text='Вы проиграли', bg=color, font='arial 14')
    balls = []
    targets = []
    for i in range(n):
        targets += [Target()]
    canvas.bind('<Button-1>', gun.fire2_start)
    canvas.bind('<ButtonRelease-1>', gun.fire2_end)
    canvas.bind('<Motion>', gun.targetting)
    root.bind('<KeyPress-Up>', gun.up_start)
    root.bind('<KeyRelease-Up>', gun.up_finish)
    root.bind('<KeyPress-Down>', gun.down_start)
    root.bind('<KeyRelease-Down>', gun.down_finish)
    root.bind('<KeyPress-p>', pause)
    sc = canvas.create_text(940, 400, text="Очки: " + str(score), font='28')
    while True:
        for t in targets:
            t.move()
            if gun.hittest(t) and t.live:
                canvas.delete(gun)
                for t in targets:
                    canvas.delete(t.id)
                    t.live = 0
                for b in balls:
                    canvas.delete(b.id)
                    b.live = -50
                canvas.delete(sc)
                l.place(x=400, y=400)
                canvas.update()
                time.sleep(4)
                l.destroy()
                score = 0
                gun.x = 20
                gun.y = 450
                new_game()
        for b in balls:
            b.move()
            for t in targets:
                if b.hittest(t) and t.live and b.live > 0:
                    t.live = 0
                    score += 1
                    canvas.delete(sc)
                    b.live = -50
                    sc = canvas.create_text(940, 400, text="Очки: " + str(score), font='28')
                    check -= 1
                    canvas.delete(t.id)
                    canvas.delete(b.id)
                    canvas.bind('<Button-1>', gun.fire2_start)
                    canvas.bind('<ButtonRelease-1>', gun.fire2_end)
                    canvas.bind('<Motion>', gun.targetting)
                    root.bind('<KeyPress-Up>', gun.up_start)
                    root.bind('<KeyRelease-Up>', gun.up_finish)
                    root.bind('<KeyPress-Down>', gun.down_start)
                    root.bind('<KeyRelease-Down>', gun.down_finish)
                    canvas.update()
                    if check == 0:
                        for b in balls:
                            canvas.delete(b.id)
                        text = canvas.create_text(400, 400, text='Количество выстрелов: ' + str(bullet), font='arial 14')
                        canvas.update()
                        time.sleep(4)
                        canvas.delete(text)
                        canvas.delete(sc)
                        canvas.delete(b.id)
                        check = n
                        new_game()
        canvas.update()
        time.sleep(0.03)
        gun.targetting()
        gun.power_up()
        gun.moveup()
        gun.movedown()


def scores():
    global score
    return score