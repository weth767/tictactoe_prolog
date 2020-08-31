/*
    jogadas possíveis para x
*/

:- dynamic jogada/3.

jogada(n, 0, 0).
jogada(n, 0, 1).
jogada(n, 0, 2).
jogada(n, 1, 0).
jogada(n, 1, 1).
jogada(n, 1, 2).
jogada(n, 2, 0).
jogada(n, 2, 1).
jogada(n, 2, 2).

zera_tabuleiro :-   retract(jogada(_, 0, 0)), assert(jogada(n, 0, 0)),
                    retract(jogada(_, 0, 1)), assert(jogada(n, 0, 1)),
                    retract(jogada(_, 0, 2)), assert(jogada(n, 0, 2)),
                    retract(jogada(_, 1, 0)), assert(jogada(n, 1, 0)),
                    retract(jogada(_, 1, 1)), assert(jogada(n, 1, 1)),
                    retract(jogada(_, 1, 2)), assert(jogada(n, 1, 2)),
                    retract(jogada(_, 2, 0)), assert(jogada(n, 2, 0)),
                    retract(jogada(_, 2, 1)), assert(jogada(n, 2, 1)),
                    retract(jogada(_, 2, 2)), assert(jogada(n, 2, 2)).

/*verifica possições onde pode dar velha*/
verifica_ganhou(V) :- 
    ((jogada(V, 0, 0),
     jogada(V, 1, 0),
     jogada(V, 2, 0)
    );
    (jogada(V, 0, 0),
     jogada(V, 0, 1),
     jogada(V, 0, 2)
    );
    (jogada(V, 0, 0),
     jogada(V, 1, 1),
     jogada(V, 2, 2)
    );
    (jogada(V, 0, 2),
     jogada(V, 1, 1),
     jogada(V, 2, 0)
    );
    (jogada(V, 0, 1),
     jogada(V, 1, 1),
     jogada(V, 2, 1)
    );
    (jogada(V, 0, 2),
     jogada(V, 1, 2),
     jogada(V, 2, 2)
    );
    (jogada(V, 1, 0),
     jogada(V, 1, 1),
     jogada(V, 1, 2)
    );
    (jogada(V, 2, 0),
     jogada(V, 2, 1),
     jogada(V, 2, 2)
    )); false.

verifica_tabuleiro :- jogada(n, _, _).
verifica_x_ganhou(X) :- verifica_ganhou(x), X = 1; X = 0.
verifica_o_ganhou(O) :- verifica_ganhou(o), O = 2; O = 0.
verifica_empate(E) :- \+verifica_tabuleiro, verifica_x_ganhou(X), X = 0, verifica_o_ganhou(O), O = 0, E = 3;
                      E = 0.

/*Mostra o jogo*/

mostra_jogo :- jogada(A,0,0), write(A), write(' | '),
               jogada(B,0,1), write(B), write(' | '),
               jogada(C,0,2), write(C), nl,
               jogada(D,1,0), write(D), write(' | '),
               jogada(E,1,1), write(E), write(' | '),
               jogada(F,1,2), write(F), nl,
               jogada(G,2,0), write(G), write(' | '),
               jogada(H,2,1), write(H), write(' | '),
               jogada(I,2,2), write(I), nl.

jogodavelha(V,P1,P2,X,O,E,R) :- R = 1, zera_tabuleiro ; ((jogada(x,P1,P2) ; jogada(o,P1,P2)), false, nl);
                        assert(jogada(V, P1, P2)), retract(jogada(n, P1, P2)),
                        verifica_x_ganhou(X); verifica_o_ganhou(O);
                        verifica_empate(E).