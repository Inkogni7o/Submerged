import pygame.sprite
import os
import pygame
from pygame.locals import *


class MainPlayer(pygame.sprite.Sprite):
    def __init__(self, screen, x=0, y=0):
        super(MainPlayer, self).__init__()
        self.BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        self.sprite_dir = f'src/player/'
        self.right = False
        self.move = False
        self.screen = screen
        self.image = pygame.image.load(f'{self.sprite_dir}6.png')
        self.rect = self.image.get_rect()
        self.image1 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}1.png'), (300, 200))
        self.image2 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}2.png'), (300, 200))
        self.image3 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}3.png'), (300, 200))
        self.image4 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}4.png'), (300, 200))
        self.image5 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}5.png'), (300, 200))
        self.image6 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}6.png'), (300, 200))
        self.sprite_pac = [
            self.image1,
            self.image2,
            self.image3,
            self.image4,
            self.image5,
            self.image6,
        ]
        self.speed = 5
        self.cur_sprite = 0
        self.torpedo_group = pygame.sprite.Group()

    def update_pos(self, key):
        if key.get_pressed()[K_LEFT] or key.get_pressed()[K_a]:
            self.rect.x -= self.speed
            self.right = False
            self.move = True
        elif key.get_pressed()[K_RIGHT] or key.get_pressed()[K_d]:
            self.rect.x += self.speed
            self.right = True
            self.move = True
        elif key.get_pressed()[K_UP] or key.get_pressed()[K_w]:
            self.rect.y -= self.speed - 3
            self.move = True
        elif key.get_pressed()[K_DOWN] or key.get_pressed()[K_s]:
            self.rect.y += self.speed - 3
            self.move = True
        else:
            self.move = False
        pygame.event.pump()

    def start_torpedo(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print(self.rect[0], )
                self.torpedo_group.add(Torpedo(self.sprite_dir, self.right, self.rect.center[0], self.rect.center[1]))
    
    def update_torpedo(self):
        self.torpedo_group.draw(self.screen)
        self.torpedo_group.update()

    def update_spr(self):
        if self.move:
            self.cur_sprite += 1
            if self.cur_sprite % 10 == 0:
                self.image = self.sprite_pac[self.cur_sprite // 10]
                if self.right:
                    self.image = pygame.transform.flip(self.sprite_pac[self.cur_sprite // 10], 1, 0)

            if self.cur_sprite >= 50:
                self.cur_sprite = 0
        else:
            self.image = self.sprite_pac[5]
            if self.right:
                self.image = pygame.transform.flip(self.sprite_pac[5], 1, 0)


class Torpedo(pygame.sprite.Sprite):
    def __init__(self, dir, right, x, y):
        super(Torpedo, self).__init__()
        self.dir = dir + 'torpedo/'
        self.right = right
        if self.right:
            self.image = pygame.transform.flip( pygame.transform.scale(pygame.image.load(f'{self.dir}torpedo.png'), (76, 38)), 1, 0)
        else:
            self.image = pygame.transform.scale(pygame.image.load(f'{self.dir}torpedo.png'), (76, 38))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.live = 100
        
    def update(self):
        self.live -= 1
        if self.right:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if self.live <= 0:
            pass