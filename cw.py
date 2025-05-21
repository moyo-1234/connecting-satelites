import pgzrun
from time import time
from random import randint

HEIGHT = 650
WIDTH = 700

satelites = []
lines = []
satelite_num = 8


def draw():
    screen.blit("background", (0,0))


def create_staelite():
    for i in range(satelite_num):
        s = Actor("satelite")
        s.pos = randint(50,640),randint(50,680)
        satelites.append(s)






pgzrun.go()