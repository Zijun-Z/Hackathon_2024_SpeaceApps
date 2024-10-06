from enum import Enum
from newspaper_text import *
import random

class Game:
    def __init__(self, start_date="2024-01-01"):
        self.date = start_date

        self.pollution = 0                  # FROM 0 TO 10
        self.government_is_aware = False
        self.government_did_aware = False

    def game_over(self):
        print("you died nerd")


class Player:

    def __init__(self, health=200, money=4000):
        self.health = health
        self.money = money

        self.wage = 3000
        self.protests_attended = 0
        self.starving = False
        self.illnesses = set()
        self.in_hospital = False
        self.cost_of_living = 1000
        self.did_protest = False

    def stays_home(self):
        self.health += 10
        remove = set()

        for illness in self.illnesses:
            if illness.value > 3:
                remove.add(illness)

        for illness in remove:
            self.illnesses.remove(illness)

    def goes_to_work(self):
        self.money += self.wage

    def goes_to_protest(self):
        self.did_protest = True
        self.protests_attended += 1

    def goes_to_hospital(self):
        self.in_hospital = True
        self.health += 60
        self.money -= 2 * self.wage

        remove = set()

        for illness in self.illnesses:
            if illness.value >= 5:
                remove.add(illness)

        for illness in remove:
            self.illnesses.remove(illness)

    def is_alive(self):
        return self.health > 0

    def apply_illness_affects(self):
        illnesses = self.illnesses

        if Illness.IRRITATION in illnesses:
            self.health -= 5
        if Illness.HEADACHES in illnesses:
            self.wage -= 50
        if Illness.BREATHING_PROBLEMS in illnesses:
            self.health -= 5
            self.wage -= 50
        if Illness.ASTHMA in illnesses:
            self.health -= 5
            self.wage -= 100
        if Illness.CARDIOVASCULAR_DISEASE:
            self.health -= 10
            self.wage -= 50
        if Illness.PNEUMONIA:
            self.health -= 20
            self.wage -= 150
        if Illness.STROKE:
            self.health -= 30
            self.wage -= 200
        if Illness.CANCER:
            self.health -= 30
            self.wage -= 501


class Newspaper:
    def __init__(self, player_protested, government_is_aware, choice_index):
        if player_protested:
            self.protest_news = good_news_options[random.choice([choice_index, choice_index - 1])]
        else:
            self.protest_news = bad_news_options[random.choice([choice_index, choice_index - 1])]

        if government_is_aware:
            self.government_action = random.choice(government_awarded)
        else:
            self.government_action = random.choice(government_havent_awarded)

        self.random_news = random.choice(random_news)

    def print(self):
        print(f"{self.protest_news}\n{self.government_action}\n{self.random_news}")


class Illness(Enum):
    HEADACHES = 1
    BREATHING_PROBLEMS = 2
    IRRITATION = 3

    ASTHMA = 4
    CARDIOVASCULAR_DISEASE = 5

    PNEUMONIA = 6
    STROKE = 7
    CANCER = 8


class Pollution(Enum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Game_state(Enum):
    MENU = 0
    PLAYING = 1
    GAME_OVER = 2


