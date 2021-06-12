'''
Blackjack game in python. Simpler attempt
'''
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(list_of_cards):
    score = sum(list_of_cards)

    if 11 in list_of_cards and score > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    
    if score == 21:
        return 0

    return sum(list_of_cards)

def compare(playerscore, computerscore):
    if playerscore == computerscore and playerscore < 21 and computerscore < 21:
        game_on = False
        print("Push")
            
    elif playerscore == 0:
        game_on = False
        print("Player blackjack")
        
    elif computerscore == 0:
        game_on = False
        print("Computer blackjack")

    elif playerscore > 21:
        print("Player bust")

    elif computerscore > 21:
        print("Computer bust")
    
    elif playerscore > computerscore:
        print("Player wins")

    elif playerscore < computerscore:
        print("Computer wins")
    
def main_game():
    player_cards = []
    computer_cards = []

    player_cards.append(deal_card())
    player_cards.append(deal_card())

    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print("Player cards: " + str(player_cards[0]) + ' + ' + str(player_cards[1]))
    print("Dealer cards: " + str(computer_cards[0]) + " + hidden")

    game_on = True
    while game_on:
        if player_score < 21 and player_score != 0:
            choice = input("Do you want to hit or stand?(h/s): ")
            if choice == 'h':
                player_cards.append(deal_card())
                player_score = calculate_score(player_cards)
                print(player_score)
                
            elif choice == 's':
                game_on = False

            else:
                print("Invalid input, try again")
                continue
        else:
            break
    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

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




