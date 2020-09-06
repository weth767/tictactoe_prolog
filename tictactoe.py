# desenvolvido por João Paulo de Souza e Leandro Souza Pinheiro

import sys
from pyswip import Prolog

class TicTacToe:
    prolog = Prolog()
    prolog.consult('tictactoe.pl')
    
    # método para executar a jogoda no prolog
    def pl(self, player, positionX, positionY, reset=0):
        # passa a query e seta os parametros, pegando alguns de retorno
        play = self.prolog.query('jogodavelha(' + player + ',' + str(positionX) + ',' + str(positionY) + ', X, O, E,' + str(reset) + ')')
        # transforma em lista
        values = list(play)
        # caso não seja reset
        if reset != 1:
            # pega todos os valores e verifica o que veio de resposta
            # para cada variavel de resposta
            for i in values:
                if isinstance(i['X'], int):
                    if i['X'] == 1:
                        return 'O jogador do "x" ganhou'
                if isinstance(i['O'], int):
                    if i['O'] == 2:
                        return 'O jogador do "o" ganhou'
                if isinstance(i['E'], int):
                    if i['E'] == 3:
                        return 'O jogo empatou "deu velha"'
        else:
            return None
            

    def __init__(self):
        super().__init__()




