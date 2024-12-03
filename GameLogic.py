import Deck
import Card
import os
import time

#Function to check if user is busted, if busted return -1
def checkHand(hand):

    #Keep track of aces
    ace_counter = 0

    totalScore = 0
    for card in hand:
        if card.rank == "Ace":
            ace_counter += 1
        totalScore += card.value

    #Deal with Aces and adjust score accordingly
    while totalScore >= 21:

        #If player has aces
        if ace_counter > 0:
            totalScore = totalScore - 10
            ace_counter -= 1
        else:
            break

    #Return score
    if (totalScore >= 21):
        return -1
    else:
        return totalScore


#Function to display a card 
def displayOneCard(card):
    print("\n")
    print(f"        ----------------------")
    print(f"         {card}       ")
    print(f"        ----------------------")


#Function to display 2 cards 
def displayTwoCards(card1, card2):
    print("\n")
    print(f"        ----------------------     ---------------------- ")
    print(f"         {card1}                 {card2}     ")
    print(f"        ----------------------     ---------------------- ")
    
    
print(chr(27) + "[2J")
print("\n******************************************************************************************")
print("* Welcome to BlackJack, you have 100$, Let's see if you can beat the House! Good Luck :) *")
print("******************************************************************************************")
#Game Loop (Loop until player's money is gone or player choose to quit game)
game_on = True
playerMoney = 100
winner = "House"


while (game_on == True):

    #Check if enough money to play
    if playerMoney <= 0:
        print("Not enough funds to play ;(")
        break

    #Asking player how much to bet
    bet_choice = int(input("\nHow much would you like to bet? "))
    while(bet_choice > playerMoney):
        print(f"Not enough funds, you have only got {playerMoney}$ left!")
        bet_choice = int(input("How much would you like to bet? "))

    #Retrieving 4 cards two for house and 2 for player
    gameDeck = Deck.Deck()
    house1 = gameDeck.dealOneCard()
    house2 = gameDeck.dealOneCard()
    player1 = gameDeck.dealOneCard()
    player2 = gameDeck.dealOneCard()

    playerHand = []
    playerHand.append(player1)
    playerHand.append(player2)

    houseHand = []
    houseHand.append(house1)
    houseHand.append(house2)

    #Displaying the cards to the user 
    print("\n")
    print("The House's cards")
    print(f"        ----------------------     ---------------------- ")
    print(f"         {house1}                       ?      ")
    print(f"        ----------------------     ---------------------- ")
    
    print("\n")
    print("The player's cards")
    print(f"        ----------------------     ---------------------- ")
    print(f"         {player1}                 {player2}     ")
    print(f"        ----------------------     ---------------------- ")
    

    #Asking the user for their input to play
    print("\n")
    total = checkHand(playerHand)
    print("Total: ", total)
    print("\n")
    user_input = input("What would you like to do? 1- Hit  2- Pass  ")
    while(user_input not in ["1", "2"]):
        user_input = input("Invalid input! Please enter one of the two options: 1- Hit 2- Pass ")

    #If User wants to hit
    while(user_input == "1"):

        #Display House cards
        print(chr(27) + "[2J")
        print("\n")
        print("The House's cards")
        print(f"        ----------------------     ---------------------- ")
        print(f"         {house1}                       ?      ")
        print(f"        ----------------------     ---------------------- ")


        extraCard = gameDeck.dealOneCard()
        playerHand.append(extraCard)
        print(f"\nYour current Hand: ")
       
        for c in range(0,len(playerHand),2):
            if (len(playerHand)-c) >= 2:
                displayTwoCards(playerHand[c], playerHand[c+1])
            else:
                displayOneCard(playerHand[c])

        #Check hand total count
        total = checkHand(playerHand)
        if total < 0:
            print("BUSTED! House wins")
            break
        else:
            print("Total: ", total)


        user_input = input("Hit Again? ")
        print("--------------------------------------------------------------------------")


    #Reveal House cards
    print(chr(27) + "[2J")
    print("--------------------------------------------------------------------------")
    print("\nYour Cards:")
    for c in range(0,len(playerHand),2):
        if (len(playerHand)-c) >= 2:
            displayTwoCards(playerHand[c], playerHand[c+1])
        else:
            displayOneCard(playerHand[c])
    totalPlayer = checkHand(playerHand)
    print("Total: ", totalPlayer)

    print("The House's cards:")
    displayTwoCards(house1, house2)
    totalHouse = checkHand(houseHand)
    print("Total: ", totalHouse)
    print("--------------------------------------------------------------------------")

    #House to draw more cards if player is winning
    while(totalPlayer >= totalHouse):
        extraHouseCard = gameDeck.dealOneCard()
        houseHand.append(extraHouseCard)
        print("\nHouse is drawing another card...")
        time.sleep(4)

        #Show House cards
        print(f"The House's Hand: ")
       
        for c in range(0,len(houseHand),2):
            if (len(houseHand)-c) >= 2:
                displayTwoCards(houseHand[c], houseHand[c+1])
            else:
                displayOneCard(houseHand[c])
        #Check House hand total count
        totalHouse = checkHand(houseHand)
        print("Total: ", totalHouse)

        #Show player cards
        print("\nYour Cards:")
        for c in range(0,len(playerHand),2):
            if (len(playerHand)-c) >= 2:
                displayTwoCards(playerHand[c], playerHand[c+1])
            else:
                displayOneCard(playerHand[c])
        totalPlayer = checkHand(playerHand)
        print("Total: ", totalPlayer)

        if totalHouse < 0:
            winner = "Player"
            break
        elif totalHouse > totalPlayer:
            winner = "House"
            break
    

    #Check winner
    if totalHouse < 0:
        winner = "Player"
    elif totalHouse < 0:
        winner = "House"
    elif totalPlayer > totalHouse:
        winner = "Player"
    else: 
        winner = "House"

    #Announce winner
    if winner == "House":
        print("\nThe House won this round, tough luck :/")
        playerMoney -= bet_choice
    else:
        print("\nCongrats! You won this round!")
        playerMoney += bet_choice

    #See if player wants to continue
    print(f"You currently have {playerMoney}$ ")
    user_choice = input("Would you like to continue playing? (y or n) ")
    while user_choice not in ["y", "n"]:
        user_choice = input("Wrong input, please enter y orn!")
    if(user_choice == "y"):
        game_on = True
    else:
        game_on = False

    print(chr(27) + "[2J")


print(f"\n******************************************************************************************")
print(f"* Game Over! You ended up with {playerMoney}$ Thanks for playing! Goodbye                *")
print(f"******************************************************************************************")
       


