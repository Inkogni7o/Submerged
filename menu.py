import pygame
from sys import exit


def menu(screen: pygame.display, clock: pygame.time.Clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)
