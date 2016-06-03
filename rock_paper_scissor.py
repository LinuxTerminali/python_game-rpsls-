import random

def name_to_number(name):
    if name=="rock":
        return 0
    elif name=="spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "wrong choice"

    
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number ==1:
        return "spock"
    elif number ==2:
        return "paper"
    elif number ==3:
        return "lizard"
    elif number ==4:
        return "scissors"
    else:
        return "wrong choice"

    
def rpsls(player_choice):
    player_number = name_to_number(player_choice)
    print "player choice is ",player_choice 
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "computer choose", comp_choice
    #print type(player_number),type(comp_number)
    subtract= player_number-comp_number
    #print subtract
    winner= subtract%5
    #print winner
    if winner == 1 or winner ==2 :
        print "player wins!"
    elif winner ==3  or winner== 4:
        print "computer wins!"
    else:
        print "Oh its a tie!"
    return 0

rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
