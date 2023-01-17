import pygame

from script.config import SIZE


class Ammo(pygame.sprite.Sprite):
    def __init__(self, speedx, speedy, x=0, y=0):
        super(Ammo, self).__init__()
        self.cache = (x, y)
        self.image = pygame.transform.scale(pygame.image.load(f'src/enemies/ammo.png'), (30, 30))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = self.cache[0]
        self.rect.y = self.cache[1]
        self.timer = 400
        self.speedx = speedx
        self.speedy = speedy

    def update(self, dx):
        self.rect = self.rect.move(-dx, 0)

    def update_pos(self, player, group, *groups):
        if pygame.sprite.collide_mask(self, player):
            player.lives -= 1
            self.kill()
            if player.lives == 0:
                player.die()
            return True
        for group in groups:
            for sprite in group:
                if 0 <= sprite.rect.x <= SIZE[0]:
                    if pygame.sprite.collide_mask(self, sprite):
                        self.kill()
                        return True

        self.timer -= 1
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.timer <= 0:
            self.kill()


class Cuttlefish(pygame.sprite.Sprite):
    def __init__(self, group, cell):
        super(Cuttlefish, self).__init__(group)
        image = pygame.image.load(f'src/enemies/cuttlefish.png')
        image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(image, (100, 100))
        self.rect = self.image.get_rect()
        self.delay = 50
        self.rect.x = cell.x
        self.rect.y = cell.y
        self.lives = 1

    def update(self, dx):
        self.rect = self.rect.move(-dx, 0)

    def update_pos(self, group, player_position):
        self.delay -= 1
        if self.delay <= 0:
            self.launch_bullet(group, player_position)
            self.delay = 50
        # self.rect.x -= 1

    def launch_bullet(self, group, player_position):
        x1 = player_position[0]
        y1 = player_position[1]
        x2 = self.rect[0] + self.rect.width // 2
        y2 = self.rect[1] + self.rect.height // 2
        if x2 >= x1:
            z = x2 - 10
            z1 = x2 - 20
            differencex = -10
        else:
            z = x2 + 10
            z1 = x2 + 20
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


class Yari(pygame.sprite.Sprite):
    def __init__(self, group, cell):
        super(Yari, self).__init__(group)
        self.image_player = \
            pygame.transform.scale(pygame.image.load(f'src/enemies/Yari.png').convert_alpha(), (300, 200))
        self.image1 = pygame.transform.flip(self.image_player, True, False)
        self.image = self.image_player
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.delay = 40
        self.rect.x = cell.x
        self.rect.y = cell.y
        self.right = True
        self.lives = 3
        if self.right:
            self.image = pygame.transform.flip(self.image_player, True, False)
        else:
            self.image = self.image_player

    def update(self, dx):
        self.rect = self.rect.move(-dx, 0)

    def update_pos(self, group, player_position):
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

        self.deley = 50


class Boss(pygame.sprite.Sprite):
    def __init__(self, screen, pos_x, pos_y):
        super(Boss, self).__init__()
        self.image = \
            pygame.transform.flip(
                pygame.transform.scale(pygame.image.load(f'src/enemies/boss.png').convert_alpha(), (800, 500)), True,
                False)
        self.rect = self.image.get_rect()
        self.image.set_colorkey((14, 209, 69))
        self.lives = 3
        self.delay1 = 100
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.delay2 = 200
        self.delay3 = 100
        self.dalay4 = 4
        self.delay5 = 300
        self.screen = screen

    def update(self, group, player_position, hero_torpedo_group):
        for torpedo in hero_torpedo_group:
            if pygame.sprite.collide_mask(self, torpedo):
                torpedo.kill()
                self.get_damage()
        if self.lives > 20:
            self.first_stage(group, player_position)
        elif 20 > self.lives > 10:
            self.second_stage(group, player_position)
        elif self.lives == 0:
            self.die()
        else:
            self.third_stage(group, player_position)

        pygame.draw.rect(self.screen, (255, 0, 0), (1300, 20, self.lives * 15, 25))

    def first_stage(self, group, player_position, flag=False, delay=1):
        self.delay1 -= delay
        if self.delay1 <= 0:
            group.add(Torpedo(False, self.rect[0] + self.rect.width // 2 - 220,
                              self.rect[1] + self.rect.height // 2 + 85, group, flag))
            group.add(Torpedo(False, self.rect[0] + self.rect.width // 2 - 245,
                              self.rect[1] + self.rect.height // 2 + 45, group, False))
            self.delay1 = 100
        y1 = self.rect[1] + self.rect.height // 2
        y2 = player_position[1] - 65
        if y2 > y1:
            if 300 < y1 < SIZE[1] - 300:
                self.rect.y += 1
        else:
            if 300 < y1 < SIZE[1] - 300:
                self.rect.y -= 1

    def second_stage(self, group, player_position):
        self.first_stage(group, player_position, flag=True, delay=0.8)
        y1 = self.rect[1] + self.rect.height // 2
        y2 = player_position[1] - 65
        if y2 > y1:
            self.rect.y += 1
        else:
            self.rect.y -= 1
        self.delay2 -= 1
        if self.delay2 <= 0:
            self.delay3 -= 1
            if self.delay3 >= 0:
                self.dalay4 -= 1
                if self.dalay4 <= 0:
                    x1 = player_position[0]
                    y1 = player_position[1]
                    x2 = self.rect[0] + self.rect.width // 2
                    y2 = self.rect[1] + self.rect.height // 2
                    if x2 >= x1:
                        z = x2 - 10
                        z1 = x2 - 20
                        differencex = -10
                    else:
                        z = x2 + 10
                        z1 = x2 + 20
                        differencex = 10
                    firtsy = (((z) - x1) / (x2 - x1)) * (y2 - y1) + y1
                    secondy = (((z1) - x1) / (x2 - x1)) * (y2 - y1) + y1
                    differencey = firtsy - secondy
                    bullet = Smart_Ammo(differencex + 4, -differencey - 5, self.rect[0] + 100,
                                        self.rect[1] + 165, f=0.1)
                    group.add(bullet)
                    self.dalay4 = 4

            else:
                self.delay2 = 200
                self.delay3 = 100

    def third_stage(self, group, player_position):
        self.second_stage(group, player_position)
        self.delay5 -= 1
        if self.delay5 <= 0:
            bullet = Laser(self.rect[0] + self.rect.width // 2 - 350, self.rect[1] + self.rect.height // 2 - 100, group,
                           player_position, self.screen)
            group.add(bullet)
            self.delay5 = 300

    def get_damage(self):
        self.lives -= 1

    def die(self):
        self.kill()


class Torpedo(pygame.sprite.Sprite):
    def __init__(self, right, x, y, group, flag):
        super(Torpedo, self).__init__()
        self.dir = f'src/player/torpedo/'
        self.right = right
        self.cut_sheet(pygame.image.load(self.dir + 'animation.png'), 8, 2)
        if self.right:
            self.image = pygame.transform.flip(
                pygame.transform.scale(pygame.image.load(f'{self.dir}torpedo.png').convert_alpha(),
                                       (76, 38)), True, False)
        else:
            self.image = pygame.transform.scale(pygame.image.load(f'{self.dir}torpedo.png'), (76, 38))
        self.rect = self.image.get_rect()
        self.masc = pygame.mask.from_surface(self.image)
        self.rect.center = (x, y)
        self.speed = 10
        self.live = 100
        self.group = group
        self.flag = flag

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
            if self.flag:
                x = self.rect[0] + self.rect.width // 2
                y = self.rect[1] + self.rect.height // 2
                self.group.add(Ammo(2, 0, x, y))
                self.group.add(Ammo(0, 2, x, y))
                self.group.add(Ammo(-2, 0, x, y))
                self.group.add(Ammo(0, -2, x, y))
                self.group.add(Ammo(-2, -2, x, y))
                self.group.add(Ammo(-2, 2, x, y))
                self.group.add(Ammo(2, -2, x, y))
                self.group.add(Ammo(2, 2, x, y))
            self.kill()

    def update(self, dx):
        self.rect = self.rect.move(-dx)

    def update_pos(self, player, group, *groups):
        if pygame.sprite.collide_mask(self, player):
            player.lives -= 1
            self.kill()
            if player.lives == 0:
                player.die()
            return True
        self.live -= 1
        if self.right:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if self.live <= 0:
            self.die()


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, group, anem_pos, screen):
        super(Laser, self).__init__()

        self.image = pygame.transform.scale(pygame.image.load(f'src/enemies/laser.png').convert_alpha(), (80, 80))
        self.rect = self.image.get_rect()
        self.masc = pygame.mask.from_surface(self.image)
        self.speedx = -10
        self.speedy = -15
        self.f = 0.5
        self.delay = 20
        self.rect.x = x
        self.rect.y = y
        self.x1 = anem_pos[0]
        self.y1 = anem_pos[1]
        self.live = 60
        self.screen = screen

    def die(self, player):
        self.delay -= 1
        x = self.rect[0] + self.rect.width // 2 + self.delay
        y = 0
        x1 = self.delay * 2
        y1 = 2400

        y3 = self.rect[1] + self.rect.height // 2 - self.delay
        x3 = 0
        x4 = 2400
        y4 = self.delay * 2
        pygame.draw.rect(self.screen, (255, 0, 0), (x, y, x1, y1))
        pygame.draw.rect(self.screen, (255, 0, 0), (x3, y3, x4, y4))
        if player.rect.colliderect(pygame.rect.Rect(x, y, x1, y1)) \
            or player.rect.colliderect(pygame.rect.Rect(x3, y3, x4, y4)):
                player.lives -= 1
        if self.delay < 0:
            self.kill()

    def update_pos(self, player, group, *groups):
        self.live -= 1
        if self.live > 0:
            self.speedy += self.f
            self.rect.x += self.speedx
            self.rect.y += self.speedy
        elif self.live < 0:
            self.die(player)


class Smart_Ammo(pygame.sprite.Sprite):
    def __init__(self, speedx, speedy, x=0, y=0, f=0):
        super(Smart_Ammo, self).__init__()
        self.cache = (x, y)
        self.image = pygame.transform.scale(pygame.image.load(f'src/enemies/ammo.png'), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = self.cache[0]
        self.rect.y = self.cache[1]
        self.timer = 400
        self.speedx = speedx
        self.speedy = speedy
        self.f = f

    def update_pos(self, player, *groups):
        self.timer -= 1
        self.speedy += self.f
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.timer <= 0:
            self.kill()
        self.deley = 40
