class Game:
    def __init__(self, start_date="2024-01-01"):
        self.date = start_date

        self.pollution_level = 0            # FROM 0 TO 5
        self.government_sensitivity = 0     # FROM 0 TO 5

    def game_over(self):
        return


class Player:

    def __init__(self, health=10, money=2000):
        self.health = health
        self.money = money

        self.wage = 2000
        self.protests_attended = 0
        self.starving = False

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


class Newspaper:
    def __init__(self, date, local_news, poster):
        self.date = date
        self.local_news = local_news
        self.poster = poster


