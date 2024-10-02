import pygame
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
SCREEN_WIDHT, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    screen.fill("purple")

    pygame.display.flip()

    clock.tick(60)  
pygame.quit()
