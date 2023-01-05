import pygame
from main_player import MainPlayer


if __name__ == '__main__':
    pygame.init()
    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)
    running = True
    count = 1
    font = pygame.font.Font(None, 100)
    text = font.render('1', True, pygame.Color("red"))
    x = width // 2 - text.get_width() // 2
    y = height // 2 - text.get_height() // 2
    screen.fill(pygame.Color('black'))
    screen.blit(text, (x, y))
    player = MainPlayer(50, 50)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == 32780:
                pass
            if event.type == 32782:
                count += 1
                font = pygame.font.Font(None, 100)
                text = font.render(str(count), True, pygame.Color("red"))
                x = width // 2 - text.get_width() // 2
                y = height // 2 - text.get_height() // 2
                screen.fill(pygame.Color('black'))
                screen.blit(text, (x, y))
        screen.blit(player, (50, 50))
        pygame.display.flip()
    pygame.quit()
