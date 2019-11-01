from random import randrange as rnd, choice
import tkinter as tk
import math
import time

def main():
    global root, canvas, gun, target, score
    root = tk.Tk()
    score=0
    root.geometry('800x600')
    canvas = tk.Canvas(root, bg='white')
    canvas.pack(fill=tk.BOTH, expand=1)
    screen1 = canvas.create_text(400, 300, text='', font='28')
    gun = Gun()
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
        self.vx = vx/2
        self.vy = vy/2
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
        self.live-=0.5
        if self.live>=0:
            if self.x>=800:
                self.vx=-self.vx
                self.x=800-self.r
            if self.y>=600:
                self.vy=-self.vy
                self.y=600-self.r
            if self.x<=0:
                self.vx=-self.vx
                self.x=self.r
            else:
                self.vy -= 0.1*(80-self.live)
                self.vx*=0.99
                self.x += self.vx
                self.y -= self.vy
            self.set_coords()
        if self.live<-10:
            canvas.delete(self.id)
    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if self.x>=obj.x-obj.r and self.x<=obj.x+obj.r and self.y>=obj.y-obj.r and self.y<=obj.y+obj.r:
            return True
        else:
            return False


class Gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.angle = 1
        self.x=20
        self.y=450
        self.id = canvas.create_line(self.x , self.y, 50, 420,width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        r = 5
        self.angle = math.atan((event.y - self.y) / (event.x - self.x))
        x=20 + max(self.f2_power, 20) * math.cos(self.angle)
        y=450 + max(self.f2_power, 20) * math.sin(self.angle)
        vx = self.f2_power * math.cos(self.angle)
        vy = - self.f2_power * math.sin(self.angle)
        new_ball= Ball(x, y, vx, vy)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.angle = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')
        canvas.coords(self.id, 20, 450,
                      20 + max(self.f2_power, 20) * math.cos(self.angle),
                      450 + max(self.f2_power, 20) * math.sin(self.angle)
                      )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')


class Target():
    def __init__(self):
        self.points = 0
        self.live = 1
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(15, 50)
        self.vx=rnd(1,10)
        self.vy=rnd(1,10)
        color = self.color = 'red'
        self.id = canvas.create_oval(0, 0, 0, 0)
        canvas.coords(self.id, x-r, y-r, x+r, y+r)
        canvas.itemconfig(self.id, fill=color)
    def set_coords(self):
        canvas.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r)
    def move(self):
        if self.x>=800 or self.x<=0:
            self.vx=-self.vx
        if self.y>=600 or self.y<=0:
            self.vy=-self.vy
        self.x+=self.vx
        self.y+=self.vy
        self.set_coords()

def new_game(event=''):
    global gun, target, screen1, balls, bullet, score
    bullet = 0
    balls = []
    targets= []
    target1=Target()
    target2=Target()
    targets += [target1]
    targets += [target2]
    canvas.bind('<Button-1>', gun.fire2_start)
    canvas.bind('<ButtonRelease-1>', gun.fire2_end)
    canvas.bind('<Motion>', gun.targetting)
    sc=canvas.create_text(30, 30, text=score, font='28')
    while True:
        for t in targets:
            t.move()
        for b in balls:
            b.move()
            for t in targets:
                if b.hittest(t) and t.live:
                    t.live = 0
                    score+=1
                    canvas.bind('<Button-1>', '')
                    canvas.bind('<ButtonRelease-1>', '')
                    text=canvas.create_text(400, 400,text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов' )
                    canvas.update()
                    for t in targets:
                        canvas.delete(t.id)
                    time.sleep(4)
                    canvas.delete(text)
                    canvas.delete(sc)
                    canvas.delete(b.id)
                    new_game()
        canvas.update()
        time.sleep(0.03)
        gun.targetting()
        gun.power_up()
    canvas.delete(gun)
    root.after(750, new_game)

main()
new_game()

root.mainloop()
