treasure = ''' 
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           |'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'||||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-|/.-'    o |'|||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
'''
print (treasure)
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
turn = input("You are at a crossroad! Left or Right? ")
if turn.capitalize() == "Left":
    choice = input("Make a choice! Swim or Wait? ")
    if choice.capitalize() == "Wait":
        door_color = input("Door Color? ")
        if door_color.capitalize() == "Red":
            print("Burned by fire.\nGame Over.")
        elif door_color.capitalize() == "Blue":
            print("Eaten by beats.\nGame Over.")
        elif door_color.capitalize() == "Yellow":
            print("You Win!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")
