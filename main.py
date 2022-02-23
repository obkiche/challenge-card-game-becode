from utils.game import Board
from utils.player import Player

userInput = input("Please enter the names of the players:")

print (players)

bord = Board()
bord.players = userInput.split(' ')

bord.start_game()

