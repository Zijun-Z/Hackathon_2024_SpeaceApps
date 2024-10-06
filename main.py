import pygame
import random
from classes import *
from newspaper_text import *
from window_display import *

game_stat = Game_state.MENU
game = Game()
pollution_level = 0
player = Player()

pollution_increase = 3

play_game = True

display_text = False

while True:
    if not player.is_alive():
        game.game_over()

    # completely fill the surface object
    # with white color
    display_surface.fill(white)
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.

    """MENU"""

    if game_stat == Game_state.MENU:
        display_surface.blit(text1, textRect)
        if pygame.mouse.get_pressed()[0]:
            if textRect.collidepoint(pygame.mouse.get_pos()):
                game_stat = Game_state.DECISION

    #PLAYING

    elif game_stat == Game_state.DECISION:

        if game.pollution > 30:
            pollution_level = Pollution.HIGH
        elif game.pollution > 20:
            pollution_level = Pollution.MEDIUM
        elif game.pollution > 10:
            pollution_level = Pollution.LOW
        else:
            pollution_level = Pollution.NONE

        if pollution_level == Pollution.HIGH:
            illness = random.choice([Illness.CANCER, Illness.PNEUMONIA, Illness.STROKE])
        elif pollution_level == Pollution.MEDIUM:
            illness = random.choice([Illness.ASTHMA, Illness.CARDIOVASCULAR_DISEASE])
        elif pollution_level == Pollution.LOW:
            illness = random.choice([Illness.IRRITATION, Illness.HEADACHES, Illness.BREATHING_PROBLEMS])
        else:
            illness = None

        if illness:
            player.illnesses.add(illness)

        player.apply_illness_affects()

        if pollution_level == Pollution.HIGH:
            choice_index = 5
        elif pollution_level == Pollution.MEDIUM:
            choice_index = 3
        elif pollution_level == Pollution.LOW:
            choice_index = 2
        else:
            choice_index = 1

        newspaper_protest = Newspaper(player.did_protest, game.government_did_aware, choice_index)
        newspaper_protest_text = newspaper_font.render(newspaper_protest.protest_news, True, black)
        newspaper_protest_rect = newspaper_protest_text.get_rect()
        newspaper_protest_rect.topleft = (0, 0)
        display_surface.blit(newspaper_protest_text, newspaper_protest_rect)

        newspaper_government_is_aware = Newspaper(player.did_protest, game.government_did_aware, choice_index)
        newspaper_government_is_aware_text = newspaper_font.render(newspaper_government_is_aware.government_action,
                                                                   True, black)
        newspaper_government_is_aware_rect = newspaper_government_is_aware_text.get_rect()
        newspaper_government_is_aware_rect.topleft = (0, 100)
        display_surface.blit(newspaper_government_is_aware_text, newspaper_government_is_aware_rect)

        newspaper_local_news = Newspaper(player.did_protest, game.government_did_aware, choice_index)
        newspaper_local_news_text = newspaper_font.render(newspaper_local_news.random_news, True, black)
        newspaper_local_news_rect = newspaper_local_news_text.get_rect()
        newspaper_local_news_rect.topleft = (0, 200)

        display_surface.blit(newspaper_local_news_text, newspaper_local_news_rect)

        game.government_did_aware = False
        player.did_protest = False

        """ PLAYER DECISION """
        work_text = stat_font.render('WORK', True, black)
        work_text_rect = work_text.get_rect()
        work_text_rect.center = (screen_width * 0.1, screen_height * 0.8)

        protest_text = stat_font.render('PROTEST', True, black)
        protest_text_rect = protest_text.get_rect()
        protest_text_rect.center = (screen_width * 0.3, screen_height * 0.8)

        stay_text = stat_font.render('STAY HOME', True, black)
        stay_text_rect = stay_text.get_rect()
        stay_text_rect.center = (screen_width * 0.6, screen_height * 0.8)

        hospital_text = stat_font.render('HOSPITAL', True, black)
        hospital_text_rect = hospital_text.get_rect()
        hospital_text_rect.center = (screen_width * 0.8, screen_height * 0.8)

        display_surface.blit(work_text, work_text_rect)
        display_surface.blit(protest_text, protest_text_rect)
        display_surface.blit(stay_text, stay_text_rect)
        display_surface.blit(hospital_text, hospital_text_rect)

        pygame.display.update()

        decision = None

        while not decision:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            if pygame.mouse.get_pressed()[0]:
                if work_text_rect.collidepoint(pygame.mouse.get_pos()):
                    decision = 1

                if protest_text_rect.collidepoint(pygame.mouse.get_pos()):
                    decision = 2
                if stay_text_rect.collidepoint(pygame.mouse.get_pos()):
                    decision = 3
                if hospital_text_rect.collidepoint(pygame.mouse.get_pos()):
                    decision = 4

        if decision == 1:
            player.goes_to_work()

        elif decision == 2:
            player.goes_to_protest()
        elif decision == 3:
            player.stays_home()
        else:
            player.goes_to_hospital()
        game.pollution += pollution_increase

        if not player.in_hospital:
            player.money -= player.cost_of_living

        game_stat = Game_state.AFTER_DECISION

    elif game_stat == Game_state.AFTER_DECISION:
        if pygame.mouse.get_pressed()[0]:
            game_stat = Game_state.DECISION

    for event in pygame.event.get():
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()
            quit()
        # Draws the surface object to the screen.

        pygame.display.update()
