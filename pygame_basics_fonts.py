import pygame
import sys
from pygame.locals import *

pygame.init()

display_surf = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hippity Hoppity !!")

white = (255,255,255)
green = (0,255,0)
blue = (0,0,255)

font_obj = pygame.font.Font('freesansbold.ttf',32)
text_surface_obj = font_obj.render("It's Free Real Estate", True, green, blue)
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (200,150)

while True:
    display_surf.fill(white)
    display_surf.blit(text_surface_obj, text_rect_obj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()