from graph import *
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


def body(x, y, width, higth):
    brushColor("white")
    ellyps(x - width, y - higth, x + width, y + higth)
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
body(250, 500, 70, 30)
mane(264, 425, 0.6, 0.6)

mane(500, 375, -0.6, 0.6)# horse2
mane(500, 395, -0.6, 0.6)
body(425, 395, -65, 25)
mane(415, 335, -0.55, 0.55)

mane(280, 250, 0.5, 0.5)# horse3
mane(285, 270, -0.4, 0.4)
body(330, 260, 40, 20)
mane(333, 210, 0.4, 0.4)

mane(490, 235, -0.2, 0.2)# horse4
mane(490, 245, 0.2, 0.2)
body(460, 240, -25, 10)
mane(456, 215, -0.2, 0.2)

penSize(1)
for i in range(110):
    penColor(i*2, 255, 255 - i*2)
    brushColor(i*2, 255, 255 - i*2)
    circle(410, 70, 110-i)

run()