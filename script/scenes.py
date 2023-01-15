import random
from sys import exit

import pygame

from script.config import SIZE
from script.environment import Bubble
from script.main_player import MainPlayer


def scene(num_scene: int, screen: pygame.display, player: MainPlayer, player_group):
    if num_scene == 1:
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
