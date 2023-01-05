import pygame
from sys import exit

from buttons import Button
from main_player import MainPlayer


def introductory_menu(screen: pygame.display, clock: pygame.time.Clock):
    buttons = list()
    buttons.append(Button('Начать игру!', 'green', 'red', 1450, 700, 400, 100))
    buttons.append(Button('Настройки', 'green', 'red', 1450, 850, 400, 100))
    buttons.append(Button('Выйти', 'green', 'red', 1450, 1000, 400, 100))
    player = MainPlayer(50, 50)
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.mouse_on_btn(*pygame.mouse.get_pos()):
                        if button.text_btn == 'Выйти':
                            pygame.quit()
                            exit()
                        if button.text_btn == 'Начать игру!':
                            return True
        for button in buttons:
            button.draw(screen, *pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(60)
