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
        self.timer = 100
        self.speedx = speedx
        self.speedy = speedy

    def update(self, *args, **kwargs):
        self.timer -= 1
        if self.timer <= 0:
            self.rect.x += self.speedx
            self.rect.y += self.speedy 
            self.timer = 100


class Cuttlefish(pygame.sprite.Sprite):
    def __init__(self):
        super(Cuttlefish, self).__init__()
        self.image = pygame.transform.scale(pygame.image.load(f'src/enemies/Cuttlefish.png').convert_alpha(), (200, 100))
        self.rect = self.image.get_rect()
        self.delay = 100
        self.rect.x = 800
        self.rect.y = 200

    def update(self, group):
        self.delay -= 1
        if self.delay <= 0:
            group = self.launch_bullet(group)
            self.delay = 100
        #self.rect.x -= 1

    def launch_bullet(self, group):
        bullet = Ammo(1, 0, self.rect.x // 2, self.rect.y // 2)
        group.add(bullet)
        self.deley = 100
        
        
