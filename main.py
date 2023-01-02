import pygame
from sys import exit

from settings import get_monitor_size, SIZE

pygame.init()
get_monitor_size()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


while True:
    pass