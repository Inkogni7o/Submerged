import pygame
from sys import exit

import pytmx

from main_player import MainPlayer
from pause import pause_screen


def main_game(screen: pygame.display, clock: pygame.time.Clock):
    player = MainPlayer(screen)
    player_group = pygame.sprite.Group()
    player_group.add(player)
    pause = False
    while True:

        if not pause:

            gameMap = pytmx.load_pygame('src/levels/test_lvl.tmx')
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
                player.start_torpedo(event)
            player.update_pos(pygame.key)
            player.update_spr()
            player.update_torpedo()
            
            player_group.draw(screen)
            pygame.display.flip()
            clock.tick(60)
            screen.fill((0, 0, 0))
        else:
            if pause_screen(screen, clock):
                pause = False
            else:
                # начать уровень заново
                pass
