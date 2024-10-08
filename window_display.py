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
               pygame.image.load("images/19.png").convert_alpha(), ]


titleCard = pygame.image.load("images/title_card.png").convert_alpha()
deathScreen = pygame.image.load("images/game_over.png").convert_alpha()
winScreen = pygame.image.load("images/victory_screen.png").convert_alpha()

player_healthy = pygame.image.load("images/worker_healthy.png").convert_alpha()
healthy_good = pygame.transform.scale(player_healthy, (400, 520))

player_sick_light = pygame.image.load("images/worker_sick_light.png").convert_alpha()
sick_light_good = pygame.transform.scale(player_sick_light, (400, 520))

player_sick_medium = pygame.image.load("images/worker_sick_medium.png").convert_alpha()
sick_medium_good = pygame.transform.scale(player_sick_medium, (400, 520))

player_sick_fatal = pygame.image.load("images/worker_sick_fatal.png").convert_alpha()
sick_fatal_good = pygame.transform.scale(player_sick_fatal, (400, 520))

player_displayed = healthy_good




player = Player()
game = Game()
game_stat = Game_state.MENU

newspaper_font = pygame.font.SysFont('Times New Roman', 26)
stat_font = pygame.font.SysFont('Calibri', 32)

# Create a text surface object,
# on which text is drawn on it.
nb = random.randint(0, 1)

protest_news = newspaper_font.render(government_havent_awarded[nb], True, black)

# text surface object
textRect = protest_news.get_rect()

# Set the center of the rectangular object.
textRect.center = (screen_width // 2, screen_height // 4)

display_text = False

polution_up = False
"""
while True:
    # Completely fill the surface object
    # with white color
    display_surface.fill(white)
    # Copying the text surface object
    # to the display surface object
    # at the center coordinate.

    if game_stat == Game_state.MENU:

        if title_card:
            display_surface.blit(titleCard, (0, 0))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            title_card = False
            game_stat = game_stat.DECISION

    if game_stat == Game_state.DECISION:


        if death_screen:
            display_surface.blit(deathScreen, (0, 0))
        else:
            display_surface.blit(backgrounds[b], (0, 0))

        display_surface.blit(player_displayed, (screen_width*0.75, 200))

        display_surface.blit(protest_news, textRect)

        # polution level up:


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
"""