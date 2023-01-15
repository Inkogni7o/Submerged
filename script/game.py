import random

import pygame
from sys import exit

import pytmx

from script.config import SIZE
from script.main_player import MainPlayer
from script.pause import pause_screen
from script.environment import Wall, Bubble
from script.enemies import Cuttlefish


def main_game(level, screen: pygame.display, clock: pygame.time.Clock, player_pos: tuple):
    player = MainPlayer(screen, *player_pos)
    player_group = pygame.sprite.Group()
    player_group.add(player)
    bullets_group = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    pause = False

    game_map = pytmx.load_pygame(f'src/levels/level{level}.tmx')
    walls_group = pygame.sprite.Group()
    for layer in game_map.visible_layers:
        try:
            if layer.name == 'walls':
                for cell in layer:
                    wall = Wall(cell, game_map.tilewidth, game_map.tileheight)
                    walls_group.add(wall)
        except TypeError:
            pass

    shift = 0
    while True:
        if not pause:
            for layer in game_map.visible_layers:
                try:
                    for x, y, gid in layer:
                        tile = game_map.get_tile_image_by_gid(gid)
                        if tile is not None:
                            screen.blit(tile, (x * game_map.tilewidth - shift, y * game_map.tileheight))
                except TypeError:
                    pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = True
                    if event.key == pygame.K_SPACE:
                        player.start_torpedo()

            player.update_pos(pygame.key.get_pressed(), walls_group)

            if player.move_map and not player.collision:
                shift += (pygame.key.get_pressed()[pygame.K_RIGHT] - pygame.key.get_pressed()[
                    pygame.K_LEFT]) * player.speed
                walls_group.update(
                    (pygame.key.get_pressed()[pygame.K_RIGHT] - pygame.key.get_pressed()[pygame.K_LEFT]) * player.speed)

            player.update_spr()
            player.update_torpedo(player, walls_group)

            player.bubbles_timer -= 1
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

            enemies.draw(screen)
            enemies.update(bullets_group, player.get_pos())

            bullets_group.draw(screen)
            bullets_group.update()

            player_group.draw(screen)
            pygame.display.flip()
            clock.tick(60)

        else:

            if pause_screen(screen, clock):
                pause = False
            else:
                for sprite in walls_group:
                    sprite.rect = sprite.rect.move(shift, 0)
                player.rect.x, player.rect.y, shift = 100, 100, 0
                pause = False
                player.bubbles = list()
                player.torpedo_group = pygame.sprite.Group()

