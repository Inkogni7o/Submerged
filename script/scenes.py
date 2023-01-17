import random
from sys import exit

import pygame

from script.config import SIZE
from script.environment import Bubble
from script.text import Text


def scene(num_scene: int, screen: pygame.display, player, player_group):
    if num_scene == 1:
        image = pygame.transform.scale(pygame.image.load('src/backgrounds/scene_1_1_bg.png'), SIZE)
        text = Text('В один прекрасный момент все побережье Америки накрыли цунами', True)
        now_text = 1
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if now_text == 1:
                        if not text.end:
                            text.end, text.string_index = True, len(text.text)
                        else:
                            text.change_text('Вам нужно определить причину и по возможности устранить')
                            now_text = 2
                    elif now_text == 2:
                        if not text.end:
                            text.end, text.string_index = True, len(text.text)
                        else:
                            return

            screen.blit(image, (0, 0))
            text.draw(screen)
            pygame.display.flip()

    if num_scene == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        player.move, player.move_map, player.right = False, False, False
        player.rect.y += 3
        player.update_spr()
        player_group.draw(screen)
        player.bubbles_timer -= 1

        # завершение кат сцены
        if player.rect.y > SIZE[1]:
            return True

        # продолжаем отрисовку пузырей
        for bubble in player.bubbles:
            bubble.draw(player.screen)
            bubble.update()
            if player.move_map and player.move:
                bubble.position = [bubble.position[0] - player.speed, bubble.position[1]] \
                    if player.right else [bubble.position[0] + player.speed, bubble.position[1]]
            if bubble.death is not None:
                if bubble.death == 0 or bubble.position[0] < 0:
                    player.bubbles.pop(player.bubbles.index(bubble))
        if player.bubbles_timer == 0:
            for _ in range(3):
                if player.right:
                    player.bubbles.append(
                        Bubble(SIZE, [random.randint(player.rect.x - 5, player.rect.x + 5),
                                      random.randint(player.rect.y + 10,
                                                     player.rect.y + player.rect.height - 10)], True))
                else:
                    player.bubbles.append(
                        Bubble(SIZE, [random.randint(player.rect.x + player.rect.width - 5,
                                                     player.rect.x + player.rect.width + 5),
                                      random.randint(player.rect.y + 10,
                                                     player.rect.y + player.rect.height - 10)], True))
            player.bubbles_timer = 4
        return False

    if num_scene == 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        player.move, player.move_map, player.right = False, False, True
        player.rect.x += 3
        player.update_spr()
        player_group.draw(screen)
        player.bubbles_timer -= 1

        # завершение кат сцены
        if player.rect.x > SIZE[0] - 600:
            return True

        # продолжаем отрисовку пузырей
        for bubble in player.bubbles:
            bubble.draw(player.screen)
            bubble.update()
            if player.move_map and player.move:
                bubble.position = [bubble.position[0] - player.speed, bubble.position[1]] \
                    if player.right else [bubble.position[0] + player.speed, bubble.position[1]]
            if bubble.death is not None:
                if bubble.death == 0 or bubble.position[0] < 0:
                    player.bubbles.pop(player.bubbles.index(bubble))
        if player.bubbles_timer == 0:
            for _ in range(3):
                if player.right:
                    player.bubbles.append(
                        Bubble(SIZE, [random.randint(player.rect.x - 5, player.rect.x + 5),
                                      random.randint(player.rect.y + 10,
                                                     player.rect.y + player.rect.height - 10)], True))
                else:
                    player.bubbles.append(
                        Bubble(SIZE, [random.randint(player.rect.x + player.rect.width - 5,
                                                     player.rect.x + player.rect.width + 5),
                                      random.randint(player.rect.y + 10,
                                                     player.rect.y + player.rect.height - 10)], True))
            player.bubbles_timer = 4
        return False

    if num_scene == 4:
        image = pygame.transform.scale(pygame.image.load('scene4.jpg'), SIZE)
        text = Text('Что это или кто - не понятно. И зачем они это делали - не понятно.', True)
        now_text = 1
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if now_text == 1:
                        if not text.end:
                            text.end, text.string_index = True, len(text.text)
                        else:
                            text.change_text('Это нам и предстоит узнать!')
                            now_text = 2
                    elif now_text == 2:
                        if not text.end:
                            text.end, text.string_index = True, len(text.text)
                        else:
                            return

            screen.blit(image, (0, 0))
            text.draw(screen)
            pygame.display.flip()