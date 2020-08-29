/*3) Faça um código em PROLOG que tem uma base de conhecimentos representando o
estado atual de um tabuleiro do jogo da velha e diga se há vencedor (cruz
ou bola).*/

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

/*verifica possições onde pode dar velha*/
verifica_deu_velha(V) :- 
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
    )), write('Jogador do '), write(V), write(' Ganhou').

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

jogodavelha(V,P1,P2) :- ((jogada(x,P1,P2) ; jogada(o,P1,P2)), write('Jogada inválida'), nl, nl, mostra_jogo);
                        assert(jogada(V, P1, P2)), retract(jogada(n, P1, P2)), nl, mostra_jogo,
                        verifica_deu_velha(V).