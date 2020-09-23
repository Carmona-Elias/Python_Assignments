
def board(field):
    for row in range(12): #0 1 2 3 4 5 6 7 8 9 10 11
        if row % 2 == 0: # 0 2 4 6 8 10
            practicalRow = int(row / 2) #0 1 2 3 4 5
            for column in range(17):#0 1 2 3 4 5 6 7 8  9 10 11 12 13 14 15 16
                if column != 16:
                    if column % 2 == 0: #0 2 4 6 8 10 12 14
                        practicalColumn = int(column / 2 - 7)  #0 1 2 3 4 5 6 7
                        print(field[practicalColumn][practicalRow], end='')
                    else:
                        print('|', end='')
                else:
                    print(field[practicalColumn][practicalRow])
        else:
            print('-----------------')



player = 1
drawField = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
board(drawField)
while True:
    print(f'Player turn {player}')
    moveColumn = int(input('Please enter the column [1 - 7]: '))
    length = len(drawField[moveColumn])
    cont = 0
    for c in range(6):
        if drawField[moveColumn][c] in 'X' and not ' ':
            print('There is no available space. Please enter another column.')
    if player == 1:
        for l in range(length - 1, -1, -1):
            if cont == 0:
                if drawField[moveColumn][l] == ' ':
                    drawField[moveColumn][l] = 'X'
                    cont += 1
                    player = 2

    if player == 2:
        for c in range(length - 1, -1, -1):
            if cont == 0:
                if drawField[moveColumn][c] == ' ':
                    drawField[moveColumn][c] = 'O'
                    cont += 1
                    player = 1

    board(drawField)




