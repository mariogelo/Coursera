### RPSLS
import random
one_more = "y"

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
###            smaller_no = comp_choice
 ###           bigger_no = player_choice
            print ("Computer wins!")
            
        else:
 ###           smaller_no = player_choice
 ###           bigger_no = comp_choice
            print ("Player wins!")
            
    elif result == 3 or result == 4:
        if random_no < player_choice:
 ###           smaller_no = comp_choice
 ###           bigger_no = player_choice
            print ("Player wins!")
        else:
 ###           smaller_no = player_choice
 ###           bigger_no = comp_choice
            print ("Computer wins!")

    else:
        print ("It's a tie!")

while one_more == "y":
    print ("One more? - y/n -")
    one_more = input()
    if one_more == "y":
        start_game()
    else:
        break
        

def start_game():
    print ("Please select number 0-4")
    choice = int(input())
    rpsls(choice)

start_game()
