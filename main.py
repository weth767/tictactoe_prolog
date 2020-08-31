from tkinter import *
import tkinter.messagebox
import tictactoe

tk = Tk()
tk.title("Jogo da velha")
ttt = tictactoe.TicTacToe()
buttons = StringVar()
bclick = True
flag = 0
message = ''

def disableButton(button):
    button.configure(state=DISABLED)

def btnClick(button, position):
    global bclick, flag
    if button["text"] == " " and bclick == True:
        button["text"] = "X"
        bclick = False
        flag += 1
        message = ttt.pl('x', position[0], position[1])
    elif button["text"] == " " and bclick == False:
        button["text"] = "O"
        bclick = True
        flag += 1
        message = ttt.pl('o', position[0], position[1])

    if message is not None:
        tkinter.messagebox.showinfo("Jogo da velha", message)
    disableButton(button)

# método para o reset
def reset():
    createButtons()
    ttt.pl('x', 0, 0, 1)

# método para criar os botões
def createButtons():
    button1 = Button(tk, text=" ", font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button1, (0,0)))
    button1.grid(row=3, column=0)

    button2 = Button(tk, text=' ', font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button2, (0, 1)))
    button2.grid(row=3, column=1)

    button3 = Button(tk, text=' ',font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button3, (0, 2)))
    button3.grid(row=3, column=2)

    button4 = Button(tk, text=' ', font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button4, (1, 0)))
    button4.grid(row=4, column=0)

    button5 = Button(tk, text=' ', font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button5, (1, 1)))
    button5.grid(row=4, column=1)

    button6 = Button(tk, text=' ', font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button6, (1, 2)))
    button6.grid(row=4, column=2)

    button7 = Button(tk, text=' ', font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button7, (2, 0)))
    button7.grid(row=5, column=0)

    button8 = Button(tk, text=' ', font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button8, (2, 1)))
    button8.grid(row=5, column=1)

    button9 = Button(tk, text=' ', font='Arial 20 bold', bg='#0f4e63', fg='white', height=4, width=8, command=lambda: btnClick(button9, (2, 2)))
    button9.grid(row=5, column=2)

    button10 = Button(tk, text='Reset', font='Arial 20 bold', bg='#0f4e63', fg='white', height=1, width=28, command=lambda: reset())
    button10.grid(row=7,column=0, columnspan=3)

createButtons()

tk.mainloop()