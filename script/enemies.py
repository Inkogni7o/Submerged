import os
import pygame
from pygame.locals import *


class Ammo(pygame.sprite.Sprite):
    def __init__(self, speedx, speedy, x=0, y=0):
        super(Ammo, self).__init__()
        self.cache = (x, y)
        self.image = pygame.transform.scale(pygame.image.load(f'src/enemies/ammo.png'), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = self.cache[0]
        self.rect.y = self.cache[1]
        self.timer = 10
        self.speedx = speedx
        self.speedy = speedy

    def update(self, *args, **kwargs):
        # self.timer -= 1
        # if self.timer <= 0:
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.timer = 100


class Cuttlefish(pygame.sprite.Sprite):
    def __init__(self, group):
        super(Cuttlefish, self).__init__(group)
        self.image = pygame.transform.scale(pygame.image.load(f'src/enemies/Cuttlefish.png').convert_alpha(), (200, 100))
        self.rect = self.image.get_rect()
        self.delay = 100
        self.rect.x = 800
        self.rect.y = 200

    def update(self, group, player_position):
        self.delay -= 1
        if self.delay <= 0:
            self.launch_bullet(group, player_position)
            self.delay = 100
        #self.rect.x -= 1

    def launch_bullet(self, group, player_position):
        x1 = player_position[0]
        y1 = player_position[1]
        x2 = self.rect.x
        y2 = self.rect.y
        if x2 >= x1:
            z = x2 - 10
            z1  = x2 - 20
            differencex = -10
        else:
            z = x2 + 10
            z1  = x2 + 20
            differencex = 10
        firtsy = (((z) - x1) / (x2 - x1)) * (y2 - y1) + y1
        secondy = (((z1) - x1) / (x2 - x1)) * (y2 - y1) + y1
        differencey = firtsy - secondy
        bullet = Ammo(differencex, -differencey, self.rect[0] + self.rect.width // 2,
                                        self.rect[1] + self.rect.height // 2)
        group.add(bullet)
        self.deley = 100
        
        
