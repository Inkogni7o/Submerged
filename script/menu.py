import pygame
from sys import exit

from buttons import Button


def introductory_menu(screen: pygame.display, clock: pygame.time.Clock):
    buttons = [Button('Начать игру!', (45, 170, 201), (226, 149, 61), 1450, 650, 400, 100),
               Button('Настройки', (45, 170, 201), (226, 149, 61), 1450, 800, 400, 100),
               Button('Выйти', (45, 170, 201), (226, 149, 61), 1450, 950, 400, 100)]
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
                        elif button.text_btn == 'Начать игру!':
                            return True
                        elif button.text_btn == 'Настройки':
                            return False
        for button in buttons:
            button.draw(screen, *pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(60)
