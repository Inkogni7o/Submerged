import pygame
from sys import exit

from buttons import Button


def introductory_menu(screen: pygame.display, clock: pygame.time.Clock):
    buttons = list()
    buttons.append(Button('Начать игру!', 'green', 'red', 1450, 700, 400, 100))
    buttons.append(Button('Настройки', 'green', 'red', 1450, 850, 400, 100))
    buttons.append(Button('Выйти', 'green', 'red', 1450, 1000, 400, 100))
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        for button in buttons:
            button.draw(screen, *pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(60)
