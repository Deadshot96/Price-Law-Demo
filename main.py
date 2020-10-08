import os
import math
import random
import pygame
import time
from settings import *
from colors import *

def main():

    # init
    pygame.init()
    pygame.font.init()

    # Clock init
    clock = pygame.time.Clock()

    # Main and graph window init
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Price's Law")
    graphWin = win.subsurface((X_OFF, Y_OFF, GRAPH_WIDTH, GRAPH_HEIGHT))
    win.fill(MID_BLACK)
    graphWin.fill(SKYBLUE)

    # Font init
    font = pygame.font.SysFont("comicsansms", 40)
    text = font.render(TEXT, 1, GOLD)

    # Blit text
    x = (win.get_width() - text.get_width()) // 2
    y = (Y_OFF - text.get_height()) // 2
    win.blit(text, (x, y))

    def reset():
        pass

    start = False

    run = True
    while run:
        clock.tick(FPS)

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                
                keys = pygame.key.get_pressed()

                if keys[pygame.K_SPACE]:
                    start = True

                if keys[pygame.K_ESCAPE]:
                    reset()
        
        if start:
            pass

    
    pygame.font.quit()
    pygame.quit()


if __name__ == "__main__":
    main()