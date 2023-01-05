import pygame
from sys import exit
from main_player import MainPlayer


def main_game(screen: pygame.display, clock: pygame.time.Clock):
    player = MainPlayer(50, 50)
    player_group = pygame.sprite.Group()
    player_group.add(player)
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(60)
