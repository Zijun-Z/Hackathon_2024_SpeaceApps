import pygame
import random
from newspaper_text import *

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 128)

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

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (screen_width //2, screen_height // 4)

is_clicked = False


# infinite loop
while True:
	# completely fill the surface object
	# with white color
	display_surface.fill(white)
	# copying the text surface object
	# to the display surface object
	# at the center coordinate.

	display_surface.blit(text, textRect)




	# iterate over the list of Event objects
	# that was returned by pygame.event.get() method.
	for event in pygame.event.get():
		# if event object type is QUIT
		# then quitting the pygame
		# and program both.
		if event.type == pygame.QUIT:
			# deactivates the pygame library
			pygame.quit()
			quit()
		# Draws the surface object to the screen.
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:  # Left mouse button
				if textRect.collidepoint(event.pos):
					is_clicked = True
					paragraph = 'Hello\nWorld\nThis is Pygame'
					lines = paragraph.split('\n')
					for i, line in enumerate(lines):
						text2 = font.render(line, True, black)
						display_surface.blit(text2, (50, 50 + 40 * i))




		pygame.display.update()
