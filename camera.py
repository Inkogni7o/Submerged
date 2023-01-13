from config import get_monitor_size

class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        # self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        # obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        x, y = get_monitor_size()
        self.dx = -(target.rect.x + target.rect.w // 2 - x // 2)
        # self.dy = -(target.rect.y + target.rect.h // 2 - y // 2)
