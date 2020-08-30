import sys
from pyswip import Prolog, Functor, Variable, Query, Atom

class TicTacToe:
    plays = []
    prolog = Prolog()
    prolog.consult('tictactoe.pl')

    def pl(self, player, positionX, positionY):
        play = self.prolog.query('jogodavelha(' + player + ',' + str(positionX) + ',' + str(positionY) + ')')
        self.plays.append(play)
        for i in play:
            print(i)

    def __init__(self):
        super().__init__()




