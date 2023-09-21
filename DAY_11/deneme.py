import random
card_list = cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
def user_turn():

    card = random.choice(card_list)
    user_cards.append(card)
    return user_cards
user_turn()
user = user_turn()
