import pygame
from sys import exit
from buttons import Button


def settings_screen(screen: pygame.display, clock: pygame.time.Clock):
    button = Button('Назад', (45, 170, 201), (226, 149, 61), 30, 30, 200, 100)
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.mouse_on_btn(*pygame.mouse.get_pos()):
                    return True
        button.draw(screen, *pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(60)