import pygame as pg
import pygame.gfxdraw as pggfx
import time
import Sand




pg.display.init()
size = width, height = 50, 50
screen = pg.display.set_mode(size=size, flags=pg.SCALED | pg.RESIZABLE)
color = (255,255,255,0)
done = False
y = int(height/2)
pixelColor = (0, 0, 0)

while not done:
    for event in pg.event.get(): #See all events in window
        if event.type == pg.QUIT: #Check if user want close window
            done = True
    pg.display.update()
    screen.fill(color)

    Sand.SandPixel(screen=screen, x=int(width/2), y=y) #Creating Pixel
    if y < height-1:
        y += 1
    time.sleep(0.5)

pg.display.quit()
