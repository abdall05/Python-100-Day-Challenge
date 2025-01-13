import random
from game_data import data
from ascii_art import logo, vs
from utils import clear

chosen_pairs = set()

data_size = len(data)
middle = data_size // 2
number_of_pairs = data_size * (data_size - 1) / 2


def clear_and_print_logo():
    clear()
    print(logo)


def entity_definition(entity):
    return f"{entity['name']}, a {entity['description']}, from {entity['country']} "


def get_two_random_entities(entity_list, picked_pairs):
    if len(picked_pairs) == number_of_pairs:
        return None
    while True:
        index1 = random.randint(0, middle - 1)
        index2 = random.randint(middle, data_size - 1)
        pair = (index1, index2)
        if pair not in picked_pairs:
            picked_pairs.add(pair)
            pair_list = list(pair)
            random.shuffle(pair_list)
            return entity_list[pair_list[0]], entity_list[pair_list[1]]


def make_a_choice():
    choice = ''
    while choice not in ['a', 'b']:
        choice = input("Who has more follower? Type 'A' or 'B': ").lower()
    return choice


def evaluate_choice(entity1, entity2, choice):
    count1 = entity1['follower_count']
    count2 = entity2['follower_count']
    if choice == 'a' and count1 >= count2:
        return True
    elif choice == 'b' and count1 <= count2:
        return True
    return False


def game():
    print(logo)
    score = 0
    finished = False
    while not finished:
        entities = get_two_random_entities(data, chosen_pairs)
        if entities is None:
            print(f"You have reached the end of the game, you have a score of {score}!")
            finished = True
            continue
        entity1, entity2 = entities
        print(f"Compare A: {entity_definition(entity1)}")
        print(vs)
        print(f"Compare B: {entity_definition(entity2)}")

        player_choice = make_a_choice()
        success = evaluate_choice(entity1, entity2, player_choice)
        clear_and_print_logo()
        if success:
            score += 1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            finished = True
