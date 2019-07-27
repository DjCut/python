
#############################################
# PROGRAM
#############################################

import sys
thisFunctionName = sys._getframe(   ).f_code.co_name
import tkinter as tk
from tkinter import *
root = tk.Tk()

#############################################
# PLATEAU
#############################################

# On initialise le plateau 8*8 avec des x
Plateau = [[None]*8 for i in range(8)]
# On initialise le dictionnaire de pieces capturees
CapturedPieces = {}

#############################################
# VARIABLES
#############################################

player = 'white'
move = 0
turn = 1
Rule50Moves = 0
isClick = False
PieceActivated = None
checkTest = False
checkMateTest = False
littleRockInProgress = False
bigRockInProgress = False

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

        if color == 'white':
            if positionX == 6 and Plateau[positionX - 1][positionY] is None and Plateau[positionX - 2][positionY] is None:
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
            if positionX == 1 and Plateau[positionX + 1][positionY] is None and Plateau[positionX + 2][positionY] is None:
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
    
    #def promote()


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
        self.littleRock = True
        self.bigRock = True

    def possibleMove(self, positionX, positionY, color):
        global littleRockInProgress, bigRockInProgress
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
            # Do this only if the caller function is click (not isItPat or check)
            caller = sys._getframe(1).f_code.co_name
            print(caller)
            if caller == 'Click':
                # Rock
                if Plateau[positionX][positionY].littleRock == True and Plateau[positionX][positionY+1] is None and Plateau[positionX][positionY+2] is None:
                    possibleMove.append(positionX)
                    possibleMove.append(positionY+2)
                    littleRockInProgress = True
                if Plateau[positionX][positionY].bigRock == True and Plateau[positionX][positionY-1] is None and Plateau[positionX][positionY-2] is None and Plateau[positionX][positionY-3] is None:
                    possibleMove.append(positionX)
                    possibleMove.append(positionY-2)
                    bigRockInProgress = True

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

# initialize black pawns
for i in range(0, 8):
    Plateau[1][i] = Pawn(1, i, 'black')

# initialize white pawns
for i in range(0, 8):
    Plateau[6][i] = Pawn(6, i, 'white')

# initialize rooks
Plateau[0][0] = Rook(0, 0, 'black')
Plateau[0][7] = Rook(0, 7, 'black')
Plateau[7][0] = Rook(7, 0, 'white')
Plateau[7][7] = Rook(7, 7, 'white')

# initialize knights
Plateau[0][1] = Knight(0, 1, 'black')
Plateau[0][6] = Knight(0, 6, 'black')
Plateau[7][1] = Knight(7, 1, 'white')
Plateau[7][6] = Knight(7, 6, 'white')

# initialize Bishops
Plateau[0][2] = Bishop(0, 2, 'black')
Plateau[0][5] = Bishop(0, 5, 'black')
Plateau[7][2] = Bishop(7, 2, 'white')
Plateau[7][5] = Bishop(7, 5, 'white')

# initialize Queens
Plateau[0][3] = Queen(0, 3, 'black')
Plateau[7][3] = Queen(7, 3, 'white')

# initialize Kings
Plateau[0][4] = King(0, 4, 'black')
Plateau[7][4] = King(7, 4, 'white')

##################################
# Fonctions
##################################


def Chessboard():
    
    canvas.delete("all")
    
    # Creation du damier
    color = True
    for j in range(0, 520, 65):
        for i in range(0, 520, 65):
            if color == False:
                canvas.create_rectangle(i, j, i+65, j+65, fill="grey", tags=("damier", i, j))
                if i != 455:
                    color = True
            elif color == True:
                canvas.create_rectangle(i, j, i+65, j+65, fill="white", tags=("damier", i, j))
                if i != 455:
                    color = False

    for ligne in range(8):
        for colonne in range(8):
           
            if Plateau[ligne][colonne] is None:
                canvas.create_image(colonne*65,ligne*65, anchor=NW, image=empty, tags=("empty", ligne, colonne))
            elif Plateau[ligne][colonne].name == 'Pawn' and Plateau[ligne][colonne].color == 'white':
                canvas.create_image(colonne*65,ligne*65, anchor=NW, image=whitePawn, tags=("whitePawn", ligne, colonne))
            elif Plateau[ligne][colonne].name == 'Pawn' and Plateau[ligne][colonne].color == 'black':
                canvas.create_image(colonne*65,ligne*65, anchor=NW, image=blackPawn, tags=("blackPawn", ligne, colonne))
            elif Plateau[ligne][colonne].name == 'Rook' and Plateau[ligne][colonne].color == 'white':
                canvas.create_image(colonne*65,ligne*65, anchor=NW, image=whiteRook, tags=("whiteRook", ligne, colonne))
            elif Plateau[ligne][colonne].name == 'Rook' and Plateau[ligne][colonne].color == 'black':
                canvas.create_image(colonne*65,ligne*65, anchor=NW, image=blackRook, tags=("blackRook", ligne, colonne))
            elif Plateau[ligne][colonne].name == 'Knight' and Plateau[ligne][colonne].color == 'white':
                canvas.create_image(colonne*65,ligne*65, anchor=NW, image=whiteKnight, tags=("whiteKnight", ligne, colonne))      
            elif Plateau[ligne][colonne].name == 'Knight' and Plateau[ligne][colonne].color == 'black':
                canvas.create_image(colonne*65,ligne*65, anchor=NW, image=blackKnight, tags=("blackKnight", ligne, colonne))
            elif Plateau[ligne][colonne].name == 'Bishop' and Plateau[ligne][colonne].color == 'white':
                canvas.create_image(colonne*65,ligne*65, anchor=NW, image=whiteBishop, tags=("whiteBishop", ligne, colonne))
            elif Plateau[ligne][colonne].name == 'Bishop' and Plateau[ligne][colonne].color == 'black':
                canvas.create_image(colonne*65,ligne*65, anchor=NW, image=blackBishop, tags=("blackBishop", ligne, colonne))
            elif Plateau[ligne][colonne].name == 'Queen' and Plateau[ligne][colonne].color == 'white':
                canvas.create_image(colonne*65,ligne*65, anchor=NW, image=whiteQueen, tags=("whiteQueen", ligne, colonne))
            elif Plateau[ligne][colonne].name == 'Queen' and Plateau[ligne][colonne].color == 'black':
                canvas.create_image(colonne*65,ligne*65, anchor=NW, image=blackQueen, tags=("blackQueen", ligne, colonne))
            elif Plateau[ligne][colonne].name == 'King' and Plateau[ligne][colonne].color == 'white':
                canvas.create_image(colonne*65,ligne*65, anchor=NW, image=whiteKing, tags=("whiteKing", ligne, colonne))
            elif Plateau[ligne][colonne].name == 'King' and Plateau[ligne][colonne].color == 'black':
                canvas.create_image(colonne*65,ligne*65, anchor=NW, image=blackKing, tags=("blackKing", ligne, colonne))


def rightClick(event):
    global isClick
    isClick = False
    # remove highlight of the activated piece by refreshing the screen
    Chessboard()


def Click(event):

    global isClick, player, Rule50Moves, move, turn, PieceActivated, getPossibleMove, checkTest, littleRockInProgress, bigRockInProgress
    Chessboard()
    
    if isClick == False:

        print("Click 1 OK!")
        
        # We get the position of the mouse click
        item = canvas.find_closest(event.x, event.y)
        positionX = int(canvas.gettags(item)[1])
        positionY = int(canvas.gettags(item)[2])

        PieceActivated = Plateau[positionX][positionY]

        if Plateau[positionX][positionY] is not None and Plateau[positionX][positionY].color == player:
            # highlight
            damier = item[0]-64
            canvas.itemconfig(damier, fill="gold")

            print(Plateau[positionX][positionY].color, Plateau[positionX][positionY].name, 'at row:', positionX,'and column:', positionY)
            if Plateau[positionX][positionY].color == player:
                isClick = True
                getPossibleMove = Plateau[positionX][positionY].possibleMove(positionX, positionY, Plateau[positionX][positionY].color)
                print('Possible Move:', getPossibleMove)
        else:
            print('No piece at row:', positionX, 'and column:', positionY)

    else:

        print("Click 2 OK!")
        checkTest = False

        # We get the position of the mouse click
        item = canvas.find_closest(event.x, event.y)
        positionX = int(canvas.gettags(item)[1])
        positionY = int(canvas.gettags(item)[2])
        print('We get the position of the mouse click', positionX, positionY)

        if pair_list(getPossibleMove, positionX, positionY) == True:
            # We save the old position of the piece activated
            oldPositionX = PieceActivated.row
            oldPositionY = PieceActivated.column

            # Rock
            if littleRockInProgress == True and positionY == 6:
                # we temporary move the piece object on the new Plateau position
                originalPiece = Plateau[positionX][positionY-1]
                Plateau[positionX][positionY-1] = PieceActivated
                # we temporary define the new position of the piece object
                PieceActivated.row = positionX
                PieceActivated.column = positionY-1
            
                print('***************************************')
                print('Is my King checked if I move like this?')

                check()

                # we remove the temporary graphical position of the piece
                Plateau[positionX][positionY-1] = originalPiece
                # we move the piece object on the old Plateau position
                Plateau[oldPositionX][oldPositionY] = PieceActivated
                # we define the old position of the piece object
                PieceActivated.row = oldPositionX
                PieceActivated.column = oldPositionY 

            if bigRockInProgress == True and positionY == 2:
                # we temporary move the piece object on the new Plateau position
                originalPiece = Plateau[positionX][positionY+1]
                Plateau[positionX][positionY+1] = PieceActivated
                # we temporary define the new position of the piece object
                PieceActivated.row = positionX
                PieceActivated.column = positionY+1
            
                print('***************************************')
                print('Is my King checked if I move like this?')

                check()          

                # we remove the temporary graphical position of the piece
                Plateau[positionX][positionY+1] = originalPiece
                # we move the piece object on the old Plateau position
                Plateau[oldPositionX][oldPositionY] = PieceActivated
                # we define the old position of the piece object
                PieceActivated.row = oldPositionX
                PieceActivated.column = oldPositionY 

            # we temporary remove old graphical position of the piece
            Plateau[PieceActivated.row][PieceActivated.column] = None
            # we temporary move the piece object on the new Plateau position
            originalPiece = Plateau[positionX][positionY]
            Plateau[positionX][positionY] = PieceActivated
            # we temporary define the new position of the piece object
            PieceActivated.row = positionX
            PieceActivated.column = positionY

            print('***************************************')
            print('Is my King checked if I move like this?')

            check()        
            
            # we remove the temporary graphical position of the piece
            Plateau[positionX][positionY] = originalPiece
            # we move the piece object on the old Plateau position
            Plateau[oldPositionX][oldPositionY] = PieceActivated
            # we define the old position of the piece object
            PieceActivated.row = oldPositionX
            PieceActivated.column = oldPositionY
            
            if checkTest == False:
            
                # Check if the Rooks or the King are moving, then disable Rock
                if player == 'white':
                    if Plateau[PieceActivated.row][PieceActivated.column].name == 'King':
                        Plateau[PieceActivated.row][PieceActivated.column].littleRock = False
                        Plateau[PieceActivated.row][PieceActivated.column].bigRock = False
                    if  Plateau[PieceActivated.row][PieceActivated.column].name == 'Rook' and PieceActivated.column == 0:
                        x,y = whereIsTheKing()
                        Plateau[x][y].bigRock = False
                    if  Plateau[PieceActivated.row][PieceActivated.column].name == 'Rook' and PieceActivated.column == 7:
                        x,y = whereIsTheKing()
                        Plateau[x][y].littleRock = False
                else:
                    if Plateau[PieceActivated.row][PieceActivated.column].name == 'King':
                        Plateau[PieceActivated.row][PieceActivated.column].littleRock = False
                        Plateau[PieceActivated.row][PieceActivated.column].bigRock = False
                    if  Plateau[PieceActivated.row][PieceActivated.column].name == 'Rook' and PieceActivated.column == 0:
                        x,y = whereIsTheKing()
                        Plateau[x][y].bigRock = False
                    if  Plateau[PieceActivated.row][PieceActivated.column].name == 'Rook' and PieceActivated.column == 7:
                        x,y = whereIsTheKing()
                        Plateau[x][y].littleRock = False

                # we remove old graphical position of the piece
                Plateau[PieceActivated.row][PieceActivated.column] = None
                # we check if a piece exists on the new Plateau position
                if Plateau[positionX][positionY] != None:
                    CapturedPieces.update({move:Plateau[positionX][positionY]})
                # we move the piece object on the new Plateau position
                Plateau[positionX][positionY] = PieceActivated
                # we define the new position of the piece object
                PieceActivated.row = positionX
                PieceActivated.column = positionY

                # Promote pawn
                if PieceActivated.name == 'Pawn' and PieceActivated.row == 0 and player == 'white':
                    Plateau[positionX][positionY] = Queen(positionX, positionY, 'white')
                if PieceActivated.name == 'Pawn' and PieceActivated.row == 7 and player == 'black':
                    Plateau[positionX][positionY] = Queen(positionX, positionY, 'black')        

                print('****************************************')
                print(Plateau[positionX][positionY].color, Plateau[positionX][positionY].name, 'moved to row:', positionX,'and column:', positionY)
                print('****************************************')

                # Rule 50 moves
                if Plateau[positionX][positionY].name == 'Pawn' or move in CapturedPieces:
                    Rule50Moves = 0
                else:
                    Rule50Moves += 1
                
                #if move in CapturedPieces:
                    #print('****************************************')
                    #print(Plateau[8][turn].color, Plateau[8][turn].name, 'has been captured')
                    #print('****************************************')

                # The second click is validated, we entered in the if loop
                isClick = False
                
                # Rock
                if littleRockInProgress == True:
                    littleRockInProgress = False 
                    Plateau[positionX][positionY].littleRock = False
                    Plateau[positionX][positionY].bigRock = False 
                    # Move the Rook
                    if Plateau[positionX][6] != None:
                        if Plateau[positionX][6].name == 'King':
                            # we remove old graphical position of the rook
                            littleRock = None
                            littleRock = Plateau[positionX][7]
                            Plateau[positionX][7] = None
                            # we move the piece object on the new Plateau position
                            Plateau[positionX][5] = littleRock
                            # we define the new position of the piece object
                            littleRock.row = positionX
                            littleRock.column = 5
                elif bigRockInProgress == True:
                    bigRockInProgress = False 
                    Plateau[positionX][positionY].littleRock = False
                    Plateau[positionX][positionY].bigRock = False  
                    # Move the Rook
                    if Plateau[positionX][2] != None:
                        if Plateau[positionX][2].name == 'King':
                            # we remove old graphical position of the rook
                            bigRock = None
                            bigRock = Plateau[positionX][0]
                            Plateau[positionX][0] = None
                            # we move the piece object on the new Plateau position
                            Plateau[positionX][3] = bigRock
                            # we define the new position of the piece object
                            bigRock.row = positionX
                            bigRock.column = 3  

                # we refresh the board
                Chessboard()

                # Player change and checkMate Test
                if player == 'white':
                    player = 'black'
                    print('Is the ennemy King CheckMated?')
                    check()
                    if checkTest == True:
                        checkMate()
                    checkTest = False
                    drawForRule50Moves()
                    isItPat()
                    twoKings()
                    move += 1
                    print ('Move number:', move)
                    print('Rule50Moves:', Rule50Moves)
                    return
                if player == 'black':
                    player = 'white'
                    print('Is the ennemy King CheckMated?')
                    check()
                    if checkTest == True:
                        checkMate()
                    checkTest = False
                    isItPat()
                    twoKings()
                    drawForRule50Moves()
                    move += 1
                    print('Move number:', move)
                    print('Rule50Moves:', Rule50Moves)
                    turn += 1
                    print('Turn number:', turn)
            else:
                # The checkTest is True
                isClick = False
                littleRockInProgress = False 
                bigRockInProgress = False 
        else:
            # The second click is NOT validated, we didn't enter in the if loop
            isClick = False

def drawForRule50Moves():
    if Rule50Moves == 50:
        draw()

def twoKings():
    pieceNumber = 0
    for ligne in range(8):
        for colonne in range(8):           
            if Plateau[ligne][colonne] != None:
                pieceNumber += 1
    if pieceNumber == 2:
        draw()    

def isItPat():
    global player, checkTest
    thisIsPat = True
    thisIsReallyNotPat = False
    for ligne in range(8):
        for colonne in range(8):           
            if Plateau[ligne][colonne] != None and Plateau[ligne][colonne].color == player:
                getPossibleMove = Plateau[ligne][colonne].possibleMove(ligne, colonne, player)
                if len(getPossibleMove) != 0 and Plateau[ligne][colonne].name != 'King':
                    thisIsPat = False
                if Plateau[ligne][colonne].name == 'King':
                    if len(getPossibleMove) != 0:
                        PieceActivated = Plateau[ligne][colonne]
                        # We save the old position of the piece activated
                        oldPositionX = PieceActivated.row
                        oldPositionY = PieceActivated.column
                        for i in range(0, len(getPossibleMove), 2):
                            checkTest = False
                            # we temporary remove old graphical position of the piece
                            Plateau[oldPositionX][oldPositionY] = None
                            # we temporary move the piece object on the new Plateau position
                            originalPiece = Plateau[getPossibleMove[i]][getPossibleMove[i+1]]
                            Plateau[getPossibleMove[i]][getPossibleMove[i+1]] = PieceActivated
                            # we temporary define the new position of the piece object
                            PieceActivated.row = getPossibleMove[i]
                            PieceActivated.column = getPossibleMove[i+1]

                            print('***************************************')
                            print('Is my King checked if I move like this?')

                            check()        
                            
                            # we remove the temporary graphical position of the piece
                            Plateau[getPossibleMove[i]][getPossibleMove[i+1]] = originalPiece
                            # we move the piece object on the old Plateau position
                            Plateau[oldPositionX][oldPositionY] = PieceActivated
                            # we define the old position of the piece object
                            PieceActivated.row = oldPositionX
                            PieceActivated.column = oldPositionY
                            
                            if checkTest == False:    
                                thisIsPat = False            
                                thisIsReallyNotPat = True
                            else:
                                thisIsPat = True   
                    elif len(getPossibleMove) == 0:
                        thisIsPat = True 
    if thisIsPat == True and thisIsReallyNotPat == False:
        draw()                    

def draw():
    print('')
    print('************************************************')
    print('**********************DRAW**********************')
    print('************************************************')

def pair_list(getPossibleMoveList, X, Y):
    moveAccepted = False
    for i in range(0, len(getPossibleMoveList), 2):
        if getPossibleMoveList[i] == X and getPossibleMoveList[i + 1] == Y:
            moveAccepted = True
    return moveAccepted

def whereIsTheKing():
    for ligne in range(8):
        for colonne in range(8):
            if Plateau[ligne][colonne] != None:
                if Plateau[ligne][colonne].name == 'King' and Plateau[ligne][colonne].color == player:
                    return ligne,colonne
                    break

def check():
    global checkTest, player
    print('*******************************************************************************************************')
    print('Is the king can move like this piece? If 100 inside, it means an ennemy piece moving like this check the king:')
    for ligne in range(8):
        for colonne in range(8):
            if Plateau[ligne][colonne] is not None:
                if Plateau[ligne][colonne].name == 'King' and Plateau[ligne][colonne].color == player:
                    rook = RookObject.possibleMove(ligne, colonne, player)
                    print('ROOK:', rook)
                    for i in range(0, len(rook), 2):
                        if rook[i] == 100:
                            checkTest = True
                            print('> CHECKED')
                            print('')
                            break
                    bishop = BishopObject.possibleMove(ligne, colonne, player)
                    print('BISHOP:', bishop)
                    for i in range(0, len(bishop), 2):
                        if bishop[i] == 100:
                            checkTest = True
                            print('> CHECKED')
                            print('')
                            break
                    pawn = PawnObject.possibleMove(ligne, colonne, player)
                    print('PAWN:', pawn)
                    for i in range(0, len(pawn), 2):
                        if pawn[i] == 100:
                            checkTest = True
                            print('> CHECKED')
                            print('')
                            break
                    knight = KnightObject.possibleMove(ligne, colonne, player)
                    print('KNIGHT:', knight)
                    for i in range(0, len(knight), 2):
                        if knight[i] == 100:
                            checkTest = True
                            print('> CHECKED')
                            print('')
                            break
                    queen = QueenObject.possibleMove(ligne, colonne, player)
                    print('QUEEN', queen)
                    for i in range(0, len(queen), 2):
                        if queen[i] == 100:
                            checkTest = True
                            print('> CHECKED')
                            print('')
                            break
                    king = KingObject.possibleMove(ligne, colonne, player)
                    print('KING:', king)
                    for i in range(0, len(king), 2):
                        if king[i] == 100:
                            checkTest = True
                            print('> CHECKED')
                            print('')
                            break


def checkMate():
    global player, checkTest, checkMateTest
    checkMateTest = True
    checkTest = False

    pieceList = ['King', 'Queen', 'Knight', 'Bishop', 'Rook', 'Pawn']
    for piece in pieceList:
        for ligne in range(8):
            for colonne in range(8):
                if Plateau[ligne][colonne] is not None:
                    if Plateau[ligne][colonne].color == player and Plateau[ligne][colonne].name == piece:
                        getPossibleMove = Plateau[ligne][colonne].possibleMove(ligne, colonne, Plateau[ligne][colonne].color)
                        print('*************************************************************************')
                        print('getPossibleMove of', piece, 'in the function checkMate: ', getPossibleMove)

                        for i in range(0, len(getPossibleMove), 2):
                            if getPossibleMove[i] == 100:
                                continue
                            # we copy the piece present on this position in the variable originalPiece
                            originalPiece = Plateau[getPossibleMove[i]][getPossibleMove[i + 1]]
                            # We temporary move the piece object on the new Plateau position
                            Plateau[getPossibleMove[i]][getPossibleMove[i + 1]] = Plateau[ligne][colonne]
                            Plateau[ligne][colonne] = None
                            Plateau[getPossibleMove[i]][getPossibleMove[i + 1]].row = getPossibleMove[i]
                            Plateau[getPossibleMove[i]][getPossibleMove[i + 1]].column = getPossibleMove[i + 1]

                            # Is my King checked if I move like this?
                            check()
                            print('<<<RESULT of the CheckTest>>>: ', checkTest)

                            # we move the piece object on the old Plateau position
                            Plateau[ligne][colonne] = Plateau[getPossibleMove[i]][getPossibleMove[i + 1]]
                            Plateau[ligne][colonne].row = ligne
                            Plateau[ligne][colonne].column = colonne
                            # we replace the original piece
                            Plateau[getPossibleMove[i]][getPossibleMove[i + 1]] = originalPiece

                            if checkTest == False:
                                checkMateTest = False
                            checkTest = False

    if checkMateTest == False:
        print('')
        print('************************************************')
        print('        CHECK: ', player, 'King is checked')
        print('************************************************')
    else:
        print('')
        print('************************************************')
        print('   CHECKMATE: ', player, 'player loose the game ')
        print('************************************************')



#############################################
# tkinter - MAIN PROGRAM
#############################################

canvas = tk.Canvas(root, 
           width=520, 
           height=520)
canvas.pack()

#############################################
# Images
#############################################

whitePawn   =   PhotoImage(file="pictures/pawnW.gif")
blackPawn   =   PhotoImage(file="pictures/pawnB.gif")
whiteRook   =   PhotoImage(file="pictures/rookW.gif")
blackRook   =   PhotoImage(file="pictures/rookB.gif")
whiteKnight =   PhotoImage(file="pictures/knightW.gif")
blackKnight =   PhotoImage(file="pictures/knightB.gif")
whiteBishop =   PhotoImage(file="pictures/bishopW.gif")
blackBishop =   PhotoImage(file="pictures/bishopB.gif")
whiteQueen  =   PhotoImage(file="pictures/queenW.gif")
blackQueen  =   PhotoImage(file="pictures/queenB.gif")
whiteKing   =   PhotoImage(file="pictures/kingW.gif")
blackKing   =   PhotoImage(file="pictures/kingB.gif")
empty       =   PhotoImage(file="pictures/empty.gif")

##################################
# Affichage du Plateau de jeu
##################################

Chessboard()

# Left Click calls the function Click
canvas.bind("<Button-1>", Click)
# Right click cancel the first click
canvas.bind("<Button-3>", rightClick)
# Loop
root.mainloop()