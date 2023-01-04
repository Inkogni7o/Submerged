import pygame

from game import main_game
from settings import get_monitor_size, SIZE

pygame.init()
get_monitor_size()

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()



main_game(screen, clock)
