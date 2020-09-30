import sys
from termcolor import colored, cprint


# Printing the board
def board(field):
    for row in range(11):
        if row % 2 == 0:
            practRow = int(row / 2)
            for column in range(13):
                if column % 2 == 0:
                    practColumn = int(column / 2)
                    if column != 12:
                        print(field[practColumn][practRow], end='')
                    else:
                        print(field[practColumn][practRow])
                else:
                    cprint('|', 'blue', end='')
        else:
            cprint('-------------', 'cyan')


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
            if column[cl] == piece and column[cl+i] == piece and column[j+cl] == piece and column[k+cl] == piece:
                return True


# Horizontal Check
def hLookUp(field, piece):
    i, j, k = 1, 2, 3
    for pos in range(1, 4):
        for rw in range(4):
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
    while not 1 <= moveColumn <= 7:
        print('Invalid column number. Please try again.')
        moveColumn = int(input('Please enter a column [1 - 7]: '))
    moveColumn -= 1
    count = countP = 0
    if player == 1:
        mark = colored('X', 'red')
        if emptyLookUp(drawField, moveColumn):
            print('There is no empty space available.')
        for l in range(5, -1, -1):
            if count == 0:
                if drawField[moveColumn][l] == ' ':
                    drawField[moveColumn][l] = mark
                    count += 1
                    player = 2
        if vLookUp(drawField, mark) or hLookUp(drawField, mark) or diagLookUp(drawField, mark):
            cprint('-=-'*10, 'blue')
            cprint('Player 1 has won the Game!!!', 'red')
            cprint('Congratulations!!', 'red', attrs=['bold'])
            board(drawField)
            cprint('-=-'*10, 'blue')
            break

    if player == 2:
        mark = colored('O', 'green')
        if emptyLookUp(drawField, moveColumn):
            print('There is no empty space available.')
        for c in range(5, -1, -1):
            if count == 0:
                if drawField[moveColumn][c] == ' ':
                    drawField[moveColumn][c] = mark
                    count += 1
                    player = 1
        if vLookUp(drawField, mark) or hLookUp(drawField, mark) or diagLookUp(drawField, mark):
            cprint('-=-'*10, 'blue')
            cprint('Player 2 has won the Game!!', 'green')
            cprint('Congratulations!!', 'green', attrs=['bold'])
            board(drawField)
            cprint('-=-'*10, 'blue')
            break
    board(drawField)
