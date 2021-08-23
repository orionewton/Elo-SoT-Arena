import os
import sqlite3 as sl

from DB_init import init


class Team:
    def __init__(self, id, elo):
        self.elo = elo
        self.id = id
        self.exp = 0


def scores():  # affichage des scores par ID
    con = sl.connect('tentacup.db')
    with con:
        data = con.execute("SELECT elo, id, tag, name FROM TEAM WHERE act = 1 ORDER BY id")  # ORDER BY elo DESC sinon
        for row in data:
            print(row)


def add_team():  # Ajout d'équipe dans la base
    print("Nom de l'équipe complet:")
    print("Précision du roster possible, exemple: Poulpeurs de Mer - Kraken")
    name = str(input())
    print("Tag de l'équipe (laisser vide si inéxistant)")
    tag = str(input())
    con = sl.connect('tentacup.db')
    with con:
        con.execute('INSERT INTO TEAM (name, tag, elo) values("' + name + '", "' + tag + '",1 ,1000)')


def mod_team():  # Modifier une team dans la base
    con = sl.connect('tentacup.db')
    with con:
        data = con.execute("SELECT id, name FROM TEAM ORDER BY id")
        for row in data:
            print(row)
    print("Choisissez l'équipe à modifier (entrez son numéro): ?")
    num = input()
    with con:
        data = con.execute("SELECT * FROM TEAM WHERE id = " + num)
        for row in data:
            print(row)
    print("Que voulez vous modifier ?")
    print("1 - Nom")
    print("2 - Tag")
    print("3 - elo")
    print("4 - Supprimer l'équipe")
    mod = int(input())
    while mod != 1 and mod != 2 and mod != 3 and mod != 4:
        print("Input error, try again")
        mod = int(input())
    if mod == 1 or mod == 2 or mod == 3:
        print("Entrez la nouvelle valeur")
        new = input()
        with con:
            if mod == 1:
                con.execute("UPDATE TEAM SET name = '" + new + "' WHERE id = " + num)
            elif mod == 2:
                con.execute("UPDATE TEAM SET tag = '" + new + "' WHERE id = " + num)
            else:
                con.execute("UPDATE TEAM SET elo = '" + str(new) + "' WHERE id = " + num)
    else:
        print("Confirmez la suppréssion de l'équipe: Y/N")
        conf = input()
        while conf != 'Y' and conf != 'N':
            print("Input error, try again")
            conf = input()
        if conf == 'Y':
            with con:
                con.execute("DELETE FROM TEAM WHERE id = " + num)


def scrim():  # Selection et résultats des équipes d'un scrim
    con = sl.connect('tentacup.db')
    with con:
        data = con.execute("SELECT id, tag, name FROM TEAM ORDER BY id")
        for row in data:
            print(row)
    print("Indiquez les numéros des équipes participantes (une à la fois)")
    teams = []
    for i in range(5):
        teams.append(int(input()))
    print("Les équipes participantes sont:")
    with con:
        for i in teams:
            data = con.execute("SELECT id, name FROM TEAM WHERE id = " + str(i))
            for row in data:
                print(row)
    print("Toujours avec les numéros, indiquez le classement du premier au dernier")
    ranking = []
    for i in range(5):
        ranking.append(int(input()))
    lineup = []
    for i in ranking:
        with con:
            data = con.execute("SELECT elo FROM TEAM WHERE id = " + str(i))
            for row in data:
                val = row[0]
        lineup.append(Team(i, int(val)))
    elo(lineup)
    for i in lineup:
        with con:
            con.execute("UPDATE TEAM SET elo = '" + str(i.elo) + "' WHERE id = " + str(i.id))


def redo():  # Remise à jour depuis reroll.txt
    os.remove("tentacup.db")
    init()
    all = []
    f = open("reroll.txt", "r")
    for line in f:
        all.append(int(line.strip()))
    f.close()
    ind = 0
    con = sl.connect('tentacup.db')
    for n in range(int(len(all) / 5)):
        ranking = []
        for i in range(5):
            ranking.append(all[ind])
            ind += 1
        lineup = []
        for i in ranking:
            with con:
                data = con.execute("SELECT elo FROM TEAM WHERE id = " + str(i))
                for row in data:
                    val = row[0]
            lineup.append(Team(i, int(val)))
        elo(lineup)
        for i in lineup:
            with con:
                con.execute("UPDATE TEAM SET elo = '" + str(i.elo) + "' WHERE id = " + str(i.id))


def elo(lineup):  # Formule Elo
    avg_elo = 0
    max_elo = 0
    min_elo = 2000
    n = 5
    for i in lineup:
        if i.id == 0:
            n -= 1
        else:
            avg_elo += i.elo
            if i.elo > max_elo:
                max_elo = i.elo
            if i.elo < min_elo:
                min_elo = i.elo
    avg_elo = int(avg_elo / n)
    print(avg_elo)
    for i in lineup:
        i.exp = round((1.0 / (4 + pow(10, (avg_elo - i.elo) / 4))), 3)
        print(str(i.id) + " | " + str(i.elo) + " | " + str(i.exp))
    print()
    mod = 20
    for i in lineup:
        var1 = abs(i.elo - min_elo)
        var2 = abs(max_elo - i.elo)
        moy = abs(i.elo - avg_elo)
        if moy >= 10 or var1 > 20 or var2 > 20:
            diff = max(moy, var1, var2)
            if mod > 0:
                if diff == var1 and diff > 30:
                    p = 0.5
                else:
                    if i.elo > avg_elo:
                        if diff > 20:
                            diff = max(moy, var2)
                        # p = max(1 - diff / 10, 0.5)
                        p = max(round(diff / 10 - 2, 2), 0.5)
                    else:
                        p = 1.2
            else:
                if i.elo > avg_elo:
                    p = 1.2
                else:
                    p = 0.2
        else:
            p = 1.2
        if i.exp < 0.2 and mod < 0:
            p = min(1, p)
        coeff = p - i.exp
        if coeff == 0:
            coeff = 0.2
        i.elo = int(i.elo + mod * coeff)
        mod -= 10
        # print(str(i.id) + " | " + str(i.elo) + " | " + str(i.exp) + " | " + str(p))
        if i.id == 0:
            i.elo = 1000
