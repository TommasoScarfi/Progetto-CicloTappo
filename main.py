import pygame
import random
import math

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

   
    screen.fill("dark green")
   
    pygame.draw.line(screen, (0, 0, 0), (100,400), (500,400), 5)
    pygame.draw.line(screen, (0, 0, 0), (100,500), (530,500), 5)
    pygame.draw.line(screen, (0, 0, 0), (500,400), (500,310), 5)
    pygame.draw.line(screen, (0, 0, 0), (530,500), (530,340), 5)
    pygame.draw.line(screen, (0, 0, 0), (530,340), (620,340), 5)
    pygame.draw.line(screen, (0, 0, 0), (500,310), (620,310), 5)
    pygame.draw.line(screen, (0, 0, 0), (620,310), (620,280), 5)
    pygame.draw.line(screen, (0, 0, 0), (620,340), (620,370), 5)
    pygame.draw.line(screen, (0, 0, 0), (620,280), (770,280), 5)
    pygame.draw.line(screen, (0, 0, 0), (620,370), (775,370), 5)
    BLACK = (0, 0, 0)
    pygame.draw.arc(screen, BLACK, pygame.Rect(765, 170, 300, 300), math.radians(280), math.radians(175), 3)
    pygame.draw.arc(screen, BLACK, pygame.Rect(765, 170, 300, 300), math.radians(190), math.radians(260), 3)
    pygame.draw.line(screen, (0, 0, 0), (890,465), (890,600), 5)
    pygame.draw.line(screen, (0, 0, 0), (940,465), (940,600), 5)
    pygame.draw.line(screen, (0, 0, 0), (890,600), (820,600), 5)
    pygame.draw.line(screen, (0, 0, 0), (940,600), (1060,600), 5)
    pygame.draw.line(screen, (0, 0, 0), (820,600), (820,690), 5)
    pygame.draw.line(screen, (0, 0, 0), (820,690), (1060,690), 5)
    pygame.draw.line(screen, (0, 0, 0), (1060,690), (1060,698), 5)
    pygame.draw.line(screen, (0, 0, 0), (1060,600), (1060,593), 5)
    pygame.draw.line(screen, (0, 0, 0), (1060,698), (1110,698), 5)
    pygame.draw.line(screen, (0, 0, 0), (1060,593), (1110,593), 5)
    pygame.draw.line(screen, (0, 0, 0), (1110,593), (1110,698), 5)
    pygame.draw.line(screen, (0, 0, 0), (1090,593), (1090,698), 5)
    pygame.draw.line(screen, (0, 0, 0), (940,645), (1060,645), 5)



















        




    





    pygame.display.flip()

    clock.tick(60)  
pygame.quit()
