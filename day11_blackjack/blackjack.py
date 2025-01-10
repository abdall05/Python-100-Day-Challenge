import random

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def get_first_hand():
    return list(random.choices(cards, k=2))


# used to hide the second card of the computer
def hide_hand(hand):
    hidden_card = hand[1]
    hand[1] = "?"
    return hidden_card


def reveal_hidden_card(hand, hidden_card):
    hand[1] = hidden_card


def hit(hand):
    hand.append(random.choice(cards))


def evaluate_hand(hand):
    sum_without_counting_aces = 0
    aces = 0
    for card in hand:
        if card.isnumeric():
            sum_without_counting_aces += int(card)
        elif card == 'A':
            aces += 1
        else:
            sum_without_counting_aces += 10
    if aces > 0:
        # count first aces as 11 and the other as 1
        total = sum_without_counting_aces + 11 + (aces - 1)
        if total <= 21:
            return total
        else:
            return sum_without_counting_aces + aces
    return sum_without_counting_aces


def is_bust(hand):
    hand_score = evaluate_hand(hand)
    return hand_score > 21


def player_moves(hand):
    while not is_bust(hand):
        choice = input("hit or stand: ").lower()
        if choice == 'hit':
            hit(hand)
            print(f"Your hand: {hand}, current score: {evaluate_hand(hand)}")
        else:
            return


def computer_moves(computer_hand, hidden_card):
    reveal_hidden_card(computer_hand, hidden_card)
    print(f"computer's hand: {computer_hand}, current score: {evaluate_hand(computer_hand)}")
    while evaluate_hand(computer_hand) <= 16:
        hit(computer_hand)
        print("computer hits.")
        print(f"computer's hand: {computer_hand}, current score: {evaluate_hand(computer_hand)}")
