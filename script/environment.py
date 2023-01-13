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
