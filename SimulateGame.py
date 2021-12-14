from Cells import Cell, Property, Tax, Community, Chance, GoToJail
import Player
import Board
from settings import *

def game_over(players):
    """Check if there are more then 1 player left in the game"""
    alive = 0
    for player in players:
        if not player.bankrupt:
            alive += 1
    if alive > 1:
        return False
    else:
        return True


def game():
    players = []
    names = ["pl "+str(i) for i in range(N_PLAYERS)]
    for i in range(N_PLAYERS):
        players.append(Player.Player(names[i], STARTING_MONEY))
    
    game_board = Board.Board(players)
    
    for i in range(N_MOVES):
        #input("Press enter to continue") allows you to go move by move
        for player in players:
            if player.money > 0:
                print(f"{player.name} has £{player.money} and is at {player.pos}")
        
        for player in players:
            if not game_over(players):
                while player.turn(game_board):
                    pass
        
    results = [players[i].money for i in range(N_PLAYERS)]
    print(results)


game()
    
