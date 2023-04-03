import pygame as py
import random

#Game Window
WIN = py.display.set_mode((800,700))
clock = py.time.Clock()

#Background
background_image = py.image.load("Resources/desert2.jpg")

#Game Looping
running = True
while running:
    for event in py.event.get():
        if event.type is py.QUIT:
            running = False
    
    py.display.flip()
    WIN.blit(background_image,(0,0))
    clock.tick(60)

py.quit()
