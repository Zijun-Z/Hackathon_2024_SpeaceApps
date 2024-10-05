import random
from classes import *

game = Game()
player = Player()

play_game = True

while play_game:
    if not player.is_alive():
        game.game_over()

    if 0 <= game.pollution < 3:
        illness = random.choice([Illness.IRRITATION, Illness.HEADACHES, Illness.BREATHING_PROBLEMS])
    elif 3 <= game.pollution < 6:
        illness = random.choice([Illness.ASTHMA, Illness.CARDIOVASCULAR_DISEASE])
    else:
        illness = random.choice([Illness.CANCER, Illness.PNEUMONIA, Illness.STROKE])

    player.illnesses.add(illness)
    player.apply_illness_affects()

    # show newspaper
    # player decides to go to work, stay home, or protest (or must go to hospital)

