import pygame

from script.buttons import Button
from script.config import SIZE
from script.main_player import AI_Player


def lvl_selection(screen: pygame.display, bubbles: list, ai_player: AI_Player) -> str:
    buttons = [Button('Назад', (45, 170, 201), (226, 149, 61), 30, 30, 200, 100),
               Button('1 уровень', (45, 170, 201), (226, 149, 61), 450, 700, 300, 100),
               Button('1 уровень', (45, 170, 201), (226, 149, 61), 850, 700, 300, 100),
               Button('1 уровень', (45, 170, 201), (226, 149, 61), 1250, 700, 300, 100)]
    image = pygame.transform.scale(pygame.image.load('src/backgrounds/menu_bg.png'), SIZE)
    with open('src/saves/main_save.txt', 'r', encoding='utf-8') as file:
        for string in str(file.read()).split('\n'):
            if string.split(':')[0] == 'save':
                level = string.split(':')[1]

    while True:
        screen.blit(image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.mouse_on_btn(*pygame.mouse.get_pos()):
                        if button.text_btn == 'Назад':
                            return 'game_menu'

        for bubble in bubbles:
            bubble.draw(screen)
            bubble.update()
        ai_player.draw()
        ai_player.move_player(5, 0)
        for button in buttons:
            button.draw(screen, *pygame.mouse.get_pos())
        pygame.display.flip()