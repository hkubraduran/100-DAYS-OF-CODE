"""
Project Name: Blackjack Capstone Project
Project Details: The goal of the game is to add up your cards to the largest number
without going over 21.If the cards in your hand add up the more than 21,
then it's called a bust and it means you lose immediately.
All the cards from  2 to 10 count as their face value.
But the Jack, King, Queen are the special cards and count as 10(each one)
The other special card is Ace. It can either count as a 1 towards your total,
or it can count as 11. And depending on whether, if you've gone over 21 or whether if you're under 21,
you can decide which value you want your Ace to represent.
"""
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
import random
from art import logo
end_of_the_game = False
card_list = cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []
def user_turn():
    card = random.choice(card_list)
    user_cards.append(card)
    return user_cards
def dealer():    #dealer
    card = random.choice(card_list)
    dealer_cards.append(card)
    return dealer_cards
def user_score(user_list):
    if "1" in user_list:
        if sum(user_list) + 10 < 21:
            return sum(user_list) + 10
        else :
            return sum(user_list)
    return sum(user_list)
    #score = 0
    #for i in user_list:
    #   score += i
def dealer_score(dealer_list):
    if "1" in dealer_list:
        if sum(dealer_list) + 10 < 21:
            return sum(dealer_list) + 10
        else:
            return sum(dealer_list)
    return sum(dealer_list)
def check_winner(score_user, score_dealer):
        if score_user > 21:     #it's called a bust
            answer = "You lose."
            print("bust")
        elif score_dealer > 21:
            answer = "You win"
        elif score_user < 21 and score_dealer < 21:
            if score_user > score_dealer:
                answer = "You win"
            elif score_dealer == score_user:
                answer = "Draw"
            elif score_dealer < 17 and score_dealer < score_user:
                answer = "hit"  #get another card
            else :
                answer = "You lose."
        return answer
#iki taraf da <21  ise, dealer < 17 ve dealer < user ise:1 kart daha çekilir
while not end_of_the_game:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play == "y":
        #first clear the screen and then start the game
        print(logo)
        # for i in range(0,2):
        #     user_turn()
        #     dealer()
        user_turn()
        user = user_turn()
        dealer()
        comp = dealer()
        # user = user_turn()
        # comp = dealer()
        u_score = user_score(user_list=user)
        d_score = dealer_score(dealer_list=comp)
        print(f"Your cards: {user}, current score: {u_score}")
        print(f"Computer's first card: {comp[0]}")
        again = True
        while again :
            if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
                user = user_turn()
                u_score = user_score(user_list=user)
                print(f"Your cards: {user}, current score: {u_score}")
                print(f"Computer's cards: {comp}")
                if u_score > 21:
                    again = False
            else :
                again = False

        print(f"Your final hand: {user}, current score: {u_score}")
        print(f"Computer's final hand: {comp}")
        print(check_winner(score_user=u_score, score_dealer=d_score))
    else :
        end_of_the_game = True
        print("End of the game.\nGoodbye...")

"""TODO: ikişer kart çekilir fakat dealer ın ikinci kartını göremeyiz.
user bir kart daha çekerse ve eğer toplam 21den çoksa dealer ın kartını görmeden 
kaybetmiş oluyoruz eğer 21den kğçğkse ve başka kart çekmek istemezsek dealer ın kartı açılır
--eğer kartlar eşitse = draw
--dealerın kartı 21 ise(Ace gelirse toplam 21+ old. için 11 ol. alınır) 
ve dealer >  user ise user lose
iki taraf da <21  ise, dealer < 17 ve dealer < user ise:1 kart daha çekilir

burda karar vermek gerekir
hit:get another card
after the hit, the dealer's card will open 
stand 
if we dont get another card the final hands will print out(The dealer's second card will be shown)
eğer 1 gelirse 21 in altında ya da üstünde olması durumuna göre değeri 1 ya da 11 olarak seçilir
"""