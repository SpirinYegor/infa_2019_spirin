from graph import *
from math import *
def mane(x, y, w, h):
    brushColor(234, 199, 177)
    ellyps(x + (w*15),y + (h*5), x + (w*55),y + (h*23))
    brushColor(234, 177, 177)
    ellyps(x, y, x + (w*45), y + (h*10))
    ellyps(x + (w*30), y - (h*15), x + (w*60), y )
    brushColor(230, 255, 129)
    ellyps(x + (w*10),y + (h*50),x + (w*60), y + (h*65))
    brushColor(234, 199, 177)
    ellyps(x - (w*15), y + (h*5), x + (w*23), y + (h*30))
    ellyps(x, y + (h*35), x + (w*40), y + (h*55))
    brushColor(255, 239, 172)
    ellyps(x - w*30, y + h*25, x + w*25, y + h*45)
    ellyps(x - w*25, y + h*50, x + w*10, y + h*65)
    brushColor(230, 255, 129)
    ellyps(x - w*40, y + h*40, x, y + h*55)
    brushColor(176, 234, 222)
    ellyps(x - w*40, y + h*60, x - w*10, y + h*70)
    brushColor(244, 216, 228)
    ellyps(x - w*15,y + h*58, x + w*30, y + h*70)
    ellyps(x - w*15, y + h*68, x + w*30, y + h*80)
    brushColor(176, 234, 222)
    ellyps(x, y + h*62, x + w*40, y + h*77)
    brushColor(222, 177, 234)
    ellyps(x - w*60, y + h*70, x, y + h*85)


def body(x, y, width, higth,n, r, g, b):
    brushColor("white")
    for i in range(n):
        penColor(i * r, g , b)
        brushColor(i * r, g, b)
        ellyps(x - (width-i/n*width), y - (higth-i/n*higth), x + (width-i/n*width), y + higth-i/n*higth)
    rectangle(x - int(0.8*width), y, x - int(0.65 * width), y + 2.5*higth)
    rectangle(x - int(0.55*width), y, x - int(0.4 * width), y + 2.2*higth)
    rectangle(x + int(0.8*width), y, x + int(0.65 * width), y + 2.2*higth)
    rectangle(x + int(0.55*width), y, x + int(0.4 * width), y + 2.5*higth)
    rectangle(x + int(0.35*width), y, x + (0.85*width), y - int(2.5*higth))
    ellyps(x + int(0.43*width), y - int(2.7*higth), x + int(0.87*width), y - int(2.4*higth))
    ellyps(x + 0.5*width, y - 2.45*higth, x + 1.3*width, y - 1.80*higth)
    brushColor(230, 129, 255)
    circle(x + 0.75*width, y-2.3*higth, 0.08*width)
    brushColor("black")
    circle(x + 0.78*width, y-2.3*higth, 0.03*width)
    brushColor(234, 177, 177)
    penColor(234, 177, 177)
    polygon([(x + 0.6*width, y - 2.6*higth), (x + 0.7*width, y - 4.24*higth), (x + 0.75*width, y - 2.55*higth), (x + 0.6*width, y - 2.6*higth)])


def tree(x, y, width, higth):
    penSize(0)
    brushColor(231, 231, 231)
    rectangle(x - 0.15 * width, y, x + 0.15*width, y + 4.2*higth)
    brushColor(0, 129, 0)
    penSize(2)
    penColor(0, 255, 0)
    ellyps(x - 0.6*width, y - 3*higth, x + 0.6*width, y)
    ellyps(x - width, y - higth, x + width, y + higth)
    ellyps(x - 0.6*width, y + 0.5*higth, x + 0.6*width, y + 2.5*higth)
    brushColor(255, 205, 172)
    circle(x -0.75*width, y + 0.05*higth, 0.15*width)
    circle(x + 0.7 * width, y + 0.05 * higth, 0.15 * width)
    circle(x + 0.15*width, y - 2.3*higth, 0.15*width)
    circle(x + 0.4*width, y + 1.9*higth, 0.15*width)



penSize(0)  # background
brushColor(0, 255, 44)
rectangle(0, 250, 800, 1000)
brushColor("cyan")
rectangle(0, 0, 800, 250)

tree(150, 60, 150, 60) # forest
tree(190, 250, 90, 30)
tree(40, 200, 70, 60)
tree(150, 340, 80, 35)
tree(70, 440, 80, 35)

penSize(0)

mane(165, 490, 0.6, 0.6)# horse1
mane(165, 530, -0.6, 0.6)
body(250, 500, 70, 30, 100, 2, 100, 220)
mane(264, 425, 0.6, 0.6)

mane(500, 375, -0.6, 0.6)# horse2
mane(500, 395, -0.6, 0.6)
body(425, 395, -65, 25, 100, 2, 20, 151)
mane(415, 335, -0.55, 0.55)

mane(280, 250, 0.5, 0.5)# horse3
mane(285, 270, -0.4, 0.4)
body(330, 260, 40, 20, 100, 2, 20, 70)
mane(333, 210, 0.4, 0.4)

mane(490, 235, -0.2, 0.2)# horse4
mane(490, 245, 0.2, 0.2)
body(460, 240, -25, 10, 100, 2, 250, 10)
mane(456, 215, -0.2, 0.2)

penSize(1)
for i in range(110):
    penColor(i*2, 255, 255 - i*2)
    brushColor(i*2, 255, 255 - i*2)
    circle(410, 70, 110-i)

brushColor("white")
def update():
    global i, obj, x, y, width, higth, r, obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9, obj10, w, h, obj11
    global obj12, obj13, obj14, obj15, obj16, obj17, obj18, obj19, obj20, obj21, obj22, obj23, obj24, obj25, obj26, obj27
    global obj28, obj29, obj30, obj31, obj32, obj33, obj34, obj35, obj36, obj37, obj38
    i+=1
    moveObjectTo(obj, xCobj+r*cos(i/2/pi),yCobj+r*sin(i/2/pi))
    moveObjectTo(obj1, xCobj1 + r * cos(i / 2 / pi), yCobj1 + r * sin(i / 2 / pi))
    moveObjectTo(obj2, xCobj2 + r * cos(i / 2 / pi), yCobj2 + r * sin(i / 2 / pi))
    moveObjectTo(obj3, xCobj3 + r * cos(i / 2 / pi), yCobj3 + r * sin(i / 2 / pi))
    moveObjectTo(obj4, xCobj4 + r * cos(i / 2 / pi), yCobj4 + r * sin(i / 2 / pi))
    moveObjectTo(obj5, xCobj5 + r * cos(i / 2 / pi), yCobj5 + r * sin(i / 2 / pi))
    moveObjectTo(obj6, xCobj6 + r * cos(i / 2 / pi), yCobj6 + r * sin(i / 2 / pi))
    moveObjectTo(obj7, xCobj7 + r * cos(i / 2 / pi), yCobj7 + r * sin(i / 2 / pi))
    moveObjectTo(obj8, xCobj8 + r * cos(i / 2 / pi), yCobj8 + r * sin(i / 2 / pi))
    moveObjectTo(obj9, xCobj9 + r * cos(i / 2 / pi), yCobj9 + r * sin(i / 2 / pi))
    moveObjectTo(obj10, xCobj7 + r * cos(i / 2 / pi), yCobj7 + r * sin(i / 2 / pi))
    moveObjectTo(obj11, xCobj11 + r * cos(i / 2 / pi), yCobj11 + r * sin(i / 2 / pi))
    moveObjectTo(obj12, xCobj12 + r * cos(i / 2 / pi), yCobj12 + r * sin(i / 2 / pi))
    moveObjectTo(obj13, xCobj13 + r * cos(i / 2 / pi), yCobj13 + r * sin(i / 2 / pi))
    moveObjectTo(obj14, xCobj14 + r * cos(i / 2 / pi), yCobj14 + r * sin(i / 2 / pi))
    moveObjectTo(obj15, xCobj15 + r * cos(i / 2 / pi), yCobj15 + r * sin(i / 2 / pi))
    moveObjectTo(obj16, xCobj16 + r * cos(i / 2 / pi), yCobj16 + r * sin(i / 2 / pi))
    moveObjectTo(obj17, xCobj17 + r * cos(i / 2 / pi), yCobj17 + r * sin(i / 2 / pi))
    moveObjectTo(obj18, xCobj18 + r * cos(i / 2 / pi), yCobj18 + r * sin(i / 2 / pi))
    moveObjectTo(obj19, xCobj19 + r * cos(i / 2 / pi), yCobj19 + r * sin(i / 2 / pi))
    moveObjectTo(obj20, xCobj20 + r * cos(i / 2 / pi), yCobj20 + r * sin(i / 2 / pi))
    moveObjectTo(obj21, xCobj21 + r * cos(i / 2 / pi), yCobj21 + r * sin(i / 2 / pi))
    moveObjectTo(obj22, xCobj22 + r * cos(i / 2 / pi), yCobj22 + r * sin(i / 2 / pi))
    moveObjectTo(obj23, xCobj23 + r * cos(i / 2 / pi), yCobj23 + r * sin(i / 2 / pi))
    moveObjectTo(obj24, xCobj24 + r * cos(i / 2 / pi), yCobj24 + r * sin(i / 2 / pi))
    moveObjectTo(obj25, xCobj25 + r * cos(i / 2 / pi), yCobj25 + r * sin(i / 2 / pi))
    moveObjectTo(obj26, xCobj26 + r * cos(i / 2 / pi), yCobj26 + r * sin(i / 2 / pi))
    moveObjectTo(obj27, xCobj27 + r * cos(i / 2 / pi), yCobj27 + r * sin(i / 2 / pi))
    moveObjectTo(obj28, xCobj28 + r * cos(i / 2 / pi), yCobj28 + r * sin(i / 2 / pi))
    moveObjectTo(obj29, xCobj29 + r * cos(i / 2 / pi), yCobj29 + r * sin(i / 2 / pi))
    moveObjectTo(obj30, xCobj30 + r * cos(i / 2 / pi), yCobj30 + r * sin(i / 2 / pi))
    moveObjectTo(obj31, xCobj31 + r * cos(i / 2 / pi), yCobj31 + r * sin(i / 2 / pi))
    moveObjectTo(obj32, xCobj32 + r * cos(i / 2 / pi), yCobj32 + r * sin(i / 2 / pi))
    moveObjectTo(obj33, xCobj33 + r * cos(i / 2 / pi), yCobj33 + r * sin(i / 2 / pi))
    moveObjectTo(obj34, xCobj34 + r * cos(i / 2 / pi), yCobj34 + r * sin(i / 2 / pi))
    moveObjectTo(obj35, xCobj35 + r * cos(i / 2 / pi), yCobj35 + r * sin(i / 2 / pi))
    moveObjectTo(obj36, xCobj36 + r * cos(i / 2 / pi), yCobj36 + r * sin(i / 2 / pi))
    moveObjectTo(obj37, xCobj37 + r * cos(i / 2 / pi), yCobj37 + r * sin(i / 2 / pi))
    moveObjectTo(obj38, xCobj38 + r * cos(i / 2 / pi), yCobj38 + r * sin(i / 2 / pi))

x=150
y=250
x2=40
y2=-38
width=40
higth=20
r=40
w=0.4
h=0.4
x1=150
y1=200
penSize(0)

obj=ellyps(x-width,y-higth,x+width,y+higth)
obj1=rectangle(x - int(0.8 * width), y, x - int(0.65 * width), y + 2.5 * higth)
obj2=rectangle(x - int(0.55 * width), y, x - int(0.4 * width), y + 2.2 * higth)
obj3=rectangle(x + int(0.8 * width), y, x + int(0.65 * width), y + 2.2 * higth)
obj4=rectangle(x + int(0.55 * width), y, x + int(0.4 * width), y + 2.5 * higth)
obj5=rectangle(x + int(0.35 * width), y, x + (0.85 * width), y - int(2.5 * higth))
obj6=ellyps(x + int(0.43 * width), y - int(2.7 * higth), x + int(0.87 * width), y - int(2.4 * higth))
obj7=ellyps(x + 0.5 * width, y - 2.45 * higth, x + 1.3 * width, y - 1.80 * higth)
brushColor(230, 129, 255)
obj8=circle(x + 0.75 * width, y - 2.3 * higth, 0.08 * width)
brushColor("black")
obj9=circle(x + 0.78 * width, y - 2.3 * higth, 0.03 * width)
brushColor(234, 177, 177)
penColor(234, 177, 177)
obj10=polygon([(x + 0.6 * width, y - 2.6 * higth), (x + 0.7 * width, y - 4.24 * higth), (x + 0.75 * width, y - 2.55 * higth),
         (x + 0.6 * width, y - 2.6 * higth)])

brushColor(234, 199, 177)
obj11=(ellyps(x1 + (w*15),y1 + (h*5), x1 + (w*55),y1 + (h*23)))
brushColor(234, 177, 177)
obj12=(ellyps(x1, y1, x1 + (w*45), y1 + (h*10)))
obj13=(ellyps(x1 + (w*30), y1 - (h*15), x1 + (w*60), y1 ))
brushColor(230, 255, 129)
obj14=(ellyps(x1 + (w*10),y1 + (h*50),x1 + (w*60), y1 + (h*65)))
brushColor(234, 199, 177)
obj15=(ellyps(x1 - (w*15), y1 + (h*5), x1 + (w*23), y1 + (h*30)))
obj16=(ellyps(x1, y1 + (h*35), x1 + (w*40), y1 + (h*55)))
brushColor(255, 239, 172)
obj17=(ellyps(x1 - w*30, y1 + h*25, x1 + w*25, y1 + h*45))
obj18=(ellyps(x1 - w*25, y1 + h*50, x1 + w*10, y1 + h*65))
brushColor(230, 255, 129)
obj19=ellyps(x1 - w*40, y1 + h*40, x1, y1 + h*55)
brushColor(176, 234, 222)
obj20=ellyps(x1 - w*40, y1 + h*60, x1 - w*10, y1 + h*70)
brushColor(244, 216, 228)
obj21=ellyps(x1 - w*15,y1 + h*58, x1 + w*30, y1 + h*70)
obj22=ellyps(x1 - w*15, y1 + h*68, x1 + w*30, y1 + h*80)
brushColor(176, 234, 222)
obj23=ellyps(x1, y1 + h*62, x1 + w*40, y1 + h*77)
brushColor(222, 177, 234)
obj24=ellyps(x1 - w*60, y1 + h*70, x1, y1 + h*85)

brushColor(234, 199, 177)
obj25=(ellyps(x1 + (w*15),y1 + (h*5), x1 + (w*55),y1 + (h*23)))
brushColor(234, 177, 177)
obj26=(ellyps(x1, y1, x1 + (w*45), y1 + (h*10)))
obj27=(ellyps(x1 + (w*30), y1 - (h*15), x1 + (w*60), y1 ))
brushColor(230, 255, 129)
obj28=(ellyps(x1 + (w*10),y1 + (h*50),x1 + (w*60), y1 + (h*65)))
brushColor(234, 199, 177)
obj29=(ellyps(x1 - (w*15), y1 + (h*5), x1 + (w*23), y1 + (h*30)))
obj30=(ellyps(x1, y1 + (h*35), x1 + (w*40), y1 + (h*55)))
brushColor(255, 239, 172)
obj31=(ellyps(x1 - w*30, y1 + h*25, x1 + w*25, y1 + h*45))
obj32=(ellyps(x1 - w*25, y1 + h*50, x1 + w*10, y1 + h*65))
brushColor(230, 255, 129)
obj33=ellyps(x1 - w*40, y1 + h*40, x1, y1 + h*55)
brushColor(176, 234, 222)
obj34=ellyps(x1 - w*40, y1 + h*60, x1 - w*10, y1 + h*70)
brushColor(244, 216, 228)
obj35=ellyps(x1 - w*15,y1 + h*58, x1 + w*30, y1 + h*70)
obj36=ellyps(x1 - w*15, y1 + h*68, x1 + w*30, y1 + h*80)
brushColor(176, 234, 222)
obj37=ellyps(x1, y1 + h*62, x1 + w*40, y1 + h*77)
brushColor(222, 177, 234)
obj38=ellyps(x1 - w*60, y1 + h*70, x1, y1 + h*85)

xCobj=xCoord(obj)
xCobj1=xCoord(obj1)
xCobj2=xCoord(obj2)
xCobj3=xCoord(obj3)
xCobj4=xCoord(obj4)
xCobj5=xCoord(obj5)
xCobj6=xCoord(obj6)
xCobj7=xCoord(obj7)
xCobj8=xCoord(obj8)
xCobj9=xCoord(obj9)
xCobj10=xCoord(obj10)
xCobj11=xCoord(obj11)
xCobj12=xCoord(obj12)
xCobj13=xCoord(obj13)
xCobj14=xCoord(obj14)
xCobj15=xCoord(obj15)
xCobj16=xCoord(obj16)
xCobj17=xCoord(obj17)
xCobj18=xCoord(obj18)
xCobj19=xCoord(obj19)
xCobj20=xCoord(obj20)
xCobj21=xCoord(obj21)
xCobj22=xCoord(obj22)
xCobj23=xCoord(obj23)
xCobj24=xCoord(obj24)
xCobj25=xCoord(obj25)-x2
xCobj26=xCoord(obj26)-x2
xCobj27=xCoord(obj27)-x2
xCobj28=xCoord(obj28)-x2
xCobj29=xCoord(obj29)-x2
xCobj30=xCoord(obj30)-x2
xCobj31=xCoord(obj31)-x2
xCobj32=xCoord(obj32)-x2
xCobj33=xCoord(obj33)-x2
xCobj34=xCoord(obj34)-x2
xCobj35=xCoord(obj35)-x2
xCobj36=xCoord(obj36)-x2
xCobj37=xCoord(obj37)-x2
xCobj38=xCoord(obj38)-x2

yCobj=yCoord(obj)
yCobj1=yCoord(obj1)
yCobj2=yCoord(obj2)
yCobj3=yCoord(obj3)
yCobj4=yCoord(obj4)
yCobj5=yCoord(obj5)
yCobj6=yCoord(obj6)
yCobj7=yCoord(obj7)
yCobj8=yCoord(obj8)
yCobj9=yCoord(obj9)
yCobj10=yCoord(obj10)
yCobj11=yCoord(obj11)
yCobj12=yCoord(obj12)
yCobj13=yCoord(obj13)
yCobj14=yCoord(obj14)
yCobj15=yCoord(obj15)
yCobj16=yCoord(obj16)
yCobj17=yCoord(obj17)
yCobj18=yCoord(obj18)
yCobj19=yCoord(obj19)
yCobj20=yCoord(obj20)
yCobj21=yCoord(obj21)
yCobj22=yCoord(obj22)
yCobj23=yCoord(obj23)
yCobj24=yCoord(obj24)
yCobj25=yCoord(obj25)-y2
yCobj26=yCoord(obj26)-y2
yCobj27=yCoord(obj27)-y2
yCobj28=yCoord(obj28)-y2
yCobj29=yCoord(obj29)-y2
yCobj30=yCoord(obj30)-y2
yCobj31=yCoord(obj31)-y2
yCobj32=yCoord(obj32)-y2
yCobj33=yCoord(obj33)-y2
yCobj34=yCoord(obj34)-y2
yCobj35=yCoord(obj35)-y2
yCobj36=yCoord(obj36)-y2
yCobj37=yCoord(obj37)-y2
yCobj38=yCoord(obj38)-y2

onTimer(update, 15)
run()
