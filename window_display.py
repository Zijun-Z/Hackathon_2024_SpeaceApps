import pygame
import random
from newspaper_text import *
from classes import *

player = Player()
game = Game()

pygame.init()

game_state = Game_state.MENU

white = (255, 255, 255)
black = (0, 0, 0)

# Get the screen size
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

display_surface = pygame.display.set_mode((screen_width * 0.95, screen_height * 0.90))

# set the pygame window name
pygame.display.set_caption('SyntaxError:')

font = pygame.font.SysFont('arial', 32)

# create a text surface object,
# on which text is drawn on it.
nb = random.randint(0, 1)

text = font.render(government_havent_awarded[nb], True, black)

text1 = font.render('Start game', True, black)

textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (screen_width // 2, screen_height // 4)

while True:
    display_surface.fill(white)

    if game_state == Game_state.MENU:
        display_surface.blit(text1, textRect)

        if pygame.mouse.get_pressed()[0]:
            if textRect.collidepoint(pygame.mouse.get_pos()):
                game_state = Game_state.PLAYING

    if game_state == Game_state.PLAYING:
        display_surface.blit(text, textRect)

        if pygame.mouse.get_pressed()[0]:
            if textRect.collidepoint(pygame.mouse.get_pos()):
                paragraph = 'Hello\nWorld\nThis is Pygame'
                lines = paragraph.split('\n')

                for i, line in enumerate(lines):
                    text2 = font.render(line, True, black)
                    display_surface.blit(text2, (50, 50 + 40 * i))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
