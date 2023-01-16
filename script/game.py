import random

import pygame
from sys import exit

import pytmx

from script.config import SIZE
from script.enemies import Cuttlefish, Yari
from script.main_player import MainPlayer
from script.pause import pause_screen
from script.environment import Wall, Bubble, Blower, DeathWall
from script.scenes import scene
from script.text import Text


def main_game(level, screen: pygame.display, clock: pygame.time.Clock, player_pos: tuple):
    text = Text('Хьюстон, я спускаюсь', False)
    player = MainPlayer(screen, *player_pos)
    player_group = pygame.sprite.Group()
    player_group.add(player)
    blower_group = pygame.sprite.Group()
    breathing_bubble_group = pygame.sprite.Group()
    blower_group.add()
    bullets_group = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    pause = False
    death_image = pygame.transform.scale(pygame.image.load('src/backgrounds/death_bg.png'), (SIZE[0] - 500, SIZE[1]))
    death_image.set_colorkey((247, 247, 247))

    game_map = pytmx.load_pygame(f'src/levels/level{level}.tmx')

    walls_group = pygame.sprite.Group()
    death_wall_group = pygame.sprite.Group()
    enemies_group = pygame.sprite.Group()

    for layer in game_map.visible_layers:
        try:
            if layer.name == 'walls':
                for cell in layer:
                    wall = Wall(cell, game_map.tilewidth, game_map.tileheight)
                    walls_group.add(wall)
            if layer.name == 'death_walls_up':
                for cell in layer:
                    wall = DeathWall(cell, False)
                    death_wall_group.add(wall)
            if layer.name == 'death_walls_down':
                for cell in layer:
                    wall = DeathWall(cell, True)
                    death_wall_group.add(wall)
            if layer.name == 'blower':
                for cell in layer:
                    Blower(blower_group, breathing_bubble_group, cell)
            if layer.name == 'cuttlefish':
                for cell in layer:
                    Cuttlefish(enemies_group, cell)
            if layer.name == 'yari':
                for cell in layer:
                    Yari(enemies_group, cell)

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

            death_wall_group.draw(screen)

            if level == 1:
                if shift > 7900:
                    result = scene(2, screen, player, player_group)
                    text.draw(screen)
                    pygame.display.flip()
                    if result:
                        # завершение уровня
                        return True
                    continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = True
                    if event.key == pygame.K_SPACE:
                        player.start_torpedo()

            player.update_pos(pygame.key.get_pressed(), walls_group, blower_group)

            if player.move_map and not player.collision:
                move = (pygame.key.get_pressed()[pygame.K_RIGHT]
                                               - pygame.key.get_pressed()[pygame.K_LEFT]) * player.speed
                shift += (pygame.key.get_pressed()[pygame.K_RIGHT] - pygame.key.get_pressed()[
                    pygame.K_LEFT]) * player.speed
                walls_group.update(move)
                death_wall_group.update(move)
                blower_group.update(move)
                breathing_bubble_group.update(move)
                enemies_group.update(move)
                bullets_group.update(move)

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

            for sprite in bullets_group:
                sprite.update_pos(player, walls_group, blower_group)
            bullets_group.draw(screen)

            for sprite in enemies_group:
                if 0 <= sprite.rect.x <= SIZE[0]:
                    sprite.update_pos(bullets_group, player.get_pos())
            enemies_group.draw(screen)

            for sprite in blower_group:
                sprite.update_timer()
            blower_group.draw(screen)

            for sprite in breathing_bubble_group:
                sprite.update_pos()
                if pygame.sprite.collide_mask(sprite, player):
                    sprite.kill()
                    # player.air += 10
            breathing_bubble_group.draw(screen)

            player_group.draw(screen)

            if player.lives <= 0:
                screen.blit(death_image, (300, 0))
                # TODO: сделать либо взрыв, либо выпуск большого количества пузырей в знак проигрыша

            # жизни героя
            for i in range(player.lives):
                image = pygame.transform.scale(pygame.image.load('src/textures/life.png'),
                                               (70, 70))
                image.set_colorkey((14, 209, 69))
                screen.blit(image, (0 + 80 * i, 0))

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

