### RPSLS
import random

def name_to_number(name):
    if name == "rock":
        name = 0
    elif name == "Spock":
        name = 1
    elif name == "paper":
        name = 2
    elif name == "lizard":
        name = 3
    elif name == "scissors":
        name = 4
    else:
        return False
        
    return name


def number_to_name(number):
    
    if number == 0:
        number = "rock"
    elif number == 1:
        number = "Spock"
    elif number == 2:
        number = "paper"
    elif number == 3:
        number = "lizard"
    elif number == 4:
        number = "scissors"
    else:
        return False
    
    return number


def rpsls(player_choice):
    global one_more
    one_more = "y"
    if player_choice <0 or player_choice >4:
        print ("Pick a number between 0 and 4!")
        start_game()
    else:
        while one_more == "y":
            player_choice_name = number_to_name(player_choice)
            print ("\n-------------")
            print ("The player chooses %s" %(player_choice_name))
            random_no = random.randrange(4)
            comp_choice = number_to_name(random_no)
            
            print ("The computer chooses %s" % (comp_choice))

            if random_no < int(player_choice):
                result = (random_no - int(player_choice))%5
            else:
                result = (int(player_choice) - random_no)%5

            if result == 1 or result == 2:
                if random_no < player_choice:
                    print ("      Computer wins!")
                else:
                    print ("      Player wins!")
                    
            elif result == 3 or result == 4:
                if random_no < player_choice:
                    print ("      Player wins!")
                else:
                    print ("      Computer wins!")

            else:
                print ("      It's a tie!")

            print ("\nOne more? y/n ")
            one_more_game = input()
            if one_more_game == "y":
                print ("\n-----------NEW GAME-------------")
                start_game()
            else:
                break
        

def start_game():
    print ("Rules of the game. You pick one of the numbers corresponding to the text:\n 0 -> rock\n 1 -> Spock\n 2 -> paper\n 3 -> lizard\n 4 -> scissors")
    print ("\n-----------------WIN RULES-----------------\nScissors cuts paper\nPaper covers rock\nRock crushes lizard\nLizard poisons Spock\nSpock smashes scissors\nScissors decapitates lizard\nLizard eats paper\nPaper disproves Spock\nSpock vaporizes rock\nAnd as it always has been\nRock crushes scissors")
    print ("\nNow please select number 0-4")
    choice = int(input())
    rpsls(choice)

start_game()
