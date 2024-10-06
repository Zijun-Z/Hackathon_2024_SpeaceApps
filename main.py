import pygame
from classes import *

""" GAME LOGIC STUFF """
game = Game()
player = Player()

pollution_level = 0
pollution_increase = 3

play_game = True

""" PYGAME STUFF """
pygame.init()
game_state = Game_state.MENU

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SYSTEM_INFO = pygame.display.Info()
WIDTH = SYSTEM_INFO.current_w * 0.8
HEIGHT = SYSTEM_INFO.current_h * 0.8

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SyntaxError:')

font = pygame.font.SysFont('arial', 32)

start_text = font.render('Start game', True, BLACK)
start_text_rect = start_text.get_rect()
start_text_rect.center = (WIDTH // 2, HEIGHT // 2)

""" MAIN GAME LOOP """
while play_game:
    display_surface.fill(WHITE)

    """ MAIN MENU """
    if game_state == Game_state.MENU:
        display_surface.blit(start_text, start_text_rect)

        if pygame.mouse.get_pressed()[0]:
            if start_text_rect.collidepoint(pygame.mouse.get_pos()):
                game_state = Game_state.PLAYING

    # GAMEPLAY
    elif game_state == Game_state.PLAYING:

        """ POLLUTION (CAN BE AT THE END) """
        if game.pollution > 30:
            pollution_level = Pollution.HIGH
        elif game.pollution > 20:
            pollution_level = Pollution.MEDIUM
        elif game.pollution > 10:
            pollution_level = Pollution.LOW
        else:
            pollution_level = Pollution.NONE

        """ ILLNESSES """
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
        print(player.illnesses)

        """ NEWSPAPER """
        if pollution_level == Pollution.HIGH: choice_index = 5
        elif pollution_level == Pollution.MEDIUM: choice_index = 3
        elif pollution_level == Pollution.LOW: choice_index = 2
        else: choice_index = 1

        newspaper = Newspaper(player.did_protest, game.government_did_aware, choice_index)
        newspaper.print()

        game.government_did_aware = False
        player.did_protest = False

        """ PLAYER DECISION """
        work_text = font.render('WORK', True, BLACK)
        work_text_rect = work_text.get_rect()
        work_text_rect.center = (WIDTH // 2 - 200, HEIGHT // 2)

        protest_text = font.render('PROTEST', True, BLACK)
        protest_text_rect = protest_text.get_rect()
        protest_text_rect.center = (WIDTH // 2 + 200, HEIGHT // 2)

        stay_text = font.render('STAY HOME', True, BLACK)
        stay_text_rect = stay_text.get_rect()
        stay_text_rect.center = (WIDTH // 2 - 200, HEIGHT // 2 + 200)

        hospital_text = font.render('HOSPITAL', True, BLACK)
        hospital_text_rect = hospital_text.get_rect()
        hospital_text_rect.center = (WIDTH // 2 + 200, HEIGHT // 2 + 200)

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

    #     """ GAME PROGRESSION """
    #     if player.protests_attended == 3:
    #         player.protests_attended = 0
    #         game.government_is_aware = True
    #         game.government_did_aware = True
    #
    #     if game.government_is_aware:
    #         pollution_increase -= 1
    #         game.government_is_aware = False
    #         game.government_did_aware = True
    #
    #     if pollution_increase == 0:
    #         print("you win bozo")
    #         break
    #
    #     game.pollution += pollution_increase
    #
    #     if not player.in_hospital:
    #         player.money -= player.cost_of_living
    #
    #     print(f"health: {player.health}, money: {player.money}, pollution: {pollution_level}, "
    #           f"protests attended: {player.protests_attended}, pollution increase: {pollution_increase}")
    #     print("-----------------------------")

    """ EVENT HANDLING """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    """ ACTUALLY UPDATE SCREEN """
    pygame.display.update()
