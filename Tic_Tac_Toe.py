from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

def msg_box():
    ans = askquestion(title='Game Over', message='Do you want to quit the game')
    if ans == 'yes':
        root.destroy()
    else:
        reset()

def reset():
    a = 1
    for i in range(3):
        for j in range(3):
            b[i][j] = a
            a += 1
            btn[i][j].configure(text='')

def check_win():
    global b
    for i in range(3):
        if (b[i][0] == b[i][1] == b[i][2] == 'x') or (b[0][i] == b[1][i] == b[2][i] == 'x'):
            dec_win.configure(text='Player-1 won')
            msg_box()
        elif (b[i][0] == b[i][1] == b[i][2] == 'o') or (b[0][i] == b[1][i] == b[2][i] == 'o'):
            dec_win.configure(text='Player-2 won')
            msg_box()
    if (b[0][0] == b[1][1] == b[2][2] == 'x') or (b[0][2] == b[2][0] == b[2][2] == 'x'):
        dec_win.configure(text='Player-1 won')
        msg_box()
    elif (b[0][0] == b[1][1] == b[2][2] == 'o') or (b[0][2] == b[2][0] == b[2][2] == 'o'):
        dec_win.configure(text='Player-2 won')
        msg_box()

def values(r,c):
    global player
    if player == 'X':
        btn[r][c].configure(text="X")
        b[r][c] = 'x'
        player ='O'
        check_win()
    elif player == 'O':
        btn[r][c].configure(text="O")
        b[r][c] = 'o'
        player = 'X'
        check_win()


root = Tk()
btn = [[0,0,0],[0,0,0],[0,0,0]]
b = [[1,2,3],[4,5,6],[7,8,9]]
btn_frame = ttk.Frame(root)
btn_frame.grid(row=1, column=0, padx=7, pady=7)
winner_frame = ttk.Frame(root)
winner_frame.grid(row=0,column=0, padx=7, pady=7)

label1= ttk.Label(winner_frame,text='The winner is: ')
label1.grid(row=0, column=0, padx=7, pady=7)
dec_win = ttk.Label(winner_frame)
dec_win.grid(row=0, column=1)

for i in range(3):
    for j in range(3):
        btn[i][j] = Button(btn_frame,font=('Verdana',50,'bold'),width=3, bg='Yellow', fg='Red', command=lambda r=i,c=j:values(r,c))
        btn[i][j].grid(row=i, column=j)

player = 'X'

root.mainloop()