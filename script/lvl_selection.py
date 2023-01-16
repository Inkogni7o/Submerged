from sys import exit
import pygame

from script.buttons import Button
from script.config import SIZE
from script.main_player import AI_Player


def lvl_selection(screen: pygame.display, bubbles: list, ai_player: AI_Player) -> str:
    with open('src/saves/main_save.txt', 'r', encoding='utf-8') as file:
        for string in str(file.read()).split('\n'):
            if string.split(':')[0] == 'save':
                level = int(string.split(':')[1])
    c_blocked = (23, 40, 143)
    buttons = [Button('Назад', (45, 170, 201), (226, 149, 61), 30, 30, 200, 100),
               Button('1 уровень', (45, 170, 201), (226, 149, 61), 450, 700, 300, 100),
               Button('2 уровень', (45, 170, 201) if level >= 2 else c_blocked, (226, 149, 61)
               if level >= 2 else c_blocked, 850, 700, 300, 100),
               Button('3 уровень', (45, 170, 201) if level >= 3 else c_blocked, (226, 149, 61)
               if level >= 2 else c_blocked, 1250, 700, 300, 100)]
    image_bg = pygame.transform.scale(pygame.image.load('src/backgrounds/menu_bg.png'), SIZE)
    image_level1 = pygame.transform.scale(pygame.image.load('src/backgrounds/level1_preview.png'), (300, 300))
    image_level2 = (pygame.transform.scale(pygame.image.load('src/backgrounds/level2_preview.png'), (300, 300))
                    if level >= 2 else pygame.transform.scale(pygame.image.load('src/backgrounds/locked_preview.png'),
                                                              (300, 300)))
    image_level3 = (pygame.transform.scale(pygame.image.load('src/backgrounds/level3_preview.png'), (300, 300))
                    if level >= 3 else pygame.transform.scale(pygame.image.load('src/backgrounds/locked_preview.png'),
                                                              (300, 300)))

    while True:
        screen.blit(image_bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.mouse_on_btn(*pygame.mouse.get_pos()):
                        if button.text_btn == 'Назад':
                            return 'game_menu'
                        if button.text_btn == '1 уровень':
                            return 'level1'
                        if button.text_btn == '2 уровень' and level >= 2:
                            pass
                        if button.text_btn == '3 уровень' and level >= 3:
                            pass

        for bubble in bubbles:
            bubble.draw(screen)
            bubble.update()
        ai_player.draw()
        ai_player.move_player(5, 0)

        for button in buttons:
            button.draw(screen, *pygame.mouse.get_pos())
        screen.blit(image_level1, (450, 350))
        screen.blit(image_level2, (850, 350))
        screen.blit(image_level3, (1250, 350))
        pygame.display.flip()