isClick = False
position1 = ""
position2 = ""

# On initialise le plateau 8*8 avec des x
l = 8; c = 8
Plateau = [[]*l for i in range(c)]

class Piece:

    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color


class Pawn(Piece):
<<<<<<< HEAD

    def __init__(self):
=======
    def __init__(self, row, column, color):
        Piece.__init__(self, row, column, color)
>>>>>>> a71168fd1290f2ce444c020e7f543d1e9296bdd5
        self.name = 'Pawn'


class Rook(Piece):
    def __init__(self, row, column, color):
        Piece.__init__(self, row, column, color)
        self.name = 'Rook'


class Knight(Piece):
    def __init__(self, row, column, color):
        Piece.__init__(self, row, column, color)
        self.name = 'Knight'


class Bishop(Piece):
    def __init__(self, row, column, color):
        Piece.__init__(self, row, column, color)
        self.name = 'Bishop'


class Queen(Piece):
    def __init__(self, row, column, color):
        Piece.__init__(self, row, column, color)
        self.name = 'Queen'


class King(Piece):
    def __init__(self, row, column, color):
        Piece.__init__(self, row, column, color)
        self.name = 'King'


# initialize white pawns
for i in range(0, 8):
    Plateau[1][i] = Pawn(1, i, 'white')
    print(Plateau[1][i].column)

# initialize black pawns
for i in range(0, 8):
    Plateau[6][i] = Pawn(6, i, 'black')
    #print(varPawn.__dict__)

# initialize rooks
Plateau[0][0] = Rook(0, 0, 'white')
Plateau[0][7] = Rook(0, 7, 'white')
Plateau[7][0] = Rook(7, 0, 'black')
Plateau[7][7] = Rook(7, 7, 'black')

# initialize knight
Plateau[0][1] = Knight(0, 1, 'white')
Plateau[0][6] = Knight(0, 6, 'white')
Plateau[7][1] = Knight(7, 1, 'black')
Plateau[7][6] = Knight(7, 6, 'black')



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