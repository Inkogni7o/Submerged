import os
import pygame
from pygame.locals import *

class Ammo(pygame.sprite.Sprite):
    def __init__(self):
        super(Ammo, self).__init__()
        self.image = pygame.transform.scale(pygame.image.load(f'src/enemies/ammo.png'), (30, 30))
        self.rect = self.image.get_rect()

class Ordinary(pygame.sprite.Sprite):
    def __init__(self):
        super(Ordinary, self).__init__()
