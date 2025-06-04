import pgzrun
from time import time
from random import randint

HEIGHT = 650
WIDTH = 700

satelites = []
lines = []
satelite_num = 8
next_satelite = 0

def draw():
    screen.blit("background", (0,0))
    m = 1
    for i in satelites:
        i.draw()
        screen.draw.text(str(m),(i.pos[0],i.pos[1]+20))
        m=m+1


def create_satelite():
    for i in range(satelite_num):
        s = Actor("satelite")
        s.pos = randint(50,640),randint(50,680)
        satelites.append(s)

def on_mouse_down(pos):
    global next_satelite,lines
    if next_satelite < satelite_num:
        if satelites[next_satelite].collidepoint(pos):
            lines.append(satelites[next_satelite-1].pos,satelites[next_satelite].pos)
            next_satelite=next_satelite+1
        

create_satelite()



pgzrun.go()