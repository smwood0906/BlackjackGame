#This is my first major project using Classes in Python. Completed during Week 4 of Bootcamp.

import random

# Class that creates Card objects and returns printable representations.
class Cards():
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

    def __repr__(self):
        return "{f} of {s}".format(f=self.face, s=self.suit)

#Instantiate Deck object for gameplay by running the whole_deck method. Takes a number of decks arg to allow for multiple
#decks.
class Deck():
    def __init__(self, number_of_decks=6):
        self.deck = self.whole_deck()
        self.shuffle_deck()

# Method to shuffle all cards in the created Deck to a random order
    def shuffle_deck(self):
        random.shuffle(self.deck)

# Method that iterates through suit and face list and appends a Card object with suit, face & value to an empty deck list

    def whole_deck(self):
        deck = []
        suit = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        face = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        for s in suit:
            x = 0
            for f in face:
                card = Cards(s, f, value[x])
                deck.append(card)
                x += 1
        return deck

# Instantiates a Player object that holds name, total value current hand, list of each Card held, whether or not it is the Player's
# turn, and whether or not the Player has won or busted.
class Player():
    def __init__(self, name):
        self.name = name
        self.hand_value = 0
        self.cards = []
        self.turn = False
        self.in_hand = True

#Method to calculate Player's current score. Iterates through Player's hand, checks for aces and holds aces in a variable.
    def calc_score(self):
        self.hand_value = 0
        aces = 0                            #Need to create a variable to hold aces to determine value (1 or 11) later
        for card in self.cards:
            if card.face == 'Ace':
                aces += 1
                if aces > 1:                #If the Player's hand has more than one Ace, the value is set to 1 and added to the total hand value.
                    self.hand_value += 1
            else:
                self.hand_value += card.value
        if aces > 0:
            if self.hand_value + 11 < 22:   #If there is one Ace,the hand value + 11 is checked for bust.
                self.hand_value += 11       #If total hand value does not bust, value is set to 11 and added to hand value.
            else:
                self.hand_value += 1        #If hand value busts, value is set to 1 and added to total hand value


# Helper method to clear Player's turn
    def clear_turn(self):
        self.hand_value = 0
        self.cards = []
        self.turn = False
        self.dealer_check = True

# User interaction
class GamePlay():
    print('Let\'s play some Blackjack!')

    def __init__(self):
        self.deck = Deck()
        self.dealer = Player('Dealer')
        self.player_lst = []
        self.create_list()
# Method to add players by taking input and adding to a player list
    def create_list(self):
        num = int(input('How many players are there?: '))
        for pl in range(1, num + 1):
            player = Player(input('Player {}, what is your name? '.format(pl)))
            self.player_lst.append(player)
        self.play_game()
# Method to take two random cards out of the GamePlay Deck and add to each Player's hand, including Dealer
    def deal(self):
        self.dealer.cards.append(self.deck.deck.pop())
        self.dealer.cards.append(self.deck.deck.pop())
        for player in self.player_lst:
            card1 = self.deck.deck.pop()
            card2 = self.deck.deck.pop()
            player.cards.append(card1)
            player.cards.append(card2)
#Method that clears turn and runs deal method for each Player. When it is Player's turn, one of the Dealer's
#cards is shown, the player's hand value is calculated and checked for Win or Bust. If neither, Player is asked to Hit
# or stay. After all Player's have gone, dealer turn method and final score (to check win against dealer) method is run.
    def play_game(self):
        for player in self.player_lst:
            player.clear_turn()
        self.deal()
        for player in self.player_lst:
            player.turn = True
            print("{} it\'s your turn!".format(player.name))
            print("Dealer is showing " + str(self.dealer.cards[0]) + ".")
            while player.turn:
                print("Your hand is " + ", ".join([str(x) for x in player.cards]))  # list comprehension
                player.calc_score()
                print("Your hand value is " + str(player.hand_value))

                if player.hand_value == 21:
                    player.turn = False
                    print('Congratulations! You\'ve won this hand!')
                    player.in_hand = False
                    continue

                elif player.hand_value > 21:
                    player.turn = False
                    print('Sorry, you bust!')
                    player.in_hand = False    #Stored so Player will not be checked in final_score method
                    continue

                choice = input('Would you like to Hit or Stay?: ')

                if choice.capitalize() == 'Hit':
                    hit_card = self.deck.deck.pop()
                    player.cards.append(hit_card)

                elif choice.capitalize() == 'Stay':
                    player.turn = False
                    player.in_hand = True

                else:
                    print('I\'m sorry, I didn\'t understand that.')
        self.dealer_turn()
        self.final_score()
#Method to execute Dealer's turn according to Vegas rules. Dealer must Hit if hand value is <= 16 and must Stay if
# hand value >= 17.
    def dealer_turn(self):
        self.dealer.turn = True
        self.dealer.calc_score()
        print("Dealer is showing " + ", ".join([str(x) for x in self.dealer.cards]))
        print("Dealer hand value is " + str(self.dealer.hand_value))
        while self.dealer.turn:
            self.dealer.calc_score()
            print(self.dealer.hand_value)
            if self.dealer.hand_value > 21:
                print("Dealer busts!")
                self.dealer.turn = False
            elif self.dealer.hand_value >= 17:
                self.dealer.turn = False
            elif self.dealer.hand_value <= 16:
                print("Dealer hits.")
                hit_card = self.deck.deck.pop()
                self.dealer.cards.append(hit_card)
#Method to check each Player's final hand value against Dealer's hand value for a win. Only checks Players still in the game,
# if they haven't Won or Busted.
    def final_score(self):
        for player in self.player_lst:
            if player.in_hand == True:
                print(str(self.dealer.hand_value))
                if self.dealer.hand_value > 21:
                    print(' Dealer busts! {} you win this hand!'.format(player.name))
                elif self.dealer.hand_value == player.hand_value:
                    print('{p} your hand value is {n}, you push.'.format(p=player.name, n=player.hand_value))
                elif self.dealer.hand_value < player.hand_value:
                    print('{p} your hand value is {n}, you win!'.format(p=player.name, n=player.hand_value))
                else:
                    print('Sorry {p}, your hand value is {n}, you lose this hand.'.format(p=player.name,
                                                                                          n=player.hand_value))


game = GamePlay()
