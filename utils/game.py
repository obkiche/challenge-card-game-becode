from player import Player, Deck

class Board:

    def __init__(self):
        self.players = []
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    def start_game(self):

        print("*****", self.players)

        print("The game starts")

        mydeck = Deck()
        h = mydeck.fill_deck()
        p= mydeck.destribute(self.players)


        nb_cards = len(h)/len(self.players)
        while nb_cards != 0:
              print(len(self.players))
              for i, player in enumerate(self.players):
                  if i < len(self.players):
                      pi = (Player(player))
                      pi.play()

                      Player(player).cards.pop()

                      Player(player).play()
                      player = self.players[i+1]
                      self.turn_count += 1
                      nb_cards -=1
                      self.active_cards.append(self.active_cards)
                      print("+++++++")
                      print (self.turn_count, self.active_cards, len(self.history_cards))
                  else:
                       break





userInput = input("Please enter the names of the players:")

bord = Board()
bord.players = userInput.split(' ')

bord.start_game()







