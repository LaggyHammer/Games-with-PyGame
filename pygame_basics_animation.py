import pygame
import sys
from pygame.locals import *

pygame.init()

fps = 30
fps_clock = pygame.time.Clock()

display_surf = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption("Animation")

white = (255,255,255)
cat_image = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

while True:
    display_surf.fill(white)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    display_surf.blit(cat_image, (catx,caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    fps_clock.tick(fps)