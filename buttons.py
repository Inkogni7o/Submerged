import pygame


class Button:
    def __init__(self, text: str, color1: str, color2: str,
                 x: int, y: int, width: int, height: int):
        """
        Класс кнопки на экране
        :param text: текст внутри кнопки
        :param color1: цвет, задающийся словом (напр. yellow), ryj
        :param x: X координата вернего левого края кнопки
        :param y: Y координата вернего левого края кнопки
        :param width: ширина кнопки в пикселях
        :param height: высота кнопки в пикселях
        """
        self.text_btn = text
        self.color1 = pygame.Color(color1)
        self.color2 = pygame.Color(color2)
        self.x, self.y = x, y
        self.width, self.height = width, height

    def draw(self, screen: pygame.display, pos_x: int, pos_y: int, outline_color=None):
        if outline_color:
            # отрисовка границы кнопки, если таковая имеется
            pygame.draw.rect(screen, outline_color, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        if self.mouse_on_btn(pos_x, pos_y):
            pygame.draw.rect(screen, self.color2, (self.x, self.y, self.width, self.height), 0)
        else:
            pygame.draw.rect(screen, self.color1, (self.x, self.y, self.width, self.height), 0)

        font = pygame.font.SysFont('comicsans', 60)
        text = font.render(self.text_btn, True, (0, 0, 0))
        if self.mouse_on_btn(pos_x, pos_y):
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                               self.y + (self.height / 2 - text.get_height() / 2) + 5))
        else:
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                               self.y + (self.height / 2 - text.get_height() / 2)))

    def mouse_on_btn(self, pos_x: int, pos_y: int) -> bool:
        if self.x <= pos_x <= self.x + self.width and self.y <= pos_y <= self.y + self.height:
            return True
        return False
