import random


class Cards():
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

    def __repr__(self):
        return "{f} of {s}".format(f=self.face, s=self.suit)


class Deck():
    def __init__(self, number_of_decks=6):
        self.deck = self.whole_deck()
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def whole_deck(self):
        deck = []
        suit = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        face = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
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
        self.in_hand = True

    def calc_score(self):
        self.hand_value = 0
        for card in self.cards:
            self.hand_value += card.value

    def clear_turn(self):
        self.hand_value = 0
        self.cards = []
        self.turn = False
        self.dealer_check = True

class GamePlay():
    print('Let\'s play some Blackjack!')

    def __init__(self):
        self.deck = Deck()
        self.dealer = Player('Dealer')
        self.player_lst = []
        self.create_list()

    def create_list(self):
        num = int(input('How many players are there?: '))
        for pl in range(1, num + 1):
            player = Player(input('Player {}, what is your name? '.format(pl)))
            self.player_lst.append(player)
        self.play_game()

    def deal(self):
        self.dealer.cards.append(self.deck.deck.pop())
        self.dealer.cards.append(self.deck.deck.pop())
        card1 = self.deck.deck.pop()
        card2 = self.deck.deck.pop()
        for player in self.player_lst:
            player.cards.append(card1)
            player.cards.append(card2)

    def play_game(self):
        self.deal()
        for player in self.player_lst:
            player.turn = True
            print("{} it\'s your turn!".format(player.name))
            print("Dealer is showing " + str(self.dealer.cards[0]) + ".")
            while player.turn:
                print("Your hand is " + ", ".join([str(x) for x in player.cards])) #list comprehension
                player.calc_score()
                print("Your hand value is " + str(player.hand_value))

                if player.hand_value == 21:
                    player.turn = False
                    print('Congratulations! You\'ve won this hand!')
                    player.in_hand = False

                elif player.hand_value > 21:
                    player.turn = False
                    print('Sorry, you bust!')
                    player.in_hand = False

                elif player.hand_value < 21:
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

    def dealer_turn(self):
         self.dealer.turn = True
         self.dealer.calc_score()
         print("Dealer is showing " + ", ".join([str(x) for x in self.dealer.cards]))
         print("Dealer hand value is " + str(self.dealer.hand_value))
         while self.dealer.turn:
                self.dealer.calc_score()
                if self.dealer.hand_value > 21:
                    print("Dealer busts!")
                    self.dealer.turn = False
                elif self.dealer.hand_value >= 17:
                    self.dealer.calc_score()
                    print(self.dealer.hand_value)
                    self.dealer.turn = False
                elif self.dealer.hand_value <= 16:
                    print( "Dealer hits.")
                    hit_card = self.deck.deck.pop()
                    self.dealer.cards.append(hit_card)
                    self.dealer.calc_score()
                    print(self.dealer.hand_value)

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
                    print('Sorry {p}, your hand value is {n}, you lose this hand.'.format(p=player.name, n=player.hand_value)


game = GamePlay()
