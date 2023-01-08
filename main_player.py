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
        self.deley = 0
        self.screen = screen
        self.image1 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}1.png').convert_alpha(), (300, 200))
        self.image2 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}2.png').convert_alpha(), (300, 200))
        self.image3 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}3.png').convert_alpha(), (300, 200))
        self.image4 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}4.png').convert_alpha(), (300, 200))
        self.image5 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}5.png').convert_alpha(), (300, 200))
        self.image6 = pygame.transform.scale(pygame.image.load(f'{self.sprite_dir}6.png').convert_alpha(), (300, 200))
        self.image = self.image6
        self.rect = self.image6.get_rect()
        self.rect = self.image6.get_rect()
        self.sprite_pac = [
            self.image1, self.image2,
            self.image3, self.image4,
            self.image5, self.image6,
        ]
        self.mask = pygame.mask.from_surface(self.image6)
        self.speed = 5
        self.cur_sprite = 0
        self.torpedo_group = pygame.sprite.Group()

    def update_pos(self, keys, *groups):    
        self.deley -= 1
        if (not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]
                and not keys[pygame.K_DOWN] and not keys[pygame.K_UP]):
            self.move = False
        else:
            old_main_player_rect = self.rect.copy()
            new_main_player_rect = self.rect.copy()
            new_main_player_rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.speed
            new_main_player_rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * (self.speed - 2)
            self.rect = new_main_player_rect
            collision = False
            for group in groups:
                for sprite in group:
                    if pygame.sprite.collide_mask(self, sprite):
                        self.rect = old_main_player_rect
                        collision = True
                        break

                if collision:
                    break
            else:
                self.rect = new_main_player_rect
                self.move = True
                if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                    self.right = True if not keys[pygame.K_LEFT] else False

    def start_torpedo(self):
         if self.deley <= 0:
            self.torpedo_group.add(Torpedo(self.sprite_dir, self.right, self.rect[0] + self.rect.width // 2,
                                        self.rect[1] + self.rect.height // 2))
            self.deley = 100

    def update_torpedo(self):
        self.torpedo_group.draw(self.screen)
        self.torpedo_group.update()

    def update_spr(self):
        if self.move:
            self.cur_sprite += 1
            if self.cur_sprite % 10 == 0:
                self.image = self.sprite_pac[self.cur_sprite // 10]
                self.mask = pygame.mask.from_surface(self.image)
                if self.right:
                    self.image = pygame.transform.flip(self.sprite_pac[self.cur_sprite // 10], True, False)
                    self.mask = pygame.mask.from_surface(self.image)

            if self.cur_sprite >= 50:
                self.cur_sprite = 0
        else:
            self.image = self.sprite_pac[5]
            self.mask = pygame.mask.from_surface(self.image)
            if self.right:
                self.image = pygame.transform.flip(self.sprite_pac[5], True, False)
                self.mask = pygame.mask.from_surface(self.image)


class Torpedo(pygame.sprite.Sprite):
    def __init__(self, dir, right, x, y):
        super(Torpedo, self).__init__()
        self.dir = f'src/player/torpedo/'
        self.right = right
        self.cut_sheet(pygame.image.load(self.dir + 'animation.png'), 8, 2)
        if self.right:
            self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(f'{self.dir}torpedo.png'),
                                                                      (76, 38)), True, False)
        else:
            self.image = pygame.transform.scale(pygame.image.load(f'{self.dir}torpedo.png'), (76, 38))
        self.rect = self.image.get_rect()
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
    
    def die(self):
        self.speed = 0
        self.cur_sprite += 1
        if self.cur_sprite % 3 == 0:
            self.image = self.frames[self.cur_sprite // 3]
        if self.cur_sprite >= 45:
            self.cur_sprite = 0
            self.kill()

    def update(self):
        self.live -= 1
        if self.right:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if self.live <= 0:
            self.die()
