import sqlite3 as sl


def init():
    con = sl.connect('tentacup.db')

    with con:
        con.execute(
            """CREATE TABLE TEAM (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT, tag TEXT, act BOOL, 
            elo INTEGER);""")

    sql = 'INSERT INTO TEAM (id, name, tag, act, elo) values(?, ?, ?, ?, ?)'
    elo = 1000
    # Num/Id | Nom Equipe | Tag | 1 = active, 0 = archivée | elo
    data = [
        (0, 'Dépannage', 'HELP', 0, elo),
        (1, 'Confrérie de la choppe débordante', 'CCD', 1, elo),
        (2, 'Poulpeurs de Mer - Kraken', 'ᴥ - Kraken', 0, elo),
        (3, 'Ashen Hearts', 'AH', 0, elo),
        (4, 'Lost Wolves', 'LW-Ex', 0, elo),
        (5, 'TortugA', '𝕋 - A', 0, elo),
        (6, 'Dans Ta Chaloupe', 'DTC', 0, elo),
        (7, 'Folie de Cthullhu - Yog', 'Ƒ𝔬𝔲 - Yog', 1, elo),
        (8, 'Devils Of Seas - Manta', '𝒟o𝒮 Manta', 0, elo),
        (9, 'Arche du Grog - Ex', '𝐆𝖗𝖔𝖌🍻 - Ex', 0, elo),
        (10, 'Folie de Cthullhu - B', 'Ƒ𝔬𝔲', 0, elo),
        (11, 'Les Contrebandiers De Neptune - EX', 'LcdN-EX', 0, elo),
        (12, 'Poulpeurs de Mer - Leviathan - EX', 'ᴥ - Leviathan-EX', 0, elo),
        (13, 'The Ghost Fate', '𝕋𝔾𝔽 - Ex', 0, elo),
        (14, 'Legends of Yesterday Souls - A', '𝕃𝕐𝕊', 1, elo),
        (15, "Les Chasseurs d'Âmes", 'LCA', 0, elo),
        (16, 'Back To Skull', 'B2S', 0, elo),
        (17, "KGB", "☭", 0, elo),
        (18, 'Legends of Yesterday Souls - B', '𝕃𝕐𝕊', 0, elo),
        (19, "The Forsaken Guards", "FG", 0, elo),
        (20, "Born On Boat", "BOB", 0, elo),
        (21, "Pirates Givrés", "PG- A", 1, elo),
        (22, "Hearthless of Paradise", "HOP - A", 0, elo),
        (23, 'Devils Of Seas - Mobula', '𝒟o𝒮 Mobula', 0, elo),
        (24, 'Fallen Angels', 'FΛ', 0, elo),
        (25, "Back 2 Fond de Panier", "B2P", 0, elo),
        (26, 'TortugB', '𝕋 - B', 1, elo),
        (27, "The Groggers", "𝐆𝖗𝖔𝖌𝖌𝖊𝖗𝖘🍻", 0, elo),
        (28, "La Folie de Cthulhu - Shub", "Ƒ𝔬𝔲 - Shub", 1, elo),
        (29, "Five Coconuts - 1", "[ꜰ╳ᴄ] - 1", 0, elo),
        (30, 'Les Contrebandiers De Neptune', 'LcdN', 0, elo),
        (31, "Glimmer Hope", "₲H̷", 0, elo),
        (32, "Hearthless of Paradise", "HOP - B", 0, elo),
        (33, "Los Grogos", "𝐆𝖗𝖔𝖌𝖔𝖘", 1, elo),
        (34, "Five Coconuts - 2", "[ꜰ╳ᴄ] - 2", 0, elo),
        (35, 'The Ghost Fate', '𝕋𝔾𝔽', 0, elo),
        (36, "Les Pirates Gros Givrés", "PG - B", 0, elo),
        (37, "Fish & Ships", "F&S", 1, elo),
        (38, 'Poulpeurs de Mer - Leviathan', 'ᴥ - Leviathan', 1, elo),
        (39, "Death Dealers - 1", "𝕯𝕯 - 1", 0, elo),
        (40, "Death Dealers - 2", "𝕯𝕯 - 2", 0, elo),
        (41, "Born On Boat Intervention Système", "BOBIS", 0, elo),
        (42, 'Lost Wolves', 'LW', 0, elo),
        (43, 'Devils Of Seas - Manta', '𝒟o𝒮 Manta', 0, elo),
        (44, 'Poulpeurs de Mer - Kraken', 'ᴥ - Kraken', 1, elo),
        (45, "Fish & Sinks", "F&S - 2", 0, elo),
        (46, "Le Hollandais Violent", "𝐿𝐻𝒱", 1, elo),
        (47, "Le Hollandais Violent 2 - Ex", "𝐿𝐻𝒱 - 2 - Ex", 0, elo),
        (48, "Five Coconuts", "[ꜰ╳ᴄ]", 0, elo),
        (49, 'Devils Of Seas - 2', '𝒟o𝒮 - 2', 0, elo),
        (50, 'Vulvy Army', 'VA', 0, elo),
        (51, "Grenouilles Ðe Ͼombat", "GÐϾ", 1, elo),
        (52, "Dans Ta Barque", "DTB", 1, elo),
        (53, "Death Angel", "ÐΛ", 1, elo),
        (54, "Hearthless of Paradise", "HOP - C", 0, elo),
        (55, "Four on Fort", "4Ø4", 1, elo),
        (56, "La Folie de Cthulhu - Nyar", "Ƒ𝔬𝔲 - Nyar", 1, elo),
        (57, "2 Old Crew", "𝟚𝕠𝕝𝕕", 1, elo),
        (58, "404 red", "404 red", 1, elo),
        (59, "𝕋𝕙𝕖 𝔾𝕙𝕠𝕤𝕥 𝔽𝕝𝕒𝕞𝕖", "𝕋𝔾𝔽", 1, elo),
        (60, "Fish & Ships - Branchie Belliqueuse", "F&S - Branchie", 1, elo),
        (61, "Le Hollandais Violent 2", "𝐿𝐻𝒱 - 2", 1, elo),
        (62, 'Legends of Yesterday Souls - B', '𝕃𝕐𝕊', 1, elo),
        (63, 'Arche du Grog', '𝐆𝖗𝖔𝖌🍻', 1, elo),
        (64, "Rocks", '𝓡𝓞𝓒', 1, elo),
    ]

    with con:
        con.executemany(sql, data)