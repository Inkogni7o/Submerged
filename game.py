import pygame


def main_game(screen: pygame.display, clock: pygame.time.Clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)