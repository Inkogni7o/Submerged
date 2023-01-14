import pygame
from sys import exit

import pytmx

from script.main_player import MainPlayer
from script.pause import pause_screen
from script.environment import Wall
from script.enemies import Cuttlefish, Yari


def main_game(screen: pygame.display, clock: pygame.time.Clock):
    player = MainPlayer(screen)
    player_group = pygame.sprite.Group()
    player_group.add(player)
    bullets_group = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    #enem = Yari(enemies)
    enem = Cuttlefish(enemies)
    pause = False

    gameMap = pytmx.load_pygame('src/levels/test_lvl.tmx')
    walls_group = pygame.sprite.Group()
    for layer in gameMap.visible_layers:
        try:
            if layer.name == 'walls':
                for cell in layer:
                    wall = Wall(cell, gameMap.tilewidth, gameMap.tileheight)
                    walls_group.add(wall)
        except TypeError:
            pass

    shift = 0
    while True:
        if not pause:
            for layer in gameMap.visible_layers:
                try:
                    for x, y, gid in layer:
                        tile = gameMap.get_tile_image_by_gid(gid)
                        if tile is not None:
                            screen.blit(tile, (x * gameMap.tilewidth - shift, y * gameMap.tileheight))
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
                shift += (pygame.key.get_pressed()[pygame.K_RIGHT] - pygame.key.get_pressed()[pygame.K_LEFT]) * player.speed
                walls_group.update(
                    (pygame.key.get_pressed()[pygame.K_RIGHT] - pygame.key.get_pressed()[pygame.K_LEFT]) * player.speed)

            player.update_spr()
            player.update_torpedo(walls_group)

            enemies.draw(screen)
            enemies.update(bullets_group, player.get_pos())
            bullets_group.draw(screen)

            bullets_group.update()

            player_group.draw(screen)
            pygame.display.flip()
            clock.tick(60)
            screen.fill((0, 0, 0))

        else:
            if pause_screen(screen, clock):
                pause = False
            else:
                for sprite in walls_group:
                    sprite.rect = sprite.rect.move(shift, 0)
                player.rect.x, player.rect.y, shift = 0, 0, 0
                pause = False
