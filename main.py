import pygame
import random
from classes import *
from newspaper_text import *
from window_display import *

game_stat = Game_state.MENU
game = Game()
pollution_level = 0
player = Player()

pollution_increase = 1.66

play_game = True

display_text = False

mouse_clicked = False  # Add a flag to track mouse click state

title_card = True

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
    if death_screen:
        display_surface.blit(deathScreen, (0, 0))
    else:
        display_surface.blit(backgrounds[b], (0, 0))

    if game_stat == Game_state.MENU:

        if title_card:
            display_surface.blit(titleCard, (0, 0))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            title_card = False
            game_stat = game_stat.DECISION

    elif game_stat == Game_state.DECISION:

        # Render player health and money as text
        player_health_txt = stat_font.render(f"Health: {player.health}", True, black)
        player_health_rect = player_health_txt.get_rect()
        player_health_rect.topright = (1300, 100)  # Set the position for health text

        display_surface.blit(player_health_txt, player_health_rect)

        player_money_txt = stat_font.render(f"Money: {player.money}", True, black)
        player_money_rect = player_money_txt.get_rect()
        player_money_rect.topright = (1300, 140)  # Set the position for money text

        display_surface.blit(player_money_txt, player_money_rect)

        if player.health < 50:
            player_displayed = sick_fatal_good
        elif player.health < 100:
            player_displayed = sick_medium_good
        elif player.health < 150:
            player_displayed = sick_light_good
        else:
            player_displayed = healthy_good

        display_surface.blit(player_displayed, (screen_width * 0.75, 200))

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

        illness_names = [illness.name for illness in player.illnesses]
        illnesses_str = ", ".join(illness_names)
        display_text = f"Current illness: {illnesses_str}"

        player_illnesses_txt = stat_font.render(display_text, True, black)
        player_illnesses_rect = player_illnesses_txt.get_rect()
        player_illnesses_rect.bottomleft = (0, screen_height * 0.8)
        display_surface.blit(player_illnesses_txt, player_illnesses_rect)

        if pollution_level == Pollution.HIGH:
            choice_index = 5
        elif pollution_level == Pollution.MEDIUM:
            choice_index = 3
        elif pollution_level == Pollution.LOW:
            choice_index = 2
        else:
            choice_index = 1
        pygame.draw.rect(display_surface, white, pygame.Rect(0, 100, 900, 300))

        newspaper_protest = Newspaper(player.did_protest, game.government_did_aware, choice_index)
        newspaper_protest_text = newspaper_font.render(newspaper_protest.protest_news, True, black)
        newspaper_protest_rect = newspaper_protest_text.get_rect()
        newspaper_protest_rect.topleft = (0, 100)

        newspaper_government_is_aware = Newspaper(player.did_protest, game.government_did_aware, choice_index)
        newspaper_government_is_aware_text = newspaper_font.render(newspaper_government_is_aware.government_action,
                                                                   True, black)
        newspaper_government_is_aware_rect = newspaper_government_is_aware_text.get_rect()
        newspaper_government_is_aware_rect.topleft = (0, newspaper_protest_rect.y + 100)

        newspaper_local_news = Newspaper(player.did_protest, game.government_did_aware, choice_index)
        newspaper_local_news_text = newspaper_font.render(newspaper_local_news.random_news, True, black)
        newspaper_local_news_rect = newspaper_local_news_text.get_rect()
        newspaper_local_news_rect.topleft = (0, newspaper_government_is_aware_rect.y + 100)

        display_surface.blit(newspaper_protest_text, newspaper_protest_rect)
        display_surface.blit(newspaper_government_is_aware_text, newspaper_government_is_aware_rect)
        display_surface.blit(newspaper_local_news_text, newspaper_local_news_rect)

        game.government_did_aware = False
        player.did_protest = False

        """ PLAYER DECISION """
        work_text = stat_font.render('WORK', True, black)
        work_text_rect = work_text.get_rect()
        work_text_rect.center = (screen_width * 0.1, screen_height * 0.9)

        protest_text = stat_font.render('PROTEST', True, black)
        protest_text_rect = protest_text.get_rect()
        protest_text_rect.center = (screen_width * 0.3, screen_height * 0.9)

        stay_text = stat_font.render('STAY HOME', True, black)
        stay_text_rect = stay_text.get_rect()
        stay_text_rect.center = (screen_width * 0.6, screen_height * 0.9)

        hospital_text = stat_font.render('HOSPITAL', True, black)
        hospital_text_rect = hospital_text.get_rect()
        hospital_text_rect.center = (screen_width * 0.8, screen_height * 0.9)

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

            if pygame.mouse.get_pressed()[0] and not mouse_clicked:
                mouse_clicked = True  # Set the flag when the mouse is clicked
                if work_text_rect.collidepoint(pygame.mouse.get_pos()):
                    player.goes_to_work()
                if protest_text_rect.collidepoint(pygame.mouse.get_pos()):
                    player.goes_to_protest()
                if stay_text_rect.collidepoint(pygame.mouse.get_pos()):
                    player.stays_home()
                if hospital_text_rect.collidepoint(pygame.mouse.get_pos()):
                    player.goes_to_hospital()
            elif not pygame.mouse.get_pressed()[0]:
                mouse_clicked = False  # Reset the flag when the mouse button is released

        game.pollution += pollution_increase
        if b < 18:
            b += 1

        if not player.in_hospital:
            player.money -= player.cost_of_living





    elif game_stat == Game_state.AFTER_DECISION:
        pass

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
