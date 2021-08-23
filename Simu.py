# elo SoT Test
from copy import copy
from random import randint, shuffle, random, sample
from DB_Methods import elo


class Team:
    def __init__(self, name, power, id):
        self.name = name
        self.power = power
        self.elo = 1000
        self.rank = []
        self.exp = 0
        self.score = 0
        self.points = 0
        self.tot = 0
        self.id = id
        self.games = 0

    def __str__(self):
        return ("Ranks:  " + str(self.rank) + " | Games: " + str(self.games) + " | Elo: " + str(
            round(self.elo)) + " | " + self.name + " (" + str(self.power) + ")")

    def __repr__(self):
        return str(self)


def modif(power, mod):
    p = power + (random() - 0.5) * mod
    if p > 100:
        p = 100
    return round(p)


def scrim(lineup, nb):
    teams = []
    lineup.sort(key=lambda x: x.elo, reverse=True)
    for i in lineup:
        teams.append(copy(i))
    # Starting Scrim
    for i in teams:
        i.power = modif(i.power, 20)
        i.points = 0
        i.tot = 0
    for i in range(4):
        for j in teams:
            j.score = 0
        fight(teams)
        # End of Round
        # for j in teams:
        # print(j)
        # -> Results of last round
        # print()
        point = 9
        for j in teams:
            j.tot += j.score
            j.points = point
            point -= 2
        teams.sort(key=lambda x: x.points, reverse=True)
    rank = 1
    for i in teams:
        i.rank[nb] = rank
        rank += 1
    elo(lineup)


def fight(teams):
    for i in teams:
        i.score = modif(i.power, 5) * randint(50, 100)
    return teams.sort(key=lambda x: x.score, reverse=True)


def roll(all):
    shuffle(all)
    teams = sample(all, 15)
    return [teams[i:i + 5] for i in range(0, len(teams), 5)]


# Jeu d'essai
all = [Team("B2S", 70, 1), Team("CCD", 75, 2), Team("ᴥ", 75, 3), Team("LW", 70, 4), Team("BOB", 70, 5),
       Team("Grog", 50, 6),
       Team("Fou", 60, 7), Team("Tortuga", 65, 8), Team("FXC", 50, 10), Team("KGB", 40, 11), Team("LHV", 80, 12),
       Team("Hostyl", 90, 13),
       Team("Noob", 10, 14), Team("Odin's", 90, 15), Team("Shtyka", 100, 16), Team("RSE", 80, 17),
       Team("Potato", 30, 18),
       Team("Chips", 25, 19), Team("Frite", 20, 20)]

for i in range(12):  # Nombre de scrims
    for j in all:
        j.rank.append(0)
    teams = roll(all)
    for j in teams:
        scrim(j, i)
all.sort(key=lambda x: x.elo, reverse=True)
for i in all:
    print(i)
