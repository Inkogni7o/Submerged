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


class DeathWall(pygame.sprite.Sprite):
    def __init__(self, cell, up: bool):
        super(DeathWall, self).__init__()
        self.image = pygame.image.load('src/textures/stalactit.png') \
            if not up else pygame.image.load('src/textures/stalagmite.png')
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = cell.x, cell.y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dx) -> None:
        self.rect = self.rect.move(-dx, 0)


class Bubble:
    color = [255, 255, 255]
    speed = 0.5

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
        self.position[1] -= self.speed if self.death is None else self.speed + 1
        if self.death is not None:
            self.death -= 1
        if self.position[1] < 0:
            if self.death is None:
                self.generate_start_position(False)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color('white'), self.position, 3, 1)


class Breathing_bubble(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Breathing_bubble, self).__init__()
        self.image = \
            pygame.transform.scale(pygame.image.load(f'src/textures/Breathing_bubble.png').convert_alpha(), (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x - 20
        self.rect.y = y - 100
        self.timer = 200
        self.flag = True
        self.move = True
        self.global_timer = 800
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dx):
        self.rect = self.rect.move(-dx, 0)

    def update_pos(self):
        self.global_timer -= 1
        if self.global_timer == 0:
            self.kill()
        if self.move:
            self.rect.y -= 0.4
            self.timer -= 1
            if self.flag:
                self.rect.x -= 1
            else:
                self.rect.x += 1
            if self.timer <= 0:
                self.flag = not self.flag
                self.timer = 200


class Blower(pygame.sprite.Sprite):
    def __init__(self, group, bubble_group, cell):
        super(Blower, self).__init__(group)
        self.image = \
            pygame.transform.scale(pygame.image.load(f'src/textures/Blower.png').convert_alpha(), (100, 120))
        self.image.set_colorkey((14, 209, 69))
        self.rect = self.image.get_rect()
        self.VAR = 100
        self.timer = self.VAR
        self.group = bubble_group
        self.rect.x = cell.x
        self.rect.y = cell.y

    def update(self, dx):
        self.rect = self.rect.move(-dx, 0)

    def update_timer(self):
        self.timer -= 0.5
        if self.timer <= 0:
            bubble = Breathing_bubble(self.rect[0] + self.rect.width // 2,
                                      self.rect[1] + self.rect.height // 2)
            self.group.add(bubble)
            self.timer = self.VAR
