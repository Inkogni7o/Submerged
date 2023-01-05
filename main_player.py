import pygame.sprite
import os
import pygame


class MainPlayer(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super(MainPlayer, self).__init__()
        self.BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        self.sprite_dir = f'src\player\\'
        self.pos = [x, y]
        self.x, self.y = 100, 100

        self.image = pygame.image.load(f'{self.sprite_dir}6.png')
        self.rect = self.image.get_rect()

        self.image1 = pygame.image.load(f'{self.sprite_dir}1.png')
        self.image2 = pygame.image.load(f'{self.sprite_dir}2.png')
        self.image3 = pygame.image.load(f'{self.sprite_dir}3.png')
        self.image4 = pygame.image.load(f'{self.sprite_dir}4.png')
        self.image5 = pygame.image.load(f'{self.sprite_dir}5.png')
        self.image6 = pygame.image.load(f'{self.sprite_dir}6.png')
        self.sprite_pac = [
            self.image1,
            self.image2,
            self.image3,
            self.image4,
            self.image5,
            self.image6,
        ]
        self.cur_sprite = 0

    def draw(self, screen, x=0, y=0):
        self.x += x
        self.y += y
        self.image = self.sprite_pac[self.cur_sprite]
        self.cur_sprite = (self.cur_sprite + 1) % len(self.sprite_pac)


