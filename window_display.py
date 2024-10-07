import pygame
import random
from newspaper_text import *
from classes import *
import os

title_card = True
b = 0
death_screen = False

pygame.init()  # Initialize Pygame

white = (255, 255, 255)
black = (0, 0, 0)

# Get the screen size
screen_info = pygame.display.Info()
screen_width = int(screen_info.current_w * 0.95)
screen_height = int(screen_info.current_h * 0.90)

display_surface = pygame.display.set_mode((screen_width, screen_height))

# Set the pygame window name
pygame.display.set_caption('SyntaxError:')

# Load images after initializing Pygame
backgrounds = [pygame.image.load("images/1.png").convert_alpha(),
               pygame.image.load("images/2.png").convert_alpha(),
               pygame.image.load("images/3.png").convert_alpha(),
               pygame.image.load("images/4.png").convert_alpha(),
               pygame.image.load("images/5.png").convert_alpha(),
               pygame.image.load("images/6.png").convert_alpha(),
               pygame.image.load("images/7.png").convert_alpha(),
               pygame.image.load("images/8.png").convert_alpha(),
               pygame.image.load("images/9.png").convert_alpha(),
               pygame.image.load("images/10.png").convert_alpha(),
               pygame.image.load("images/11.png").convert_alpha(),
               pygame.image.load("images/12.png").convert_alpha(),
               pygame.image.load("images/13.png").convert_alpha(),
               pygame.image.load("images/14.png").convert_alpha(),
               pygame.image.load("images/15.png").convert_alpha(),
               pygame.image.load("images/16.png").convert_alpha(),
               pygame.image.load("images/17.png").convert_alpha(),
               pygame.image.load("images/18.png").convert_alpha(),
               pygame.image.load("images/19.png").convert_alpha(),]
titleCard = pygame.image.load("images/title_card.png").convert_alpha()
deathScreen = pygame.image.load("images/game_over.png").convert_alpha()

player = Player()
game = Game()
game_stat = Game_state.MENU

newspaper_font = pygame.font.SysFont('Times New Roman', 32)
stat_font = pygame.font.SysFont('Calibri', 32)

# Create a text surface object,
# on which text is drawn on it.
nb = random.randint(0, 1)

protest_news = newspaper_font.render(government_havent_awarded[nb], True, black)

text1 = newspaper_font.render('Start game', True, black)

# Create a rectangular object for the
# text surface object
textRect = protest_news.get_rect()

# Set the center of the rectangular object.
textRect.center = (screen_width // 2, screen_height // 4)

display_text = False

while True:
    # Completely fill the surface object
    # with white color
    display_surface.fill(white)
    # Copying the text surface object
    # to the display surface object
    # at the center coordinate.

    if game_stat == Game_state.MENU:
        display_surface.blit(text1, textRect)
        if pygame.mouse.get_pressed()[0]:
            if textRect.collidepoint(pygame.mouse.get_pos()):
                game_stat = Game_state.DECISION

        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            title_card = False
        if title_card == True:
            display_surface.blit(titleCard, (0, 0))
        elif death_screen == True:
            display_surface.blit(deathScreen, (0, 0))
        else:
            display_surface.blit(backgrounds[b], (0, 0))

        # polution level up:
        if b < 18:
            b += 1

    if game_stat == Game_state.DECISION:
        display_surface.blit(protest_news, textRect)

        if pygame.mouse.get_pressed()[0] and textRect.collidepoint(pygame.mouse.get_pos()):
            display_text = not display_text

        if display_text:
            paragraph = 'Hello\nWorld\nThis is Pygame'
            lines = paragraph.split('\n')
            for i, line in enumerate(lines):
                text2 = newspaper_font.render(line, True, black)
                display_surface.blit(text2, (50, 50 + 40 * i))
        print(display_text)

    # Iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
        # If event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # Deactivates the pygame library
            pygame.quit()
            quit()
        # Draws the surface object to the screen.

    pygame.display.update()
