from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def find_highest_bidder(bids):
    winner = ""
    max_bid = 0
    for person in bids:
        if bids[person] > max_bid:
            max_bid = bids[person]
            winner = person
    print(f"The Winner is {winner} with a bid of ${max_bid}")
