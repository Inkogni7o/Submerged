import pygame
from sys import exit

from buttons import Button


def introductory_menu(screen: pygame.display, clock: pygame.time.Clock):
    buttons = [Button('Начать игру!', 'green', 'red', 1450, 700, 400, 100),
               Button('Настройки', 'green', 'red', 1450, 850, 400, 100),
               Button('Выйти', 'green', 'red', 1450, 1000, 400, 100)]
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.mouse_on_btn(*pygame.mouse.get_pos()):
                        if button.text_btn == 'Выйти':
                            pygame.quit()
                            exit()
                        if button.text_btn == 'Начать игру!':
                            return True
                        if button.text_btn == 'Настройки':
                            return False
        for button in buttons:
            button.draw(screen, *pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(60)
