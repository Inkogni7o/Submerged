import pygame

from script.environment import Bubble
from script.game import main_game
from script.main_player import AI_Player
from script.start_menu import introductory_menu
from script.config import SIZE
from script.game_menu import game_menu
from script.lvl_selection import lvl_selection

pygame.init()

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
clock.tick(60)

BUBBLES = [Bubble(list(SIZE)) for _ in range(300)]
AI_PLAYER = AI_Player(screen, -200, 600)

now_screen = 'start'
while True:
    if now_screen == 'start':
        if introductory_menu(screen, BUBBLES, AI_PLAYER):
            now_screen = 'game_menu'
    if now_screen == 'game_menu':
        now_screen = game_menu(screen, BUBBLES, AI_PLAYER)
    if now_screen == 'select_lvl':
        now_screen = lvl_selection(screen, BUBBLES, AI_PLAYER)
    if now_screen == 'level1':
        now_screen = 'level2' if main_game(1, screen, clock, (100, 100)) else 'level1'
    if now_screen == 'level2':
        now_screen = 'level3' if main_game(2, screen, clock, (0, 0)) else 'level2'
