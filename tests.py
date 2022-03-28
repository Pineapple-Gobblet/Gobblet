"""Tests Gobblet

Ce module contient des tests unitaires pour le projet Gobblet.
"""
from gobblet import (
    formater_jeu,
    formater_plateau,
    formater_un_joueur,
    formater_un_gobblet,
)


def test_formater_un_gobblet_vide():
    gobblet = []
    attendu = "   "

    résultat = formater_un_gobblet(gobblet)

    assert résultat == attendu, "Échec du test de formater_un_gobblet avec une gobblet vide"


def test_formater_un_gobblet_non_vide():
    gobblet = [1, 2]
    attendu = " ◯ "

    résultat = formater_un_gobblet(gobblet)

    assert résultat == attendu, "Échec du test de formater_un_gobblet avec une gobblet non vide"


def test_formater_un_jouer_sans_piles():
    joueur = {
        "nom": "Alfred",
        "piles": [
            [],
            [],
            [],
        ],
    }

    attendu = "Alfred:            "

    résultat = formater_un_joueur(joueur)

    assert résultat == attendu, "Échec du test de formater_un_joueur sans des piles"


def test_formater_un_jouer_avec_piles():
    joueur = {
        "nom": "Alfred",
        "piles": [
            [1, 3],
            [1, 3],
            [1, 3],
        ],
    }

    attendu = "Alfred:  □   □   □ "

    résultat = formater_un_joueur(joueur)

    assert résultat == attendu, "Échec du test de formater_un_joueur avec des piles"


def test_formater_un_plateau_vide():
    plateau = [
        [[], [], [], []],
        [[], [], [], []],
        [[], [], [], []],
        [[], [], [], []],
    ]

    attendu = (
        "3   |   |   |   \n"
        " ───┼───┼───┼───\n"
        "2   |   |   |   \n"
        " ───┼───┼───┼───\n"
        "1   |   |   |   \n"
        " ───┼───┼───┼───\n"
        "0   |   |   |   \n"
        "  0   1   2   3 "
    )

    résultat = formater_plateau(plateau)

    assert résultat == attendu, "Échec du test de formater_plateau avec un plateau vide"


def test_formater_un_plateau_plein():
    plateau = [
        [[1, 0], [1, 1], [2, 0], [2, 1]],
        [[2, 2], [2, 3], [1, 2], [1, 3]],
        [[1, 0], [1, 1], [2, 0], [2, 1]],
        [[2, 2], [2, 3], [1, 2], [1, 3]],
    ]

    attendu = (
        "3 ▫ | ◇ | ▪ | ◆ \n"
        " ───┼───┼───┼───\n"
        "2 ● | ■ | ◯ | □ \n"
        " ───┼───┼───┼───\n"
        "1 ▫ | ◇ | ▪ | ◆ \n"
        " ───┼───┼───┼───\n"
        "0 ● | ■ | ◯ | □ \n"
        "  0   1   2   3 "
    )

    résultat = formater_plateau(plateau)

    assert résultat == attendu, "Échec du test de formater_plateau avec un plateau plein"


def test_formater_un_jeu():
    plateau = [
        [[], [], [], []],
        [[], [], [], []],
        [[], [], [], []],
        [[], [], [], []],
    ]
    joueurs = [
        {
            "nom": "Robin",
            "piles": [
                [1, 3],
                [1, 3],
                [1, 3],
            ],
        },
        {
            "nom": "Alfred",
            "piles": [
                [2, 3],
                [2, 3],
                [2, 3],
            ],
        },
    ]

    attendu = (
        "         0   1   2 \n"
        " Robin:  □   □   □ \n"
        "Alfred:  ■   ■   ■ \n\n"
        "3   |   |   |   \n"
        " ───┼───┼───┼───\n"
        "2   |   |   |   \n"
        " ───┼───┼───┼───\n"
        "1   |   |   |   \n"
        " ───┼───┼───┼───\n"
        "0   |   |   |   \n"
        "  0   1   2   3 "
    )

    résultat = formater_jeu(plateau, joueurs)

    assert résultat == attendu, "Échec du test de formater_jeu"


if __name__ == "__main__":
    test_formater_un_gobblet_vide()
    print("Test de formater_un_gobblet_vide réussi")
    test_formater_un_gobblet_non_vide()
    print("Test de formater_un_gobblet_non_vide réussi")
    test_formater_un_jouer_sans_piles()
    print("Test de formater_un_jouer_sans_piles réussi")
    test_formater_un_jouer_avec_piles()
    print("Test de formater_un_jouer_avec_piles réussi")
    test_formater_un_plateau_vide()
    print("Test de formater_un_plateau_vide réussi")
    test_formater_un_plateau_plein()
    print("Test de formater_un_plateau_plein réussi")
    test_formater_un_jeu()
    print("Test de formater_un_jeu réussi")
