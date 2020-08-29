import sys
from pyswip import Prolog, Functor, Variable, Query, Atom
from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

prolog = Prolog()
prolog.consult('tictactoe.pl')

jogadas = []

jogadas.append(prolog.query('jogodavelha(o,1,1)'))
jogadas.append(prolog.query('jogodavelha(x,1,0)'))
jogadas.append(prolog.query('jogodavelha(o,0,0)'))
jogadas.append(prolog.query('jogodavelha(x,0,2)'))
jogadas.append(prolog.query('jogodavelha(o,2,2)'))

for i in jogadas:
    for j in i:
        print(j)
    print('')
