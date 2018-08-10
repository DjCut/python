
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

    def possibleMove(self, positionX, positionY, color):
        possibleMove = []

        if color == 'black':
            if positionX == 6 and Plateau[positionX - 1][positionY] is None:
                possibleMove.append(positionX - 2)
                possibleMove.append(positionY)
            if Plateau[positionX - 1][positionY] is None:
                possibleMove.append(positionX - 1)
                possibleMove.append(positionY)
            if 7 >= positionY - 1 >= 0:
                if Plateau[positionX - 1][positionY - 1] is not None:
                    if Plateau[positionX - 1][positionY - 1].color != color:
                        possibleMove.append(positionX - 1)
                        possibleMove.append(positionY - 1)
                        if Plateau[positionX - 1][positionY - 1].name == 'Pawn':
                            possibleMove.append(100)
                            possibleMove.append(100)
            if 7 >= positionY + 1 >= 0:
                if Plateau[positionX - 1][positionY + 1] is not None:
                    if Plateau[positionX - 1][positionY + 1].color != color:
                        possibleMove.append(positionX - 1)
                        possibleMove.append(positionY + 1)
                        if Plateau[positionX - 1][positionY + 1].name == 'Pawn':
                            possibleMove.append(100)
                            possibleMove.append(100)
        else:
            if positionX == 1 and Plateau[positionX + 1][positionY] is None:
                possibleMove.append(positionX + 2)
                possibleMove.append(positionY)
            if Plateau[positionX + 1][positionY] is None:
                possibleMove.append(positionX + 1)
                possibleMove.append(positionY)
            if 7 >= positionY - 1 >= 0:
                if Plateau[positionX + 1][positionY - 1] is not None:
                    if Plateau[positionX + 1][positionY - 1].color != color:
                        possibleMove.append(positionX + 1)
                        possibleMove.append(positionY - 1)
                        if Plateau[positionX + 1][positionY - 1].name == 'Pawn':
                            possibleMove.append(100)
                            possibleMove.append(100)
            if 7 >= positionY + 1 >= 0:
                if Plateau[positionX + 1][positionY + 1] is not None:
                    if Plateau[positionX + 1][positionY + 1].color != color:
                        possibleMove.append(positionX + 1)
                        possibleMove.append(positionY + 1)
                        if Plateau[positionX + 1][positionY + 1].name == 'Pawn':
                            possibleMove.append(100)
                            possibleMove.append(100)

        return possibleMove


class Rook(Piece):
    def __init__(self, row, column, color):
        Piece.__init__(self, row, column, color)
        self.name = 'Rook'

    def possibleMove(self, positionX, positionY, color):
        possibleMove = []

        # Check UP and DOWN position
        for i in range(-1, 2, 2):
            X = positionX + i
            if 7 >= X >= 0:
                if Plateau[X][positionY] is not None:
                    if Plateau[X][positionY].color != color:
                        possibleMove.append(X)
                        possibleMove.append(positionY)
                        if Plateau[X][positionY].name == 'Rook' or Plateau[X][positionY].name == 'Queen':
                            possibleMove.append(100)
                            possibleMove.append(100)
            while (7 >= X >= 0) and (Plateau[X][positionY]) is None:
                possibleMove.append(X)
                possibleMove.append(positionY)
                X = X + i
                if 7 >= X >= 0:
                    if Plateau[X][positionY] is not None:
                        if Plateau[X][positionY].color != color:
                            possibleMove.append(X)
                            possibleMove.append(positionY)
                            if Plateau[X][positionY].name == 'Rook' or Plateau[X][positionY].name == 'Queen':
                                possibleMove.append(100)
                                possibleMove.append(100)

        # Check LEFT and RIGHT position
        for i in range(-1, 2, 2):
            Y = positionY + i
            if 7 >= Y >= 0:
                if Plateau[positionX][Y] is not None:
                    if Plateau[positionX][Y].color != color:
                        possibleMove.append(positionX)
                        possibleMove.append(Y)
                        if Plateau[positionX][Y].name == 'Rook' or Plateau[positionX][Y].name == 'Queen':
                            possibleMove.append(100)
                            possibleMove.append(100)
            while (7 >= Y >= 0) and (Plateau[positionX][Y]) is None:
                possibleMove.append(positionX)
                possibleMove.append(Y)
                Y = Y + i
                if 7 >= Y >= 0:
                    if Plateau[positionX][Y] is not None:
                        if Plateau[positionX][Y].color != color:
                            possibleMove.append(positionX)
                            possibleMove.append(Y)
                            if Plateau[positionX][Y].name == 'Rook' or Plateau[positionX][Y].name == 'Queen':
                                possibleMove.append(100)
                                possibleMove.append(100)

        return possibleMove


class Knight(Piece):
    def __init__(self, row, column, color):
        Piece.__init__(self, row, column, color)
        self.name = 'Knight'

    def possibleMove(self, positionX, positionY, color):
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
                    if Plateau[positionX + i][positionY + j] is not None:
                        if Plateau[positionX + i][positionY + j].color != color:
                            possibleMove.append(positionX + i)
                            possibleMove.append(positionY + j)
                            if Plateau[positionX + i][positionY + j].name == 'Knight':
                                possibleMove.append(100)
                                possibleMove.append(100)
            j *= (-1)
            if 7 >= positionX + i >= 0:
                if 7 >= positionY + j >= 0:
                    if Plateau[positionX + i][positionY + j] is None:
                        possibleMove.append(positionX + i)
                        possibleMove.append(positionY + j)
                    if Plateau[positionX + i][positionY + j] is not None:
                        if Plateau[positionX + i][positionY + j].color != color:
                            possibleMove.append(positionX + i)
                            possibleMove.append(positionY + j)
                            if Plateau[positionX + i][positionY + j].name == 'Knight':
                                possibleMove.append(100)
                                possibleMove.append(100)

        return possibleMove


class Bishop(Piece):
    def __init__(self, row, column, color):
        Piece.__init__(self, row, column, color)
        self.name = 'Bishop'

    def possibleMove(self, positionX, positionY, color):
        possibleMove = []

        for h in range(-1, 2, 2):
            for i in range(-1, 2, 2):
                X = positionX + i
                Y = positionY + h
                if 7 >= X >= 0 and 7 >= Y >= 0:
                    if Plateau[X][Y] is not None:
                        if Plateau[X][Y].color != color:
                            possibleMove.append(X)
                            possibleMove.append(Y)
                            if Plateau[X][Y].name == 'Bishop' or Plateau[X][Y].name == 'Queen':
                                possibleMove.append(100)
                                possibleMove.append(100)
                while (7 >= X >= 0) and 7 >= Y >= 0 and (Plateau[X][Y]) is None:
                    possibleMove.append(X)
                    possibleMove.append(Y)
                    X = X + i
                    Y = Y + h
                    if 7 >= X >= 0 and 7 >= Y >= 0:
                        if Plateau[X][Y] is not None:
                            if Plateau[X][Y].color != color:
                                possibleMove.append(X)
                                possibleMove.append(Y)
                                if Plateau[X][Y].name == 'Bishop' or Plateau[X][Y].name == 'Queen':
                                    possibleMove.append(100)
                                    possibleMove.append(100)
        return possibleMove


class Queen(Piece):
    def __init__(self, row, column, color):
        Piece.__init__(self, row, column, color)
        self.name = 'Queen'

    def possibleMove(self, positionX, positionY, color):

        # Get the Rook movement
        if color == 'white':
            possibleMove = RookWhite.possibleMove(positionX, positionY, color)
        else:
            possibleMove = RookBlack.possibleMove(positionX, positionY, color)

        # Get the Bishop movement
        if color == 'white':
            possibleMove = possibleMove + BishopWhite.possibleMove(positionX, positionY, color)
        else:
            possibleMove = possibleMove + BishopBlack.possibleMove(positionX, positionY, color)

        return possibleMove

class King(Piece):
    def __init__(self, row, column, color):
        Piece.__init__(self, row, column, color)
        self.name = 'King'

    def possibleMove(self, positionX, positionY, color):
        possibleMove = []

        for i in range(-1, 2):
            X = positionX + i
            for j in range(-1, 2):
                Y = positionY + j
                if 7 >= X >= 0 and 7 >= Y >= 0:
                    if Plateau[X][Y] is not None:
                        if Plateau[X][Y].color != color:
                            possibleMove.append(X)
                            possibleMove.append(Y)
                            if Plateau[X][Y].name == 'King':
                                possibleMove.append(100)
                                possibleMove.append(100)
                    else:
                        possibleMove.append(X)
                        possibleMove.append(Y)

        return possibleMove


#############################################
# OBJECTS
#############################################

# Objects used for the Queen movement
RookWhite = Rook(10, 10, 'white')
RookBlack = Rook(10, 10, 'black')
BishopWhite = Bishop(10, 10, 'white')
BishopBlack = Bishop(10, 10, 'black')

# Objects used for the check function
RookObject = Rook(10, 10, 'red')
BishopObject = Bishop(10, 10, 'red')
PawnObject = Pawn(10, 10, 'red')
KnightObject = Knight(10, 10, 'red')
QueenObject = Queen(10, 10, 'red')
KingObject = King(10, 10, 'red')

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

    global isClick, player, PieceActivated, getPossibleMove, checkTest

    if isClick == 'false':

        print("Click 1 OK!")
        checkTest = 'false'
        Chessboard()

        # We get the position of the mouse click
        positionX = Button.grid_info(event.widget)['row']
        positionY = Button.grid_info(event.widget)['column']

        PieceActivated = Plateau[positionX][positionY]
        print(PieceActivated)

        if Plateau[positionX][positionY] is not None:
            # highlight
            Button(Window, width=60, height=60, image=eval(''.join([PieceActivated.color, PieceActivated.name])), bg='gold', borderwidth=0).grid(row=positionX, column=positionY)

            print(Plateau[positionX][positionY].color, Plateau[positionX][positionY].name, 'at row:', positionX,'and column:', positionY)
            if Plateau[positionX][positionY].color == player:
                isClick = 'true'
                getPossibleMove = Plateau[positionX][positionY].possibleMove(positionX, positionY, Plateau[positionX][positionY].color)
                print(getPossibleMove)
        else:
            print('No piece at row:', positionX, 'and column:', positionY)

    else:

        print("Click 2 OK!")

        # We get the position of the mouse click
        positionX = Button.grid_info(event.widget)['row']
        positionY = Button.grid_info(event.widget)['column']

        # We save the old position of the piece activated
        oldPositionX = PieceActivated.row
        oldPositionY = PieceActivated.column

        # we temporary remove old graphical position of the piece
        Plateau[PieceActivated.row][PieceActivated.column] = None
        # we temporary move the piece object on the new Plateau position
        originalPiece = Plateau[positionX][positionY]
        Plateau[positionX][positionY] = PieceActivated
        # we temporary define the new position of the piece object
        PieceActivated.row = positionX
        PieceActivated.column = positionY

        # Is my King checked if I move like this?
        check()

        # we remove the temporary graphical position of the piece
        Plateau[positionX][positionY] = originalPiece
        # we move the piece object on the old Plateau position
        Plateau[oldPositionX][oldPositionY] = PieceActivated
        # we define the old position of the piece object
        PieceActivated.row = oldPositionX
        PieceActivated.column = oldPositionY

        print("Possible Move: ", getPossibleMove)
        if pair_list(getPossibleMove, positionX, positionY) == 'true' and checkTest == 'false':
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
                # Is the opponent's King CheckMated?
                checkMate()
                return
            if player == 'black':
                player = 'white'
                # Is the opponent's King CheckMated?
                checkMate()



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


def check():
    global checkTest, player
    checkTest = 'false'
    print('Is the king can move like a this piece? If 100 inside the move means a piece moving like this piece checked the king:')
    for ligne in range(8):
        for colonne in range(8):
            if Plateau[ligne][colonne] is not None:
                if Plateau[ligne][colonne].name == 'King' and Plateau[ligne][colonne].color == player:
                    rook = RookObject.possibleMove(ligne, colonne, player)
                    print('rookCheckMove:', rook)
                    for i in range(0, len(rook), 2):
                        if rook[i] == 100:
                            checkTest = 'true'
                            print('CHECKED BY A ROOK (or a Queen)')
                            break
                    bishop = BishopObject.possibleMove(ligne, colonne, player)
                    print('bishopCheckMove:', bishop)
                    for i in range(0, len(bishop), 2):
                        if bishop[i] == 100:
                            checkTest = 'true'
                            print('CHECKED BY A BISHOP (or a Queen)')
                            break
                    pawn = PawnObject.possibleMove(ligne, colonne, player)
                    print('pawnCheckMove:', pawn)
                    for i in range(0, len(pawn), 2):
                        if pawn[i] == 100:
                            checkTest = 'true'
                            print('CHECKED BY A PAWN')
                            break
                    knight = KnightObject.possibleMove(ligne, colonne, player)
                    print('knightCheckMove:', knight)
                    for i in range(0, len(knight), 2):
                        if knight[i] == 100:
                            checkTest = 'true'
                            print('CHECKED BY A KNIGHT')
                            break
                    queen = QueenObject.possibleMove(ligne, colonne, player)
                    print('queenCheckMove', queen)
                    for i in range(0, len(queen), 2):
                        if queen[i] == 100:
                            checkTest = 'true'
                            print('CHECKED BY A QUEEN (or a Bishop, or a Rook)')
                            break
                    king = KingObject.possibleMove(ligne, colonne, player)
                    print('kingCheckMove:', king)
                    for i in range(0, len(king), 2):
                        if king[i] == 100:
                            checkTest = 'true'
                            print('CHECKED BY A KING')
                            break


def checkMate():
    global player, checkTest, checkMateTest
    checkMateTest = 'false'
    for ligne in range(8):
        for colonne in range(8):
            if Plateau[ligne][colonne] is not None:
                if Plateau[ligne][colonne].color == player and Plateau[ligne][colonne].name == 'Queen':
                    getPossibleMove = Plateau[ligne][colonne].possibleMove(ligne, colonne, Plateau[ligne][colonne].color)
                    print('longueur du getPossibleMove de la Queen dans checkMate: ', len(getPossibleMove))
                    # We save the old position of the piece
                    oldPositionX = ligne
                    oldPositionY = colonne

                    for i in range(0, len(getPossibleMove), 2):
                        # we copy the piece present on this position in the variable originalPiece
                        originalPiece = Plateau[getPossibleMove[i]][getPossibleMove[i + 1]]
                        # We temporary move the piece object on the new Plateau position
                        Plateau[getPossibleMove[i]][getPossibleMove[i + 1]] = Plateau[ligne][colonne]
                        # we temporary define the new position of the piece object
                        Plateau[ligne][colonne].row = getPossibleMove[i]
                        Plateau[ligne][colonne].column = getPossibleMove[i + 1]

                        # Is my King checked if I move like this?
                        check()

                        # we move the piece object on the old Plateau position
                        Plateau[oldPositionX][oldPositionY] = Plateau[getPossibleMove[i]][getPossibleMove[i + 1]]
                        # we replace the original piece
                        Plateau[getPossibleMove[i]][getPossibleMove[i + 1]] = originalPiece
                        # we define the old position of the piece object
                        Plateau[ligne][colonne].row = oldPositionX
                        Plateau[ligne][colonne].column = oldPositionY
                        if checkTest == 'true':
                            checkMateTest = 'true'
                            break
    if checkMateTest == 'true':
        print('CHECKMATE')
    else:
        print('NO CHECKMATE')

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
checkTest = 'false'
checkMateTest = 'false'

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