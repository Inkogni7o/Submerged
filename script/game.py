import pygame
from sys import exit

import pytmx

from script.main_player import MainPlayer
from script.pause import pause_screen
from script.enemies import Cuttlefish


def main_game(screen: pygame.display, clock: pygame.time.Clock):
    player = MainPlayer(screen)
    player_group = pygame.sprite.Group()
    player_group.add(player)
    bullets_group = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    enem = Cuttlefish(enemies)
    pause = False

    gameMap = pytmx.load_pygame('src/levels/test_lvl.tmx')
    walls_group = pygame.sprite.Group()
    for layer in gameMap.visible_layers:
        try:
            if layer.name == 'walls':
                image = pygame.image.load('src/textures/sand.png')
                image = pygame.transform.scale(image, (30, 30))
                for cell in layer:
                    wall = pygame.sprite.Sprite()
                    wall.rect = pygame.Rect(cell.x, cell.y, gameMap.tilewidth, gameMap.tileheight)
                    wall.image = image
                    wall.mask = pygame.mask.from_surface(wall.image)
                    walls_group.add(wall)
        except TypeError:
            pass

    while True:
        if not pause:

            for layer in gameMap.visible_layers:
                try:
                    for x, y, gid in layer:
                        tile = gameMap.get_tile_image_by_gid(gid)
                        if tile is not None:
                            screen.blit(tile, (x * gameMap.tilewidth, y * gameMap.tileheight))
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
            player.update_spr()
            player.update_torpedo()
            player_group.draw(screen)

            enemies.draw(screen)
            enemies.update(bullets_group)
            print(bullets_group)
            bullets_group.draw(screen)

            bullets_group.update()

            pygame.display.flip()
            clock.tick(60)
        else:
            if pause_screen(screen, clock):
                pause = False
            else:
                # начать уровень заново
                pass
