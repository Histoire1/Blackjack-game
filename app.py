import random
player_in = True
dealer_in = True

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


# revealing hands and determine whether to hit or stand


def reveal_dealer_hand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]


while player_in or dealer_in:
    print(f"Dealer has {reveal_dealer_hand()} and ....")
    print(f"You have {player_hand} for a total of {total(player_hand)}")
    if player_in:
        stay_or_hit = input("1: stay\n2: hit\n")
    if stay_or_hit == '1':
        player_in = False
    else:
        deal_card(player_hand)
    if total(dealer_hand) > 16:
        dealer_in = False
    else:
        deal_card(dealer_hand)
    if total(player_hand) >= 21:
        break
    elif total(dealer_hand) >= 21:
        break
if total(player_hand) == 21:
    print("Blackjack! Congratulations, you win!")
elif total(dealer_hand) == 21:
    print("Blackjack! The dealer wins!")
elif total(player_hand) > 21:
    print(f"You have a total of {total(player_hand)}.")
    print("You have busted! The dealer wins!")
elif total(dealer_hand) > 21:
    print("The dealer has busted! You win!")
elif total(player_hand) > total(dealer_hand):
    print(f"Your hand is {player_hand},adding up to {total(player_hand)}. The dealer's hand is {dealer_hand},"
          f"adding up to {total(dealer_hand)}. You win!")
elif total(player_hand) < total(dealer_hand):
    print(f"Your hand is {player_hand},adding up to {total(player_hand)}. The dealer's hand is {dealer_hand},"
          f" adding up to {total(dealer_hand)}. You lose.")




















