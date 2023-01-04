import pygame


class Button:
    def __init__(self, screen: pygame.display, text: str, color: str, x: int, y: int, width: int, height: int):
        """
        Класс кнопки на экране
        :param screen: экран, на котором отрисовывается кнопка
        :param text: текст внутри кнопки
        :param color: цвет, задающийся словом (напр. yellow)
        :param x: X координата вернего левого края кнопки
        :param y: Y координата вернего левого края кнопки
        :param width: ширина кнопки в пикселях
        :param height: высота кнопки в пикселях
        """
        self.screen = screen
        self.text_btn = text
        self.color = pygame.Color(color)
        self.x, self.y = x, y
        self.width, self.height = width, height

    def draw(self, screen, outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text_btn != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text_btn, True, (0, 0, 0))
            screen.blit(text,
                        (self.x + (self.width / 2 - text.get_width() / 2),
                         self.y + (self.height / 2 - text.get_height() / 2)))

    def update(self, pos_x: int, pos_y: int):
        if self.x <= pos_x <= self.x + self.width and self.y <= pos_y <= self.y + self.height:
            # TODO: изменить вид кнопки при наведении на неё курсора
            pass
