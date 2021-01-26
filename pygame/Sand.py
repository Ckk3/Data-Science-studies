import pygame.gfxdraw as pggfx
import pygame as pg
import time

class SandPixel:
    def __init__(self, screen, x=0, y=0):
        self.x = x
        self.y = y
        pggfx.pixel(screen, x, y, (0,0,0))


