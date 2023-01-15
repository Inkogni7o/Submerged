import pygame
from sys import exit

from script.config import SIZE
from script.buttons import Button
from script.main_player import AI_Player


def introductory_menu(screen: pygame.display, bubbles: list, player: AI_Player):
    buttons = [Button('Начать игру', (45, 170, 201), (226, 149, 61), 1380, 800, 480, 100),
               Button('Выйти', (45, 170, 201), (226, 149, 61), 1380, 950, 480, 100)]
    image = pygame.transform.scale(pygame.image.load('src/backgrounds/menu_bg.png'), SIZE)
    while True:
        screen.blit(image, (0, 0))
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
                        elif button.text_btn == 'Начать игру':
                            return True
        for bubble in bubbles:
            bubble.draw(screen)
            bubble.update()
        player.draw()
        player.move_player(5, 0)
        for button in buttons:
            button.draw(screen, *pygame.mouse.get_pos())
        pygame.display.flip()
