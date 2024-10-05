from enum import Enum


class Game:
    def __init__(self, start_date="2024-01-01"):
        self.date = start_date

        self.pollution = 0                  # FROM 0 TO 10
        self.government_is_aware = False

    def game_over(self):
        return


class Player:

    def __init__(self, health=10, money=2000):
        self.health = health
        self.money = money

        self.wage = 2000
        self.protests_attended = 0
        self.starving = False
        self.illnesses = set()

    def stays_home(self):
        self.health += 3

    def goes_to_work(self):
        self.money += self.wage

    def goes_to_protest(self):
        self.protests_attended += 1

    def goes_to_hospital(self):
        self.health += 5
        self.money -= self.wage

    def is_alive(self):
        return self.health > 0

    def apply_illness_affects(self):
        illnesses = self.illnesses

        if Illness.IRRITATION in illnesses:
            self.health -= 5
        if Illness.HEADACHES in illnesses:
            self.wage *= 0.95
        if Illness.BREATHING_PROBLEMS in illnesses:
            self.health -= 10
            self.wage *= 0.95


class Newspaper:
    def __init__(self, date, local_news, poster):
        self.date = date
        self.local_news = local_news
        self.poster = poster


class Illness(Enum):
    HEADACHES = 1
    BREATHING_PROBLEMS = 2
    IRRITATION = 3

    ASTHMA = 4
    CARDIOVASCULAR_DISEASE = 5

    CANCER = 6
    STROKE = 7
    PNEUMONIA = 8


class Pollution(Enum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3


