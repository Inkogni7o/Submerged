import sys

import pygame
import textwrap

from script.config import SIZE


class Text:
    def __init__(self, text: str):
        self.text = textwrap.wrap(text, 40) + ['Нажмите, чтобы продолжить']
        self.font = pygame.font.Font('src/font.ttf', 55)
        self.sym_index, self.string_index = 0, 0
        self.timer = 8
        self.end = False

    def draw(self, screen):
        pygame.draw.rect(screen, (181, 184, 177, 50), (0, SIZE[1] - 300, SIZE[0], 300))
        if not self.end:
            if self.timer == 0:
                self.sym_index += 1
                if self.sym_index - 1 == len(self.text[self.string_index]):
                    self.string_index += 1
                    if self.string_index > len(self.text) - 1:
                        self.end = True
                        return
                    self.sym_index = 0
                self.timer = 8
            self.timer -= 1

            for i in range(self.string_index + 1):
                if i == self.string_index:
                    text = self.font.render(self.text[i][:self.sym_index], True, (0, 0, 0))
                else:
                    text = self.font.render(self.text[i], True, (0, 0, 0))
                screen.blit(text, (50, SIZE[1] - 280 + 54 * i))
        else:
            for i in range(self.string_index):
                text = self.font.render(self.text[i], True, (0, 0, 0))
                screen.blit(text, (50, SIZE[1] - 280 + 54 * i))

    def change_text(self, new_text):
        self.text = textwrap.wrap(new_text, 40) + ['Нажмите, чтобы продолжить']
        self.timer = 8
        self.string_index, self.sym_index = 0, 0
        self.end = False
        print(self.end)
