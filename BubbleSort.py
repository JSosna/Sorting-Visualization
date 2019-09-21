#  Copyright © 2019, Jakub Sosna, All rights reserved.

import pygame as pg
import random

pg.init()

size = (1600, 900)
bg = (120, 120, 180)
line_color = (230, 230, 230)

i = 0
j = 0

root = pg.display.set_mode(size, pg.FULLSCREEN)
pg.display.set_caption("Bubble Sort Visualization")


def setup():
    v = []
    while len(v) < size[0]:
        v.append(random.randint(0, 900))
    return v


def draw():
    root.fill(bg)

    global i, j
    print("i:", i, "j:", j)
    if i < len(values):
        if values[j] > values[j+1]:
            values[j], values[j+1] = values[j+1], values[j]

        j += 1

        if j >= len(values)-i-1:
            j = 0
            i += 1
        print("s", i)

    for x in range(size[0]):
        pg.draw.line(root, line_color, (x, size[1]), (x, size[1]-values[x]))


def bubble_sort():
    for x in range(len(values)):
        for y in range(0, len(values)-x-1):
            if values[y] > values[y+1]:
                values[y], values[y+1] = values[y+1], values[y]


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

    # bubble_sort()
    draw()
    pg.display.update()
    clock.tick(60)
