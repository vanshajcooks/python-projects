import random

#Making a Roll Function

def roll():
    min_value = 1
    max_value = 6
    number = random.randint(min_value,max_value)

    return number


#Choosing number of players

while True: #checks if input is actually a number
    players = input("How many players (1-4 max)? ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break 
        else:
            print("Must be bw 2-4 players. ")

    else: 
        print("Invalid, Try again.")

max_score= 50 # defining a max score variable to check later

player_scores = [0 for i in range(players)] #just creating a list for players scores based on no of players input

print("Your initial scores are ",player_scores)

print("\nIts time to begin the game, I guess\n")

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("Player ", player_idx + 1," has started!\n")
        print("Your total score is ", player_scores[player_idx],"\n")
        

        while True:
            current_score = 0
            should_roll = input("Would you like to roll? (y) \n")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn OVER!!!!\n")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a : ",value)
                print("\n Your score is ", current_score)

            player_scores[player_idx] += current_score
            print("Your total score is : ", player_scores[player_idx])
            

max_score = max(player_scores)

winningidx =  player_scores.index(max_score)
print("Player ",winningidx+1, "wins!")



