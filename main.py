import pygame

from game import main_game
from menu import introductory_menu
from settings import settings_screen
from config import get_monitor_size

pygame.init()
SIZE = get_monitor_size()

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

now_screen = 'start'
while True:
    if now_screen == 'start':
        now_screen = 'level1' if introductory_menu(screen, clock) else 'settings'
    if now_screen == 'settings':
        if settings_screen(screen, clock):
            now_screen = 'start'
    if now_screen == 'level1':
        main_game(screen, clock)
