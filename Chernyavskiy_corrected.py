from graph import *
import math
c=canvas()
windowSize(700,700)
def ellipse(x, y, a, b, f):
    f = f * math.pi / 180
    x_e = [i for i in range(-a, a)]
    y1, y2 = [], []
    for i in range(len(x_e)):
        xy1 = [x_e[i], b * (1 - (x_e[i] / a)**2)**0.5]
        xy2 = [x_e[i], -b * (1 - (x_e[i] / a)**2)**0.5]
        xy1 = [xy1[0] * math.cos(f) - xy1[1] * math.sin(f), xy1[0]
               * math.sin(f) + xy1[1] * math.cos(f)]
        xy2 = [xy2[0] * math.cos(f) - xy2[1] * math.sin(f), xy2[0]
               * math.sin(f) + xy2[1] * math.cos(f)]
        y1.append((xy1[0] + x, xy1[1] + y))
        y2.append((xy2[0] + x, xy2[1] + y))
    y2 = y2[::-1]
    polygon(y1 + y2)
penColor('black')
brushColor('grey')
rectangle(0,0,2000,300)
penColor('grey')
brushColor('white')
circle(120,340,90)
for i in range (6):
    line(30+2*i, 340-90/(6)*i, 210-2*i, 340-90/(6)*i)
    for m in range(10):
        if (40 + 5*i + m * 21) < 210:
            line(40+ 5*i + m*21, 340-i*15, 40 + 5*i + m*21, 340-(i+1)*15)


penColor('white')
brushColor('white')
rectangle(15,340,230,450)
penColor("black")
penColor('white')
c.create_oval(290,325,390,475, outline='#696969',fill='#696969',width=1)#tulovische
rectangle(290,415,390,515)
penColor('#2F4F4F')
brushColor('#2F4F4F')
rectangle(330,340,350,425)
c.create_oval(300,450,335,470, outline='#696969',fill='#696969',width=1)#steps
c.create_oval(345,450,380,470, outline='#696969',fill='#696969',width=1)
c.create_oval(315,410,335,465, outline='#696969',fill='#696969',width=1)#foot
c.create_oval(345,410,365,465, outline='#696969',fill='#696969',width=1)
rectangle(290,415,390,425)
brushColor('#C0C0C0')
circle(340,320,40)
brushColor('#696969')
circle(340,320,30)
brushColor('#DCDCDC')
circle(340,322,25)#golova
line(327,313,338,320)#glaza
line(353,313,342,320)
polyline([(329,331),(333,328),(337,327),(341,327),(345,328),(349,331)])#rot
brushColor('#696969')
penColor('#696969')
ellipse(280, 365, 35, 8, 169)#ruka
ellipse(395, 375, 35, 8, 45)
line(256,285,256,460)
c.create_oval(70,400,140,425, outline='#696969',fill='#696969',width=1)#koshka
brushColor('#696969')
circle(69,400,15)
polygon([(71,387),(73,381),(77,389)])
polygon([(61,389),(63,381),(65,387)])
brushColor('white')
circle(64,396,4)
circle(74,396,4)
brushColor('black')
circle(66,396,2)
circle(76,396,2)
c.create_oval(77,413,85,447, outline='#696969',fill='#696969',width=1)#lapka
c.create_oval(91,413,100,447, outline='#696969',fill='#696969',width=1)
c.create_oval(116,413,125,447, outline='#696969',fill='#696969',width=1)
c.create_oval(128,413,137,447, outline='#696969',fill='#696969',width=1)
c.create_oval(130,375,140,425, outline='#696969',fill='#696969',width=1)#khvost
run()
