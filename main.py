import random
from classes import *

game = Game()
pollution_level = 0
player = Player()

pollution_increase = 3

play_game = True

while play_game:
    if not player.is_alive():
        game.game_over()

    """ POLLUTION (CAN BE AT THE END) """
    if game.pollution > 7: pollution_level = Pollution.HIGH
    elif game.pollution > 4: pollution_level = Pollution.MEDIUM
    elif game.pollution > 1: pollution_level = Pollution.LOW
    else: pollution_level = Pollution.NONE

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

    """ NEWSPAPER """

    """ PLAYER DECISION """
    decision = int(input("DECIDE (1) WORK, (2) PROTEST, (3) STAY HOME, (4) GO TO HOSPITAL"))

    if decision == 1: player.goes_to_work()
    elif decision == 2: player.goes_to_protest()
    elif decision == 3: player.stays_home()
    else: player.goes_to_hospital()

    """ GAME PROGRESSION """
    if player.protests_attended == 3:
        player.protests_attended = 0
        game.government_is_aware = True

    if game.government_is_aware:
        pollution_increase -= 1
        game.government_is_aware = False

    game.pollution += pollution_increase



