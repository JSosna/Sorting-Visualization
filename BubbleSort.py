#  Copyright © 2019, Jakub Sosna, All rights reserved.

import pygame as pg

pg.init()

size = (1600, 900)
bg = (120, 120, 180)

root = pg.display.set_mode(size, pg.FULLSCREEN)
pg.display.set_caption("Bubble Sort Visualization")

clock = pg.time.Clock()
finished = False

while not finished:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                quit()

    root.fill(bg)
    pg.display.update()
    clock.tick(60)
