import random

CHOICES = ["камень", "бумага", "ножницы"]
RESULTS = {
    ("камень", "бумага"): "Вы проиграли",
    ("бумага", "ножницы"): "Вы проиграли",
    ("ножницы", "камень"): "Вы проиграли",
    ("бумага", "камень"): "Вы победили",
    ("ножницы", "бумага"): "Вы победили",
    ("камень", "ножницы"): "Вы победили",
    ("камень", "камень"): "Ничья",
    ("бумага", "бумага"): "Ничья",
    ("ножницы", "ножницы"): "Ничья"
}


def get_computer_choice():
    return random.choice(CHOICES)


def determine_winner(player_choice, computer_choice):
    if (player_choice, computer_choice) in RESULTS:
        return RESULTS[(player_choice, computer_choice)]
    else:
        return "Invalid choice"


def play_game(player_choice, computer_choice):
    result = determine_winner(player_choice, computer_choice)
    return result