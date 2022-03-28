"""Module Gobblet

Attributes:
    GOBBLET_REPRÉSENTATION (dict): Constante représentant les gobblet des joueurs.

Functions:
    * interpréteur_de_commande - Génère un interpréteur de commande.
    * formater_un_gobblet - Formater la représentation graphique d'un Gobblet.
    * formater_un_joueur - Formater la représentation graphique d'un joueur et de ses piles.
    * formater_plateau - Formater la représentation graphique d'un plateau.
    * formater_jeu - Formater la représentation graphique d'un jeu.
    * formater_les_parties - Formater la liste des dernières parties.
    * récupérer_le_coup - Demander le prochain coup à jouer au joueur.
"""
from argparse import ArgumentParser

# Voici la représentation des Gobblets, n'hésitez pas à l'utiliser.
# 1 pour le joueur 1, 2 pour le joueur 2.
GOBBLET_REPRÉSENTATION = {
    1: [" ▫ ", " ◇ ", " ◯ ", " □ "],
    2: [" ▪ ", " ◆ ", " ● ", " ■ "],
}


def interpréteur_de_commande():
    """Interpreteur de commande

    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
                   Cette objet aura l'attribut IDUL représentant l'idul du joueur
                   et l'attribut lister qui est un booléen True/False.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('IDUL', metavar='IDUL', help='IDUL du joueur')

    parser.add_argument('-l', '--lister', action='store_true', help="Lister les parties existantes")
        
    args = parser.parse_args()

    # Complétez le code ici
    # vous pourriez aussi avoir à ajouter des arguments dans ArgumentParser(...)

    return args


def formater_un_gobblet(gobblet):
    """Formater un Gobblet

    Args:
        gobblet (list): liste vide ou de 2 entier [x, y] représentant le Gobblet

    Returns:
        str: Représentation du Gobblet pour le bon joueur
    """
    
    if gobblet != []:
        return GOBBLET_REPRÉSENTATION[gobblet[0]][gobblet[1]]
    else :
        return "   "
        


def formater_un_joueur(joueur):
    """Formater un joueur

    Args:
        joueur (dict): dictionnaire contenant le nom du joueurs et ses piles de Gobblet

    Returns:
        str: Représentation du joueur et de ses piles de Gobblet
    """
    gobblets = []

    for i in joueur['piles'] :
        gobblets.append(formater_un_gobblet(i))

    gobblets="".join(gobblets)

    return (joueur['nom'] + ":   " + gobblets)


def formater_plateau(plateau):
    """Formater un plateau

    Args:
        plateau (list): plateau de jeu 4 x 4

    Returns:
        str: Représentation du plateau avec ses Gobblet
    """
    gobs = []
    plateau_form = str()
    if plateau ==  [[[], [], [], []],[[], [], [], []],[[], [], [], []],[[], [], [], []],]:
        plateau_form = (
        "3   |   |   |   \n"
        " ───┼───┼───┼───\n"
        "2   |   |   |   \n"
        " ───┼───┼───┼───\n"
        "1   |   |   |   \n"
        " ───┼───┼───┼───\n"
        "0   |   |   |   \n"
        "  0   1   2   3 "
    )
    else:
        for i in plateau :
            for j in i :
                gobs.append(formater_un_gobblet(j))

        plateau_form = "3{0}|{1}|{2}|{3}\n ───┼───┼───┼───\n2{4}|{5}|{6}|{7}\n ───┼───┼───┼───\n1{8}|{9}|{10}|{11}\n ───┼───┼───┼───\n0{12}|{13}|{14}|{15}\n  0   1   2   3".format(gobs[0], gobs[1], gobs[2], gobs[3], gobs[4], gobs[5], gobs[6], gobs[7], gobs[8], gobs[9], gobs[10], gobs[11], gobs[12], gobs[13], gobs[14], gobs[15])
    return plateau_form

def formater_jeu(plateau, joueurs):
    """Formater un jeu

    Args:
        plateau (list): plateau de jeu 4 x 4
        joueurs (list): list de dictionnaire contenant le nom du joueurs et ses piles de Gobblet

    Returns:
        str: Représentation du jeu
    """
    jeu = "          0  1  2\n"
    for i in joueurs:
        jeu+="{0}: {1}  {2}  {3}\n".format(i['nom'], formater_un_gobblet(i['piles'][0]), formater_un_gobblet(i['piles'][1]), formater_un_gobblet(i['piles'][2]))

    jeu += "\n"+str(formater_plateau(plateau))

    return jeu


def formater_les_parties(parties):
    """Formater une liste de parties

    L'ordre doit être exactement la même que ce qui est passé en paramètre.

    Args:
        parties (list): Liste des parties

    Returns:
        str: Représentation des parties
    """
    parts = str()
    nb = 1
    gagnant = str()

    for j in parties :
        if j["gagnant"] == None :
            gagnant = ""
        else :
            gagnant = ", gagnant: {0}".format(j["gagnant"])
        parts += "{0}: {1}, {2} vs {3}{4}\n".format(nb, j["date"], j["joueurs"][0], j["joueurs"][1], gagnant)
        nb+=1
    return parts


def récupérer_le_coup():
    """Récupérer le coup

    Returns:
        tuple: Un tuple composé d'un origine et de la destination.
               L'origine est soit un entier représentant le numéro de la pile du joueur
               ou une liste de 2 entier [x, y] représentant le Gobblet sur le plateau
               La destination estune liste de 2 entier [x, y] représentant le Gobblet
               sur le plateau

    Examples:
        Quel Gobblet voulez-vous déplacer:
        Donnez le numéro de la pile (p) ou la position sur le plateau (x,y): 0
        Où voulez-vous placer votre Gobblet (x,y): 0,1

        Quel Gobblet voulez-vous déplacer:
        Donnez le numéro de la pile (p) ou la position sur le plateau (x,y): 2,3
        Où voulez-vous placer votre Gobblet (x,y): 0,1
    """
    origine = input("Donnez le numéro de la pile (p) ou la position sur le plateau (x,y) : ")
    destination = input("Où voulez-vous placer votre Gobblet ? Donnez des coordonnées (x,y) : ")

    return (origine, destination)