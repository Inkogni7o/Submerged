import pygame
from main_player import MainPlayer


def main_game(screen: pygame.display, clock: pygame.time.Clock):
    player = MainPlayer(50, 50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            player.blit(screen)
        screen.fill((255, 255, 255))
        pygame.display.flip()
        clock.tick(60)
