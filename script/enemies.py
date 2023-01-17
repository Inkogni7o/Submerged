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
        self.timer = 400
        self.speedx = speedx
        self.speedy = speedy

    def update(self, *args, **kwargs):
        self.timer -= 1
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.timer <= 0:
            self.kill()


class Cuttlefish(pygame.sprite.Sprite):
    def __init__(self, group, cell):
        super(Cuttlefish, self).__init__(group)
        self.image = pygame.transform.scale(pygame.image.load(f'src/enemies/Cuttlefish.png').convert_alpha(), (200, 100))
        self.rect = self.image.get_rect()
        self.delay = 100
        self.rect.x = cell.x
        self.rect.y = cell.y
        self.lives = 1

    def update(self, group, player_position):
        self.delay -= 1
        if self.delay <= 0:
            self.launch_bullet(group, player_position)
            self.delay = 100
        #self.rect.x -= 1

    def launch_bullet(self, group, player_position):
        x1 = player_position[0]
        y1 = player_position[1]
        x2 = self.rect[0] + self.rect.width // 2
        y2 = self.rect[1] + self.rect.height // 2
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
        self.delay = 100

    def get_damage(self):
        if self.lives > 0:
            self.lives -= 1
        else:
            self.die()
        
        
class Yari(pygame.sprite.Sprite):
    def __init__(self, group, cell):
        super(Yari, self).__init__(group)
        self.image_player = \
            pygame.transform.scale(pygame.image.load(f'src/enemies/Yari.png').convert_alpha(), (300, 200))
        self.image1 = pygame.transform.flip(self.image_player, True, False)
        self.image = self.image_player
        self.rect = self.image.get_rect()
        self.delay = 100
        self.rect.x = cell.x
        self.rect.y = cell.y
        self.right = True  
        self.lives = 3          
        if self.right:
            self.image = pygame.transform.flip(self.image_player, True, False)
        else:
            self.image = self.image_player

    def update(self, group, player_position):
        self.delay -= 1
        x1 = player_position[0]
        x2 = self.rect[0] + self.rect.width // 2
        y1 = player_position[1]
        y2 = self.rect[1] + self.rect.height // 2
        if x2 >= x1:
            self.image = self.image1
        else:
            self.image = self.image_player
        if x1 > x2:
            self.rect.x += 1
        elif x1 < x2:
            self.rect.x -= 1
        if y1 > y2:
            self.rect.y += 1
        elif y1 < y2:
            self.rect.y -= 1
        if self.delay <= 0:
            self.launch_bullet(group, player_position)
            self.delay = 100

    def get_damage(self):
        if self.lives > 0:
            self.lives -= 1
        else:
            self.die()

    def launch_bullet(self, group, player_position):
        x1 = player_position[0]
        x2 = self.rect.x
        if x2 >= x1:
            x = -5
        else:
            x = 5
        bullet = Ammo(x, 5, self.rect[0] + self.rect.width // 2,
                                        self.rect[1] + self.rect.height // 2)
        bullet2 = Ammo(x, 0, self.rect[0] + self.rect.width // 2,
                                        self.rect[1] + self.rect.height // 2)
        bullet3 = Ammo(x, -5, self.rect[0] + self.rect.width // 2,
                                        self.rect[1] + self.rect.height // 2)
        group.add(bullet)
        group.add(bullet3)
        group.add(bullet2)

        self.deley = 100


class Boss():
    def __init__(self, group, cell):
        super(Boss, self).__init__(group)
        self.image_player = \
            pygame.transform.scale(pygame.image.load(f'src/enemies/boss.png').convert_alpha(), (300, 200))
        self.rect = self.image.get_rect()
        self.lives = 30


    def update(self):
    

    def get_damage(self):
        self.lives -= 1