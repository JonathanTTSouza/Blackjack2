'''
Blackjack game in python. Simpler program
'''
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    '''Deals a random card from the cards list.'''
    return random.choice(cards)

def calculate_score(list_of_cards):
    '''Calculates the total value of a hand at a certain point in time'''
    score = sum(list_of_cards)

    if 11 in list_of_cards and score > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    
    if score == 21:
        return 0

    return sum(list_of_cards)

def compare(playerscore, computerscore):
    '''Compares the player's score and the computer's score and checks for game ending scenarios'''
    # Draw check
    if playerscore == computerscore and playerscore < 21 and computerscore < 21:
        game_on = False
        print("Push")
            
    # Player blackjack check (0 is defined as blackjack)        
    elif playerscore == 0:
        game_on = False
        print("Player blackjack")

    # Computer blackjack check (0 is defined as blackjack)
    elif computerscore == 0:
        game_on = False
        print("Computer blackjack")

    # Player busts check
    elif playerscore > 21:
        print("Player bust")

    # Computer busts check
    elif computerscore > 21:
        print("Computer bust")
    
    # Checks if player has the biggest score if no blackjacks or busts happened
    elif playerscore > computerscore:
        print("Player wins")

    # Checks if computer has the biggest score if no blackjacks or busts happened
    elif playerscore < computerscore:
        print("Computer wins")
    
def main_game():
    '''Runs the game logic'''

    # The player and computer hands start as empty
    player_cards = []
    computer_cards = []

    # Deal two cards to the player
    player_cards.append(deal_card())
    player_cards.append(deal_card())

    # Deal two cards to the dealer(computer)
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    # Calculates the score of both player and computer
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    # Prints the cards. Both for the player and only one for the computer
    print("Player cards: " + str(player_cards[0]) + ' + ' + str(player_cards[1]))
    print("Dealer cards: " + str(computer_cards[0]) + " + hidden")

    game_on = True
    while game_on:
        # Checks if player can still hit
        if player_score < 21 and player_score != 0:
            choice = input("Do you want to hit or stand?(h/s): ")
            if choice == 'h': # hit
                player_cards.append(deal_card())
                player_score = calculate_score(player_cards)
                print(player_score)
                
            elif choice == 's': # stand
                game_on = False

            else: 
                print("Invalid input, try again")
                continue
        else:
            break
    
    # Dealer hits until  at least 17
    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Displays the scores and checks game ending scenarios
    print("Player score: " + str(player_score))
    print("Computer score: " + str(computer_score))
    compare(player_score, computer_score)

    replay = input("Want to play again?(y/n): ")
    if replay == 'y':
        print('\n\n\n\n\n\n\n\n\n\n')
        main_game()
    else:
        print("Goodbye")

main_game()




