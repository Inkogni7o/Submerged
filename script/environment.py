import random

import pygame.sprite


class Wall(pygame.sprite.Sprite):
    image = pygame.image.load('src/textures/sand.png')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, cell, tile_width, tile_height):
        super(Wall, self).__init__()
        self.rect = pygame.Rect(cell.x, cell.y, tile_width, tile_height)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dx) -> None:
        self.rect = self.rect.move(-dx, 0)


class Bubble:
    color = [255, 255, 255]
    speed = 1

    def __init__(self, size: list, position=None, death=None):
        self.monitor_size = size
        self.death = 100 if death else None
        if position is None:
            self.generate_start_position(True)
        else:
            self.position = position

    def generate_start_position(self, yrandom=False):
        if yrandom:
            self.position = [random.randint(2, self.monitor_size[0] - 2), random.randint(1, self.monitor_size[1])]
        else:
            self.position = [self.position[0], self.monitor_size[1]]

    def update(self):
        if self.death is not None:
            self.death -= 1
        self.position[1] -= self.speed
        if self.position[1] < 0:
            self.generate_start_position(False)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color('white'), self.position, 3, 1)
