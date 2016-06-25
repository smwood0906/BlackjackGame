import random

class Cards():
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

    def __repr__(self):
        return "{f} of {s}".format(f= self.face, s= self.suit)

class Deck():
    def __init__(self):
        self.deck = self.whole_deck()
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def whole_deck(self):
        deck = []
        suit = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        face = ['Ace', '2', '3', '4', '5' , '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        for group in suit:
            x = 0
            for each in face:
                card = Cards(group, each, value[x])
                deck.append(card)
                x += 1
        return deck

class Player():
    def __init__(self, name):
        self.name = name
        self.hand_value = 0
        self.cards = []
        self.turn = False

    def display_hand(self):
        pass

    def calc_score(self):
        for card in self.cards:
            self.hand_value += card.value


class GamePlay():
    print('Let\'s play some Blackjack!')
    def __init__(self):
        self.deck = Deck()
        self.dealer = Player('Dealer')
        self.player_lst = []
        self.create_list()

    def create_list(self):
       num = int(input('How many players are there?: '))
        for pl in range(1, num +1):
            player = Player(input('Player {}, what is your name? '.format(pl)))
            self.player_lst.append(player)


    def deal(self):
        self.dealer.cards.append(self.deck.pop())
        self.dealer.cards.append(self.deck.pop())
        card1 = self.deck.pop()
        card2 = self.deck.pop()
        for player in self.player_lst:
            player.cards.append(card1)
            player.cards.append(card2)


    for player in self.player_lst
    if self.hand_value == 21:
        print( 'Congratulations! You\'ve won this hand!')

    elif self.hand_value > 21:
        print('Sorry, you bust!')

    elif self.hand_value < 21:
        choice = input('Would you like to Hit or Stay?: ')

        if choice.capitalize() == 'Hit':
            hit_card = self.deck.pop()

            print(self.hand_value)

        elif choice.capitalize == 'Stay':
        # move to next player's turn
    else:
        print('I\'m sorry, I didn\'t understand that.')






