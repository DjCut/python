
#############################################
# PROGRAM
#############################################

import tkinter
from tkinter import *

#############################################
# PLATEAU
#############################################

# On initialise le plateau 8*8 avec des x
Plateau = [[None]*8 for i in range(8)]

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

    def possibleMove(self, positionX, positionY):
        possibleMove = []
        j = 0
        for i in range(-2, 3):
            if i == -2: j = 1
            if i == -1: j = 2
            if i == 1: j = 2
            if i == 2: j = 1
            if i == 0: continue
            if 7 >= positionX + i >= 0:
                if 7 >= positionY + j >= 0:
                    if Plateau[positionX + i][positionY + j] is None:
                        possibleMove.append(positionX + i)
                        possibleMove.append(positionY + j)
            j *= (-1)
            if 7 >= positionX + i >= 0:
                if 7 >= positionY + j >= 0:
                    if Plateau[positionX + i][positionY + j] is None:
                        possibleMove.append(positionX + i)
                        possibleMove.append(positionY + j)

        return possibleMove

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

# initialize black pawns
for i in range(0, 8):
    Plateau[6][i] = Pawn(6, i, 'black')

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
Plateau[0][4] = Queen(0, 4, 'white')
Plateau[7][4] = Queen(7, 4, 'black')

# initialize Kings
Plateau[0][3] = King(0, 3, 'white')
Plateau[7][3] = King(7, 3, 'black')

##################################
# Fonctions
##################################


def Chessboard():

    bg = 'false'

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

            if Plateau[ligne][colonne] is None:
                Button(Window, width=8, height=4, text='', bg=background, borderwidth=0).grid(row=ligne, column=colonne)
            elif Plateau[ligne][colonne].name == 'Pawn' and Plateau[ligne][colonne].color == 'white':
                Button(Window, width=60, height=60, image=whitePawn, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
            elif Plateau[ligne][colonne].name == 'Pawn' and Plateau[ligne][colonne].color == 'black':
                Button(Window, width=60, height=60, image=blackPawn, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
            elif Plateau[ligne][colonne].name == 'Rook' and Plateau[ligne][colonne].color == 'white':
                Button(Window, width=60, height=60, image=whiteRook, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
            elif Plateau[ligne][colonne].name == 'Rook' and Plateau[ligne][colonne].color == 'black':
                Button(Window, width=60, height=60, image=blackRook, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
            elif Plateau[ligne][colonne].name == 'Knight' and Plateau[ligne][colonne].color == 'white':
                Button(Window, width=60, height=60, image=whiteKnight, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
            elif Plateau[ligne][colonne].name == 'Knight' and Plateau[ligne][colonne].color == 'black':
                Button(Window, width=60, height=60, image=blackKnight, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
            elif Plateau[ligne][colonne].name == 'Bishop' and Plateau[ligne][colonne].color == 'white':
                Button(Window, width=60, height=60, image=whiteBishop, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
            elif Plateau[ligne][colonne].name == 'Bishop' and Plateau[ligne][colonne].color == 'black':
                Button(Window, width=60, height=60, image=blackBishop, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
            elif Plateau[ligne][colonne].name == 'Queen' and Plateau[ligne][colonne].color == 'white':
                Button(Window, width=60, height=60, image=whiteQueen, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
            elif Plateau[ligne][colonne].name == 'Queen' and Plateau[ligne][colonne].color == 'black':
                Button(Window, width=60, height=60, image=blackQueen, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
            elif Plateau[ligne][colonne].name == 'King' and Plateau[ligne][colonne].color == 'white':
                Button(Window, width=60, height=60, image=whiteKing, bg=background, borderwidth=0).grid(row=ligne, column=colonne)
            elif Plateau[ligne][colonne].name == 'King' and Plateau[ligne][colonne].color == 'black':
                Button(Window, width=60, height=60, image=blackKing, bg=background, borderwidth=0).grid(row=ligne, column=colonne)


def rightClick(event):
    global isClick
    isClick = 'false'
    # remove highlight of the activated piece by refreshing the screen
    Chessboard()


def Click(event):

    global isClick, player, PieceActivated, getPossibleMove

    if isClick == 'false':

        print("Click 1 OK!")

        # We get the position of the mouse click
        positionX = Button.grid_info(event.widget)['row']
        positionY = Button.grid_info(event.widget)['column']

        PieceActivated = Plateau[positionX][positionY]
        print(PieceActivated)

        if Plateau[positionX][positionY] is not None:
            # highlight
            print(PieceActivated.color+PieceActivated.name)
            PieceActivatedImage =''.join([PieceActivated.color, PieceActivated.name])
            print(PieceActivatedImage)
            Button(Window, width=60, height=60, image=whiteKnight, bg='bisque3', borderwidth=0).grid(row=positionX, column=positionY)

            print(Plateau[positionX][positionY].color, Plateau[positionX][positionY].name, 'at row:', positionX,'and column:', positionY)
            if Plateau[positionX][positionY].color == player:
                isClick = 'true'
                getPossibleMove = Plateau[positionX][positionY].possibleMove(positionX, positionY)
                print(getPossibleMove)
        else:
            print('No piece at row:', positionX, 'and column:', positionY)

    else:

        print("Click 2 OK!")

        # We get the position of the mouse click
        positionX = Button.grid_info(event.widget)['row']
        positionY = Button.grid_info(event.widget)['column']

        print("Possible Move: ", getPossibleMove)
        if pair_list(getPossibleMove, positionX, positionY) == 'true':
            # we remove old graphical position of the piece
            Plateau[PieceActivated.row][PieceActivated.column] = None
            # we move the piece object on the new Plateau position
            Plateau[positionX][positionY] = PieceActivated
            # we define the new position of the piece object
            PieceActivated.row = positionX
            PieceActivated.column = positionY
            print(PieceActivated)
            print(PieceActivated.row, PieceActivated.column)
            print(Plateau[positionX][positionY].color, Plateau[positionX][positionY].name, 'moved to row:', positionX,'and column:', positionY)

            # The second click is validated, we entered in the if loop
            isClick = 'false'
            # we refresh the board
            Chessboard()
            # Player change
            if player == 'white':
                player = 'black'
                return
            if player == 'black':
                player = 'white'
        else:
            # The second click is NOT validated, we didn't enter in the if loop
            isClick = 'false'


def pair_list(getPossibleMoveList, X, Y):
    moveAccepted = 'false'
    print(len(getPossibleMoveList))
    for i in range(0, len(getPossibleMoveList), 2):
        if getPossibleMoveList[i] == X and getPossibleMoveList[i + 1] == Y:
            moveAccepted = 'true'
    return moveAccepted

#############################################
# TKINTER - MAIN PROGRAM
#############################################


Window = Tk()

#############################################
# VARIABLES
#############################################

player = 'white'
isClick = 'false'
PieceActivated = None

whitePawn = PhotoImage(file="pictures/pawnW.gif")
blackPawn = PhotoImage(file="pictures/pawnB.gif")
whiteRook = PhotoImage(file="pictures/rookW.gif")
blackRook = PhotoImage(file="pictures/rookB.gif")
whiteKnight = PhotoImage(file="pictures/knightW.gif")
blackKnight = PhotoImage(file="pictures/knightB.gif")
whiteBishop = PhotoImage(file="pictures/bishopW.gif")
blackBishop = PhotoImage(file="pictures/bishopB.gif")
whiteQueen = PhotoImage(file="pictures/queenW.gif")
blackQueen = PhotoImage(file="pictures/queenB.gif")
whiteKing = PhotoImage(file="pictures/kingW.gif")
blackKing = PhotoImage(file="pictures/kingB.gif")

##################################
# Affichage du Plateau de jeu
##################################

Chessboard()

# Left Click calls the function Click
Window.bind("<Button-1>", Click)
# Right click cancel the first click
Window.bind("<Button-3>", rightClick)
# Loop
Window.mainloop()