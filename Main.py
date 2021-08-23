from DB_Methods import *


def main():
    n = True
    while n:
        print("Options de lancements:")
        print("1 - Lancer un scrim")
        # Donner les 5 participants, puis dans l'odre des résultats
        print("2 - Voir les scores")
        # Affiche les elos dans l'ordre des ID
        print("3 - Ajouter une équipe")
        # Ajoute une équipe à la base
        print("4 - Modifier une équipe")
        # Modifier une équipe existante
        print("5 - Reroll Elo")
        # Efface la base et en recrée une avec les scores de "reroll.txt"
        print("6 - Quitter")

        mod = int(input())

        while mod != 1 and mod != 2 and mod != 3 and mod != 4 and mod != 5 and mod != 6:
            print("Input error, try again")
            mod = int(input())

        if mod == 1:
            scrim()
            print()
        elif mod == 2:
            scores()
            print()
        elif mod == 3:
            add_team()
            print()
        elif mod == 4:
            mod_team()
            print()
        elif mod == 5:
            redo()
            print()
        else:
            n = False


if __name__ == "__main__":
    main()
