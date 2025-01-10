import blackjack
from ascii_art import logo

print(logo)

finished = False

while not finished:
    player_hand = blackjack.get_first_hand()
    print(f"Your hand: {player_hand}, current score: {blackjack.evaluate_hand(player_hand)}")
    computer_hand = blackjack.get_first_hand()
    hidden_card = blackjack.hide_hand(computer_hand)
    print(f"computer's first hand: {computer_hand}")
    blackjack.player_moves(player_hand)
    player_score = blackjack.evaluate_hand(player_hand)
    if player_score > 21:
        print("You went over 21! You lose!")
    else:
        blackjack.computer_moves(computer_hand, hidden_card)
        computer_score = blackjack.evaluate_hand(computer_hand)
        if computer_score > 21:
            print("your opponent went over 21! You win!")
        elif player_score == computer_score:
            print(f"You got the same score: {player_score}. Draw!")
        elif player_score > computer_score:
            print(f"your score is higher. You win!")
        else:
            print(f"Your score ({player_score}) is lower than than your opponent's ({computer_score}). You lose!")
    choice = input("Play again y/n? ").lower()
    if choice == 'n':
        finished = True
