import sys
from termcolor import colored, cprint
def board(field):
    for row in range(12):
        if row % 2 == 0:
            practRow = int(row / 2)
            for column in range(15):
                if column != 14:
                    if column % 2 != 0:
                        practColumn = int(column / 2)
                        print(field[practColumn][practRow], end='')
                    else:
                        print('|', end='')
                else:
                    print('|')
        else:
            print('---------------')


# Check If the chosen column has empty space
def emptyLookUp(field, column):
    if ' ' not in field[column]:
        return True


# Check winner
# Vertical Check
def vLookUp(field, piece):
    i, j, k = 1, 2, 3
    for column in field:
        for cl in range(3):
            if column[l] == piece and column[l+i] == piece and column[j+l] == piece and column[k+l] == piece:
                return True


# Horizontal Check
def hLookUp(field, piece):
    i, j, k = 1, 2, 3
    for pos in range(1, 4):
        for rw in range(3):
            if field[rw][-pos] == piece and field[rw + i][-pos] == piece and field[rw + j][-pos] == piece and field[rw + k][-pos] == piece:
                return True


# Diagonal Check
def diagLookUp(field, piece):
    i, j, k, l = 1, 2, 3, 4
    for pos in range(4):
        if field[pos][-i] == piece and field[pos + i][-j] == piece and field[pos + j][-k] == piece and field[pos + k][-l] == piece:
            return True
    for pos in (1, 5):
        if field[-pos][-i] == piece and field[-pos - i][-j] == piece and field[-pos - j][-k] == piece and field[-pos - k][-l] == piece:
            return True


player = 1
drawField = [[' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ']]
board(drawField)
while True:
    print(f'Player turn {player}')
    moveColumn = int(input('Please enter a column [1 - 7]: '))
    moveColumn -= 1
    count = countP = 0
    if player == 1:
        mark = 'X'
        if emptyLookUp(drawField, moveColumn):
            print('There is no empty space available.')
        for l in range(5, -1, -1):
            if count == 0:
                if drawField[moveColumn][l] == ' ':
                    drawField[moveColumn][l] = 'X'
                    count += 1
                    player = 2
        if vLookUp(drawField, mark) or hLookUp(drawField, mark) or diagLookUp(drawField, mark):
            print('Player 1 has won the Game!!!')
            print('Congratulations!!')
            board(drawField)
            break

    if player == 2:
        mark = 'O'
        if emptyLookUp(drawField, moveColumn):
            print('There is no empty space available.')
        for c in range(5, -1, -1):
            if count == 0:
                if drawField[moveColumn][c] == ' ':
                    drawField[moveColumn][c] = 'O'
                    count += 1
                    player = 1
        if vLookUp(drawField, mark) or hLookUp(drawField, mark) or diagLookUp(drawField, mark):
            print('Player 2 has won the Game!!')
            print('Congratulations!!')
            board(drawField)
            break
    board(drawField)
