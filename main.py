import pygame

from game import main_game
from menu import introductory_menu
from settings import get_monitor_size, SIZE

pygame.init()
get_monitor_size()

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

if introductory_menu(screen, clock):
    main_game(screen, clock)
