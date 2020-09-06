# desenvolvido por João Paulo de Souza e Leandro Souza Pinheiro

from tkinter import *
import tkinter.messagebox
import tictactoe

tk = Tk()
tk.title("Jogo da velha")
ttt = tictactoe.TicTacToe()
bclick = True
flag = 0
message = ''
buttons = []

# método para desabilitar o clique de um botão
def disableButton(button):
    button.configure(state=DISABLED)

# método que desabilita o clique de todos os botões com
# exceção do reset
def disableAllButtons():
    for i in buttons:
        disableButton(i)

# método para pegar o botão clicado e realizar a escrita em tela
def btnClick(button, position):
    # define que vai fazer uso das variaveis globais
    global bclick, flag
    # verifica se o texto do botão está vazio e caso esteja com a flag de clique como
    # true, indica que pode ser clicado e que o valor deve ser X
    if button["text"] == " " and bclick == True:
        # seta o texto do botão com X
        button["text"] = "X"
        # troca o valor da flag de clique para que venha o O
        bclick = False
        # soma a quantidade de botões clicados
        flag += 1
        # pega a mensagem de retorno do prolog caso exista
        message = ttt.pl('x', position[0], position[1])
    # da mesma forma, caso o texto do botão esteja vazio e a flag de clique
    # esteja como false
    elif button["text"] == " " and bclick == False:
        # seta o texto O no botão
        button["text"] = "O"
        # troca a flag de clique
        bclick = True
        # soma o botão clicado
        flag += 1
        # e pega a mensagem do prolog caso exista
        message = ttt.pl('o', position[0], position[1])

    # se a mensagem for diferente de none, indica que alguem
    # ganhou ou deu empate
    if message is not None:
        # então mostra na tela e bloqueia os botões
        tkinter.messagebox.showinfo("Jogo da velha", message)
        disableAllButtons()
        
    disableButton(button)

# método para o reset
def reset():
    bclick = True
    # recria o tabuleiro
    createBoard()
    # chama o método de jogada no prolog com a flag de reset como 1, ou seja, indicando o reset
    ttt.pl('n', 0, 0, 1)

# método para criar os botões e o tabuleiro
def createBoard():
    button1 = Button(tk, text=" ", font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button1, (0,0)))
    button1.grid(row=3, column=0)
    buttons.append(button1)

    button2 = Button(tk, text=' ', font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button2, (0, 1)))
    button2.grid(row=3, column=1)
    buttons.append(button2)

    button3 = Button(tk, text=' ',font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button3, (0, 2)))
    button3.grid(row=3, column=2)
    buttons.append(button3)

    button4 = Button(tk, text=' ', font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button4, (1, 0)))
    button4.grid(row=4, column=0)
    buttons.append(button4)

    button5 = Button(tk, text=' ', font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button5, (1, 1)))
    button5.grid(row=4, column=1)
    buttons.append(button5)

    button6 = Button(tk, text=' ', font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button6, (1, 2)))
    button6.grid(row=4, column=2)
    buttons.append(button6)

    button7 = Button(tk, text=' ', font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button7, (2, 0)))
    button7.grid(row=5, column=0)
    buttons.append(button7)

    button8 = Button(tk, text=' ', font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button8, (2, 1)))
    button8.grid(row=5, column=1)
    buttons.append(button8)

    button9 = Button(tk, text=' ', font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button9, (2, 2)))
    button9.grid(row=5, column=2)
    buttons.append(button9)

    button10 = Button(tk, text='Reset', font='Arial 20 bold', bg='#0f4e63', fg='white', height=1, width=28, command=lambda: reset())
    button10.grid(row=7,column=0, columnspan=3)


if __name__ == "__main__":
    createBoard()
    tk.mainloop()

