import random
player_in = True
dealer_in = True
game_start = True


# introduction to the game

starting_game = input("Welcome to Blackjack! Please press '1' to play ")
if starting_game == '1':
    game_start = True
else:
    player_in = False
    dealer_in = False
    game_start = False
    print("The game will close.")


# creating deck of cards
player_hand = []
dealer_hand = []
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']*4


# dealing the cards


def deal_card(hand):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)


for _ in range(2):
    deal_card(player_hand)
    deal_card(dealer_hand)


# summation of value of cards


def total(hand):
    total = 0
    face_card = ['J', 'Q', 'K']
    ace_card = ['A']
    for card in hand:
        if card in range(1, 11):
            total += card
        elif card in face_card:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total


while total(player_hand) > 21 and ace_card in player_hand:
    ace_card = 1

# revealing hands and determine whether to hit or stand


def reveal_dealer_hand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    if len(dealer_hand) == 3 and player_in is False:
        return dealer_hand[0], dealer_hand[1]
    if len(dealer_hand) >= 2 and player_in is True:
        return dealer_hand[0]
    if len(dealer_hand) == 4 and player_in is False:
        return dealer_hand[0], dealer_hand[1], dealer_hand[2]
    elif len(dealer_hand) == 4 and player_in is False:
        return dealer_hand[0], dealer_hand[1], dealer_hand[2], dealer_hand[3]
    elif len(dealer_hand) == 5 and player_in is False:
        return dealer_hand[0], dealer_hand[1], dealer_hand[2], dealer_hand[4], dealer_hand[5]
    elif len(dealer_hand) == 6 and player_in is False:
        return dealer_hand[0], dealer_hand[1], dealer_hand[2], dealer_hand[4], dealer_hand[5], dealer_hand[6]


while game_start is True:
    print(f"Dealer has {reveal_dealer_hand()} and ..")
    print(f"You have {player_hand} for a total of {total(player_hand)}")
    break
while player_in or dealer_in:
    if total(player_hand) == 21 and len(player_hand) == 2:
        print("Blackjack! Congratulations, you win!")
        game_start = False
        dealer_in = False
        player_in = False
        break

    elif total(dealer_hand) == 21 and len(dealer_hand) == 2:
        print("Blackjack! The dealer wins!")
        game_start = False
        dealer_in = False
        player_in = False
        break

    if player_in:
        stay_or_hit = input("1: stay\n2: hit\n")
    if stay_or_hit == '1':
        player_in = False
    else:
        deal_card(player_hand)
        print(f"You have {player_hand} for a total of {total(player_hand)}")
    if total(dealer_hand) > 16:
        dealer_in = False
    else:
        deal_card(dealer_hand)
    if total(player_hand) >= 21:
        break
    elif total(dealer_hand) >= 21:
        break
    if total(player_hand) == total(dealer_hand):
        print(f"The dealer's hand is {dealer_hand}, adding up to {total(dealer_hand)}. It's a draw!")
        game_start = False
        dealer_in = False
        player_in = False
        break
while len(dealer_hand) >= 2 and game_start is True:
    if total(dealer_hand) < 16:
        deal_card(dealer_hand)
    if total(dealer_hand) < 16:
        deal_card(dealer_hand)
    if total(dealer_hand) < 16:
        deal_card(dealer_hand)
    if total(player_hand) == 21 and len(player_hand) > 2:
        print(f"The dealer's hand is {dealer_hand}, adding up to {total(dealer_hand)}. You win!")
        break
    elif total(dealer_hand) == 21 and len(dealer_hand) > 2:
        print(f"The dealer's hand is {dealer_hand}, adding up to {total(dealer_hand)}. You lose.")
        break
    elif total(player_hand) > 21:
        print("You have busted! The dealer wins!")
        break
    elif total(dealer_hand) > 21:
        print(f"The dealer's hand is {dealer_hand}, adding up to {total(dealer_hand)}. The dealer has busted! You win!")
        break
    elif total(player_hand) > total(dealer_hand):
        print(f"The dealer's hand is {dealer_hand}, adding up to {total(dealer_hand)}. You win!")
        break
    elif total(player_hand) < total(dealer_hand):
        print(f"The dealer's hand is {dealer_hand}, adding up to {total(dealer_hand)}. You lose.")
        break
    if total(player_hand) == total(dealer_hand):
        print(f"The dealer's hand is {dealer_hand}, adding up to {total(dealer_hand)}. It's a draw!")
        game_start = False
        dealer_in = False
        player_in = False
        break
























