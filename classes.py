class Game:
    def __init__(self, date="2024-01-01"):
        self.date = date

        self.pollution_level = 0            # FROM 0 TO 5
        self.government_sensitivity = 0     # FROM 0 TO 5

    def next_day(self):
        return


class Player:
    def __init__(self, health=10, money=500):
        self.health = health
        self.money = money

        self.protests_attended = 0
        self.starving = False

    def stays_home(self):
        return

    def goes_to_work(self):
        return

    def goes_to_protest(self):
        return

    def goes_to_hospital(self):
        return

class Newspaper:
    def __init__(self, date, local_news, poster):
        self.date = date
        self.local_news = local_news
        self.poster = poster

