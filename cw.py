import pgzrun
from time import time
from random import randint

HEIGHT = 700
WIDTH = 700

satelites = []
lines = []
satelite_num = 8
next_satelite = 0
start_time = 0
total_time = 0
end_time = 0

def draw():
    global total_time
    screen.blit("background", (0,0))
    m = 1
    for i in lines:
        screen.draw.line(i[0],i[1],"Blue")
    if next_satelite < satelite_num:
        total_time=time()-start_time
        screen.draw.text(str(round(total_time,3)),(20,20),fontsize = 30)
    else:
        screen.draw.text(str(round(total_time,3)),(20,20),fontsize = 30)    

    for i in satelites:
        i.draw()
        screen.draw.text(str(m),(i.pos[0],i.pos[1]+20))
        m=m+1


def create_satelite():
    global start_time
    for i in range(satelite_num):
        s = Actor("satelite")
        s.pos = randint(50,640),randint(50,640)
        satelites.append(s)
    start_time = time()
    

def on_mouse_down(pos):
    global next_satelite,lines
    if next_satelite < satelite_num:
        if satelites[next_satelite].collidepoint(pos):
            if next_satelite:

                lines.append((satelites[next_satelite-1].pos,satelites[next_satelite].pos))
            next_satelite=next_satelite+1
        else:
            lines = []
            next_satelite = 0

create_satelite()



pgzrun.go()