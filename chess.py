
#############################################
# PROGRAM
#############################################

import tkinter
from tkinter import *

Window = Tk()

#############################################
# VARIABLES
#############################################

isClick = False
position1 = ""
position2 = ""
bg = 'false'

pawnW = PhotoImage(file="pictures/pawnW.gif")
pawnB = PhotoImage(file="pictures/pawnB.gif")
rookW = PhotoImage(file="pictures/rookW.gif")
rookB = PhotoImage(file="pictures/rookB.gif")
knightW = PhotoImage(file="pictures/knightW.gif")
knightB = PhotoImage(file="pictures/knightB.gif")
bishopW = PhotoImage(file="pictures/bishopW.gif")
bishopB = PhotoImage(file="pictures/bishopB.gif")
queenW = PhotoImage(file="pictures/queenW.gif")
queenB = PhotoImage(file="pictures/queenB.gif")
kingW = PhotoImage(file="pictures/kingW.gif")
kingB = PhotoImage(file="pictures/kingB.gif")

#############################################
# PLATEAU
#############################################

# On initialise le plateau 8*8 avec des x
Plateau = [['x']*8 for i in range(8)]


#############################################
# CLASS
#############################################


class Piece:

    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color


class Pawn(Piece):

    def __init__(self, row, column, color):
        Piece.__init__(self, row, column, color)
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


#############################################
# OBJECTS
#############################################


# initialize white pawns
for i in range(0, 8):
    Plateau[1][i] = Pawn(1, i, 'white')
    #print(Plateau[1][i].column)

# initialize black pawns
for i in range(0, 8):
    Plateau[6][i] = Pawn(6, i, 'black')
    #print(varPawn.__dict__)

# initialize rooks
Plateau[0][0] = Rook(0, 0, 'white')
Plateau[0][7] = Rook(0, 7, 'white')
Plateau[7][0] = Rook(7, 0, 'black')
Plateau[7][7] = Rook(7, 7, 'black')

# initialize knights
Plateau[0][1] = Knight(0, 1, 'white')
Plateau[0][6] = Knight(0, 6, 'white')
Plateau[7][1] = Knight(7, 1, 'black')
Plateau[7][6] = Knight(7, 6, 'black')

# initialize Bishops
Plateau[0][2] = Bishop(0, 2, 'white')
Plateau[0][5] = Bishop(0, 5, 'white')
Plateau[7][2] = Bishop(7, 2, 'black')
Plateau[7][5] = Bishop(7, 5, 'black')

# initialize Queens
Plateau[0][3] = Queen(0, 3, 'white')
Plateau[7][4] = Queen(7, 4, 'black')

# initialize Kings
Plateau[0][4] = King(0, 4, 'white')
Plateau[7][3] = King(7, 3, 'black')


##################################
# Affichage du Plateau de jeu
##################################

for ligne in range(8):
    for colonne in range(8):

        # Damier du plateau
        if bg == 'true':
            background = 'bisque2'
            if colonne != 7:
                bg = 'false'
        else:
            background = 'white'
            if colonne != 7:
                bg = 'true'

        if Plateau[ligne][colonne] == 'x':
            Button(Window, width=8, height=4, text='', bg=background, borderwidth=0).grid(row=ligne, column=colonne)
        elif Plateau[ligne][colonne].name == 'Pawn' and Plateau[ligne][colonne].color == 'white':
            Button(Window, width=60, height=60, image=pawnW, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
        elif Plateau[ligne][colonne].name == 'Pawn' and Plateau[ligne][colonne].color == 'black':
            Button(Window, width=60, height=60, image=pawnB, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
        elif Plateau[ligne][colonne].name == 'Rook' and Plateau[ligne][colonne].color == 'white':
            Button(Window, width=60, height=60, image=rookW, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
        elif Plateau[ligne][colonne].name == 'Rook' and Plateau[ligne][colonne].color == 'black':
            Button(Window, width=60, height=60, image=rookB, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
        elif Plateau[ligne][colonne].name == 'Knight' and Plateau[ligne][colonne].color == 'white':
            Button(Window, width=60, height=60, image=knightW, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
        elif Plateau[ligne][colonne].name == 'Knight' and Plateau[ligne][colonne].color == 'black':
            Button(Window, width=60, height=60, image=knightB, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
        elif Plateau[ligne][colonne].name == 'Bishop' and Plateau[ligne][colonne].color == 'white':
            Button(Window, width=60, height=60, image=bishopW, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
        elif Plateau[ligne][colonne].name == 'Bishop' and Plateau[ligne][colonne].color == 'black':
            Button(Window, width=60, height=60, image=bishopB, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
        elif Plateau[ligne][colonne].name == 'Queen' and Plateau[ligne][colonne].color == 'white':
            Button(Window, width=60, height=60, image=queenW, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
        elif Plateau[ligne][colonne].name == 'Queen' and Plateau[ligne][colonne].color == 'black':
            Button(Window, width=60, height=60, image=queenB, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
        elif Plateau[ligne][colonne].name == 'King' and Plateau[ligne][colonne].color == 'white':
            Button(Window, width=60, height=60, image=kingW, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
        elif Plateau[ligne][colonne].name == 'King' and Plateau[ligne][colonne].color == 'black':
            Button(Window, width=60, height=60, image=kingB, bg=background, borderwidth=0).grid(row=ligne, column=colonne)

##################################
# Fonctions
##################################
def Click(event):
    global isClick, position1, position2
    if isClick == False:
        print("Click 1 OK!")
        positionX = Button.grid_info(event.widget)['row']
        positionY = Button.grid_info(event.widget)['column']
        print(positionX, positionY)
        print(Plateau[positionX][positionY].name)
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