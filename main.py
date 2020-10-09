import os
import math
import random
import pygame
import time
from settings import *
from colors import *

player_list = list()


X_AXIS = ((AXIS_OFF, GRAPH_HEIGHT - AXIS_OFF),\
    (GRAPH_WIDTH - AXIS_OFF, GRAPH_HEIGHT - AXIS_OFF))

Y_AXIS = ((AXIS_OFF, AXIS_OFF), (AXIS_OFF, GRAPH_HEIGHT - AXIS_OFF))


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
    graphWin.fill(MINT_CREAM)

    # Font init
    font = pygame.font.SysFont("comicsansms", 40)
    text = font.render(TEXT, 1, GOLD)

    # Blit text
    x = (win.get_width() - text.get_width()) // 2
    y = (Y_OFF - text.get_height()) // 2
    win.blit(text, (x, y))

    # setting variables
    

    def reset():
        global player_list
        player_list = [INITIAL_SUM] * PLAYERS_NOS

    def histogarm():
        global player_list
        
        s = set(player_list)
        d = dict()
        for i in s:
            d[i] = player_list.count(i)

        return d

        
    def draw():
        global player_list
        graphWin.fill(MINT_CREAM)
        hist = histogarm()

        pygame.draw.line(graphWin, BLACK, X_AXIS[0], X_AXIS[1], 2)
        pygame.draw.line(graphWin, BLACK, Y_AXIS[0], Y_AXIS[1], 2)

        for i in sorted(hist):
            val = hist[i]

            if i < MAX_RANGE:
                x = AXIS_OFF + GRP_X_MUL * (i + 1) - GRP_WID
                w = GRP_WID
                h = val * GRP_Y_MUL
                y = GRAPH_HEIGHT - AXIS_OFF - h
                
                pygame.draw.rect(graphWin, ORCHID, (x, y, w, h), 0)

        pygame.display.update()

    def bet():
        global player_list
        for i in range(len(player_list) - 1):
            for j in range(i + 1, len(player_list)):

                if player_list[i] == 0 or player_list[j] == 0:
                    continue

                bet = random.random()

                if bet < 0.5:
                    player_list[i] += 1
                    player_list[j] -= 1
                else:
                    player_list[i] -= 1
                    player_list[j] += 1


    start = False
    reset()
    run = True
    while run:
        clock.tick(FPS)
        global player_list
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                
                keys = pygame.key.get_pressed()

                if keys[pygame.K_SPACE]:
                    start = not start

                if keys[pygame.K_ESCAPE]:
                    reset()
                    start = False
        
        if start:
            # print(player_list)
            bet()
            
        draw()
    
    pygame.font.quit()
    pygame.quit()


if __name__ == "__main__":
    main()