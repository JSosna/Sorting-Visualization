#  Copyright © 2019, Jakub Sosna, All rights reserved.

import pygame as pg
import random

pg.init()

size = (1600, 900)
bg = (120, 120, 180)
line_color = (230, 230, 230)

root = pg.display.set_mode(size, pg.FULLSCREEN)
pg.display.set_caption("Bubble Sort Visualization")


def setup():
    v = []
    while len(v) < size[0]:
        v.append(random.randint(0, 900))
    return v


def draw():
    root.fill(bg)
    i = 0
    while i < size[0]:
        pg.draw.line(root, line_color, (i, size[1]), (i, size[1]-values[i]))
        i += 1


clock = pg.time.Clock()
finished = False

values = setup()

setup()
while not finished:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                quit()

    draw()
    pg.display.update()
    clock.tick(60)
