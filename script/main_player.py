import random

import pygame.sprite
import os
import pygame

from script.config import SIZE
from script.environment import Bubble


class MainPlayer(pygame.sprite.Sprite):
    def __init__(self, screen, x=0, y=0):
        super(MainPlayer, self).__init__()
        self.BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        self.sprite_dir = f'src/player/'
        self.right = True
        self.move = False
        self.move_map = False
        self.deley = 0
        self.screen = screen
        self.image_player = \
            pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}player1.png').convert_alpha(), (300, 200))
        self.image = self.image_player
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 8
        self.cur_sprite = 0
        self.torpedo_group = pygame.sprite.Group()

    def update_pos(self, keys, *groups):
        self.collision = False
        self.deley -= 1
        if (not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]
                and not keys[pygame.K_DOWN] and not keys[pygame.K_UP]):
            self.move = False
        else:
            old_main_player_rect = self.rect.copy()
            new_main_player_rect = self.rect.copy()
            new_main_player_rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.speed * 2
            new_main_player_rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * (self.speed - 2)
            self.rect = new_main_player_rect
            if 50 <= self.rect.x + min([i[0] for i in self.mask.outline()]) * 1.5 <= SIZE[0] // 2:
                self.move_map = False
            else:
                self.move_map = True
            if self.rect.y <= 0:
                self.collision = True
            if self.collision:
                self.rect = old_main_player_rect
                return

            for group in groups:
                for sprite in group:
                    if 0 <= sprite.rect.x <= SIZE[0] // 2:
                        if pygame.sprite.collide_mask(self, sprite):
                            self.rect = old_main_player_rect
                            self.collision = True
                            break
                if self.collision:
                    break
            else:
                if not self.move_map:
                    self.rect = new_main_player_rect
                    self.rect.x -= (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.speed
                    self.move = True
                    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                        self.right = True if not keys[pygame.K_LEFT] else False
                else:
                    self.rect = old_main_player_rect

    def start_torpedo(self):
        if self.deley <= 0:
            self.torpedo_group.add(Torpedo(self.sprite_dir, self.right, self.rect[0] + self.rect.width // 2,
                                           self.rect[1] + self.rect.height // 2))
            self.deley = 100

    def update_torpedo(self, player, *groups):
        self.torpedo_group.draw(self.screen)
        self.torpedo_group.update(player, groups)

    def get_pos(self):
        return self.rect.center[0], self.rect.center[1]

    def update_spr(self):
        if self.move:
            self.cur_sprite += 1
            if self.right:
                self.image = pygame.transform.flip(self.image_player, True, False)
            else:
                self.image = self.image_player
        else:
            if self.right:
                self.image = pygame.transform.flip(self.image_player, True, False)
            else:
                self.image = self.image_player


class Torpedo(pygame.sprite.Sprite):
    def __init__(self, dir, right, x, y):
        super(Torpedo, self).__init__()
        self.dir = f'src/player/torpedo/'
        self.right = right
        self.cut_sheet(pygame.image.load(self.dir + 'animation.png'), 8, 2)
        if self.right:
            self.image = pygame.transform.flip(
                pygame.transform.scale(pygame.image.load(f'{self.dir}torpedo.png').convert_alpha(),
                                       (76, 38)), True, False)
        else:
            self.image = pygame.transform.scale(pygame.image.load(f'{self.dir}torpedo.png'), (76, 38))
        self.rect = self.image.get_rect()
        self.masc = pygame.mask.from_surface(self.image)
        self.rect.center = (x, y)
        self.speed = 10
        self.live = 100

    def cut_sheet(self, sheet, columns, rows):
        self.frames = []
        self.cur_frame = 0
        self.cur_sprite = 0
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(92, 92)

    def die(self, player: MainPlayer):
        self.speed = 0
        self.cur_sprite += 1
        if player.move_map:
            self.rect.x = self.rect.x + player.speed if not player.right else self.rect.x - player.speed
        if self.cur_sprite % 3 == 0:
            self.image = self.frames[self.cur_sprite // 3]
        if self.cur_sprite >= 45:
            self.cur_sprite = 0
            self.kill()

    def update(self, player, groups):
        for group in groups:
            for sprite in group:
                if 0 < sprite.rect.x < SIZE[0] // 2:
                    if pygame.sprite.collide_mask(self, sprite):
                        self.die(player)
        self.live -= 1
        if self.right:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if self.live <= 0:
            self.die(player)


class AI_Player(MainPlayer):
    def __init__(self, screen, x, y):
        super(AI_Player, self).__init__(screen)
        self.x, self.y = x, y
        self.monitor_size = list(SIZE)
        self.bubbles = list()
        self.timer = 4

    def move_player(self, x: int, y: int):
        self.rect.x += x
        self.rect.y += y
        self.timer -= 1
        if self.rect.x > self.monitor_size[0]:
            self.rect.x = -400
            self.rect.center = self.rect.center[0], random.randint(300, self.monitor_size[1] - 300)

    def draw(self):
        for bubble in self.bubbles:
            bubble.draw(self.screen)
            bubble.update()
            if bubble.death is not None:
                if bubble.death == 0:
                    self.bubbles.pop(self.bubbles.index(bubble))
        if not self.right:
            self.screen.blit(self.image, self.get_pos())
        else:
            self.screen.blit(pygame.transform.flip(self.image, True, False), self.get_pos())
        if self.timer == 0:
            for _ in range(2):
                self.bubbles.append(Bubble(self.monitor_size,
                                           [self.rect.center[0] + random.randint(95, 100),
                                            self.rect.center[1] + random.randint(80, 120)], True))
                self.bubbles.append(Bubble(self.monitor_size,
                                           [self.rect.center[0] + random.randint(95, 100),
                                            self.rect.center[1] + random.randint(80, 120)], True))
            self.timer = 4
