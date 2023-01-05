import pygame

from game import main_game
from menu import introductory_menu
from settings import get_monitor_size, SIZE

pygame.init()
get_monitor_size()

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

now_screen = 'start'
while True:
    if now_screen == 'start':
        if introductory_menu(screen, clock):
            now_screen = 'level1'
        else:
            now_screen = 'settings'
    if now_screen == 'level1':
        main_game(screen, clock)
