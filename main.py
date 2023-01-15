import pygame

from script.game import main_game
from script.menu import introductory_menu
from script.config import SIZE


pygame.init()

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
clock.tick(60)

now_screen = 'start'
while True:
    if now_screen == 'start':
        now_screen = 'level1' if introductory_menu(screen, clock) else 'settings'
    if now_screen == 'level1':
        main_game(1, screen, clock)
