import random
from classes import *
from newspaper_text import *

game = Game()
pollution_level = 0
player = Player()

pollution_increase = 3

play_game = True


def create_newspaper(boolean, boolean_2, list_index):
    if boolean:
        print(good_news_options[random.choice([list_index, list_index - 1])])
    else:
        print(bad_news_options[random.choice([list_index, list_index - 1])])
    if boolean_2:
        print(government_awarded[random.choice([0, 1])])

    else:
        print(government_havent_awarded[random.choice([0, 1])])

    print(local_news_options[random.choice([0, 7])])
    return boolean == False, boolean_2 == False


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
    print("newspaper stuff")

    if pollution_level == Pollution.HIGH:
        create_newspaper(player.did_protest, game.government_did_aware, 5)

    elif pollution_level == Pollution.MEDIUM:
        create_newspaper(player.did_protest, game.government_did_aware, 3)
    elif pollution_level == Pollution.LOW:
        create_newspaper(player.did_protest, game.government_did_aware, 2)
    else:
        create_newspaper(player.did_protest, game.government_did_aware, 1)

    print(game.government_did_aware)

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
