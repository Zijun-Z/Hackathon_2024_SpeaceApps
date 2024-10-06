import pygame
import random
from classes import *
from newspaper_text import *



game = Game()
pollution_level = 0
player = Player()

pollution_increase = 3

play_game = True

while play_game:
    if not player.is_alive():
        game.game_over()
        break

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
    """
    pollution_level    INCLUDE
    pollution_increase (pollution rate) HAVEN'T INCLUDE
    did player attend protest last round?   INCLUDE
    is government now aware?    HAVEN'T INCLUDE
    
    """
    if pollution_level == Pollution.HIGH: choice_index = 5
    elif pollution_level == Pollution.MEDIUM: choice_index = 3
    elif pollution_level == Pollution.LOW: choice_index = 2
    else: choice_index = 1

    newspaper = Newspaper(player.did_protest, game.government_did_aware, choice_index)
    newspaper.print()

    game.government_did_aware = False
    player.did_protest = False

    """ PLAYER DECISION """
    decision = int(input("DECIDE:  (1) WORK, (2) PROTEST, (3) STAY HOME, (4) GO TO HOSPITAL"))

    if decision == 1:
        player.goes_to_work()
    elif decision == 2:
        player.goes_to_protest()
    elif decision == 3:
        player.stays_home()
    else:
        player.goes_to_hospital()

    """ GAME PROGRESSION """
    if player.protests_attended == 3:
        player.protests_attended = 0
        game.government_is_aware = True
        game.government_did_aware = True

    if game.government_is_aware:
        pollution_increase -= 1
        game.government_is_aware = False
        game.government_did_aware = True

    if pollution_increase == 0:
        print("you win bozo")
        break

    game.pollution += pollution_increase

    if not player.in_hospital:
        player.money -= player.cost_of_living

    print(f"health: {player.health}, money: {player.money}, pollution: {pollution_level}, "
          f"protests attended: {player.protests_attended}, pollution increase: {pollution_increase}")
    print("-----------------------------")
