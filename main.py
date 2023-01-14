import pygame

from script.game import main_game
from script.menu import introductory_menu
from script.config import get_monitor_size


pygame.init()

screen = pygame.display.set_mode(get_monitor_size())
clock = pygame.time.Clock()
clock.tick(120)

now_screen = 'start'
while True:
    if now_screen == 'start':
        now_screen = 'level1' if introductory_menu(screen, clock) else 'settings'
    if now_screen == 'level1':
        main_game(screen, clock)
