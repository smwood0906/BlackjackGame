
class Player():
    def __init__(self, name):
        self.name = name
        self.hand_value = 0
        self.cards = []
        self.turn = False

    def __repr__(self):
        return self.name

    def display_hand(self):
        pass


    def calc_score(self):
        for card in self.cards:
            self.hand_value += card.value


def create_list():
    player_lst = []
    num = int(input('How many players are there?: '))
    for pl in range(1, num + 1):
        player = Player(input('Player {}, what is your name? '.format(pl)))
        player_lst.append(player)
    print(player_lst)
create_list()

