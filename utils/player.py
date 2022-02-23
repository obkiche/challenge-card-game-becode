from card import Card
import random

class Player:

    def __init__(self, name):
        self.turn_count = 0
        self.cards = [Card(0, 2, 3),Card(1, 0, 5), Card(0,3,11), Card(1,2,9)]
        self.name = name
        self.number_of_cards = len(self.cards)
        self.history = []

    def __str__(self):
        return self.cards


    def play(self):
        """"
        color = random.randint(0, 1)
        icon = random.randint(0,3)
        value = random.randint(0,13)
        print(color, icon, value)
        card = Card(color, icon, value)
        """
        card = random.choice(self.cards)
        card1 = f"{card}"
        print(self.cards)
        self.history.append(card1)
        print("----")
        self.turn_count += 1

        print(f"Player name: {self.name} {self.turn_count} played: {card1} ")

        return card1


        print('-----')


class Deck(Player):

    def __init__(self):
        self.cards = []


    def fill_deck(self):
        mycards = []
        for i in (range(13)):
            for j in range(4):
                if j == 0 or j == 1:
                    k = 0
                    card = Card(k, j, i)
                    print(f"your card {card}")
                    mycards.append(card)
                elif j == 2 or j == 3:
                    k = 1
                    card = Card(k, j, i)
                    mycards.append(card)

        return mycards

    def shuffle(self):
        shuffle(self.deck)

    def destribute(self, *names):

        players = []
        for name in names:
            players.append(name)


        mydeck = self.fill_deck()
        print("****",len(mydeck))
        number_of_cards = len(mydeck) // len(names)

        for player in players:
            for j in range(number_of_cards):
                print(j,number_of_cards)
                Player(player).cards = []
                print(Player(player).cards )
                self.cards = Player(player).cards.append(mydeck.pop())
                print(len(Player(player).cards))

            print(player, len(Player(player).cards))

            return Player(player).cards
