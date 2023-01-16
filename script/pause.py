from sys import exit
import pygame

from script.config import SIZE
from script.buttons import Button


def pause_screen(screen: pygame.display, clock: pygame.time.Clock):
    bg = pygame.image.load('src/backgrounds/pause_bg.png')
    bg = pygame.transform.scale(bg, SIZE)
    buttons = [Button('Продолжить', (45, 170, 201), (226, 149, 61), 700, 400, 500, 100),
               Button('Начать заново', (45, 170, 201), (226, 149, 61), 700, 550, 500, 100),
               Button('Выйти из игры', (45, 170, 201), (226, 149, 61), 700, 700, 500, 100)]
    while True:
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.mouse_on_btn(*pygame.mouse.get_pos()):
                        if button.text_btn == 'Продолжить':
                            return True
                        elif button.text_btn == 'Начать заново':
                            return False
                        elif button.text_btn == 'Выйти из игры':
                            pygame.quit()
                            exit()
        for button in buttons:
            button.draw(screen, *pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(60)