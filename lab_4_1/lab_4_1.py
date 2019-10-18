from tkinter import *
from random import randrange as rnd, choice
import time
def clicked():
    global name
    name=txt.get()
    root.destroy()
root = Tk()
txt = Entry(width=20)
b = Button(text="ОК", command=clicked)
l=Label(text="Enter your name")
txt.pack()
b.pack()
l.pack()
root.mainloop()
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']
obj=[]
high_scores=[]
score=0
k=0
with open('highscores.txt') as f:
    for line in f:
        high_scores.append(line.split())
        k+=1
for i in range(k):
    high_scores[i][0]=int(high_scores[i][0])

def randomball():
    x = rnd(100, 500)
    y = rnd(100, 500)
    r = rnd(50, 100)
    horizontal = rnd(1, 8)
    vertical = rnd(1, 8)
    color = choice(colors)
    return [0, [x, y, r, horizontal, vertical, color]]

def randomsquare():
    x=rnd(100,600)
    y=rnd(100,500)
    r=rnd(20,70)
    horizontal = rnd(1, 8)
    vertical = rnd(1, 8)
    color= choice(colors)
    return [1, [x, y, r, horizontal, vertical, color]]

for i in range(0, 3):
    obj.append(randomball())
    obj.append(randomsquare())


def move_square(a):
    global score, obj
    x=a[0]
    y=a[1]
    r=a[2]
    horizontal=a[3]
    vertical=a[4]
    color=a[5]
    if x + r >= 800:
        horizontal=-1*horizontal
    if x - r <= 0:
        horizontal=-1*horizontal
    if y - r <= 0:
        vertical=-1*vertical
    if y + r >= 600:
        vertical=-1*vertical
    a[0]=x+horizontal
    a[1]=y+vertical
    a[3]=horizontal
    a[4]=vertical
    canv.create_rectangle(x-r, y-r, x+r, y+r, fill=color, width=1)

def move_ball(a):
    global score, obj
    x = a[0]
    y = a[1]
    r = a[2]
    horizontal = a[3]
    vertical = a[4]
    color = a[5]
    if x + r >= 800:
        horizontal = -1 * horizontal
    if x - r <= 0:
        horizontal = -1 * horizontal
    if y - r <= 0:
        vertical = -1 * vertical
    if y + r >= 600:
        vertical = -1 * vertical
    a[0] = x + horizontal
    a[1] = y + vertical
    a[3] = horizontal
    a[4] = vertical
    canv.create_oval(x - r, y - r, x + r, y + r, fill=color, width=1)


def display():
    global score, obj
    canv.delete(ALL)
    canv.create_text(20, 10, text=score,
                     justify=CENTER, font="Verdana 14")
    for i in obj:
        if i[0] == 0:
            move_ball(i[1])
        else:
            move_square(i[1])
    root.after(10, display)

def click(event):
    global score, obj
    for i in obj:
        if i[0] == 0:
            if (event.x-i[1][0])**2+(event.y-i[1][1])**2<=(i[1][2])**2:
                score+=1
        else:
            if ((event.x)>=i[1][0]-i[1][2]) and ((event.x)<=i[1][0]+i[1][2]) and ((event.y)>=i[1][1]-i[1][2]) and ((event.y)<=i[1][1]+i[1][2]):
                score+=5

display()
canv.bind('<Button-1>', click)
mainloop()
high_scores.append([score, name])
high_scores = sorted(high_scores, reverse=True, key=lambda  i: i[0])
with open('highscores.txt', 'w') as f:
    for i in high_scores:
        f.writelines(str(i[0]))
        f.writelines(' ')
        f.writelines(str(i[1]))
        f.writelines('\n')



