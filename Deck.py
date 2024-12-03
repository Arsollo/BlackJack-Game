suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

import Card 
import random

class Deck:

    def __init__(self):
        self.numOfCards = 52
        self.cards = []

        #Build & shuffle Deck
        self.buildDeck()
        

    def showCards(self):
        for card in self.cards:
            print(card)

    def dealOneCard(self):
        cardToGive = self.cards.pop()
        self.numOfCards -= 1
        return self.cards.pop()
    
    def buildDeck(self):
        for s in suits:
            for r in ranks:
                newCard = Card.Card(s,r)
                self.cards.append(newCard)
        
        #Shuffle Deck
        random.shuffle(self.cards)

    
    def resetDeck(self):
        self.cards = []
        self.buildDeck()

