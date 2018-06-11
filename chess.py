isClick = False
position1 = ""
position2 = ""

# On initialise le plateau 8*8 avec des x
l = 8; c = 8
Plateau = [['x']*l for i in range(c)]

# On place les pièces
Plateau[0][0]='Tn1'
Plateau[0][1]='Cn1'
Plateau[0][2]='Fn1'
Plateau[0][3]='Qn'
Plateau[0][4]='Kn'
Plateau[0][5]='Fn2'
Plateau[0][6]='Cn2'
Plateau[0][7]='Tn2'

Plateau[7][0]='Tb1'
Plateau[7][1]='Cb1'
Plateau[7][2]='Fb1'
Plateau[7][3]='Qb'
Plateau[7][4]='Kb'
Plateau[7][5]='Fb2'
Plateau[7][6]='Cb2'
Plateau[7][7]='Tb2'

class Piece:

    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color


class Pawn:

    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.name = 'Pawn'


# initialize all white pawns
for i in range(0, 8):
    Plateau[1][i] = Pawn(1, i, 'white')
    print(Plateau[1][i].column)

# initialize all black pawns
for i in range(0, 8):
    Plateau[6][i] = Pawn(6, i, 'black')
    #print(varPawn.__dict__)




# Affichage du Plateau de jeu
import tkinter
from tkinter import *

Window = Tk()

for ligne in range(8):
    for colonne in range(8):
        Button(Window, width=8, height=4, text=Plateau[ligne][colonne], borderwidth=1).grid(row=ligne, column=colonne)


def Click(event):
    global isClick, position1, position2
    if isClick == False:
        print("Click 1 OK!")
        positionX = Button.grid_info(event.widget)['row']
        positionY = Button.grid_info(event.widget)['column']
        print (positionX, positionY)
        print(isClick)
        isClick = True
        #PossibleMove()
    else:
        print ("Click 2 OK!")
        position2 = event.widget
        print(isClick) 
        isClick = False  

Window.bind("<Button-1>", Click)
Window.mainloop()