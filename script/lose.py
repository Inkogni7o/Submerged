from sys import exit
import pygame

from script.config import SIZE
from script.text import Text


def lose_screen(screen: pygame.display, clock: pygame.time.Clock):
    bg = pygame.image.load('src/backgrounds/lose_bg.png')
    bg = pygame.transform.scale(bg, SIZE)
    text = Text('Вы старались как могли... Но так и не смогли покорить глубины и спасти мир', True)
    screen.blit(bg, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text.end:
                    return 'game_menu'
                else:
                    text.end, text.string_index = True, len(text.text)
        text.draw(screen)
        pygame.display.flip()
        clock.tick(60)