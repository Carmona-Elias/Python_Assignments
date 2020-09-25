
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


player = 1
drawField = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
board(drawField)
while True:
    print(f'Player turn {player}')
    moveColumn = int(input('Please enter the column [1 - 7]: '))
    moveColumn -= 1
    count = countP = 0
    for c in range(6):
        if drawField[moveColumn][c] in 'X' and not ' ':
            print('There is no available space. Please enter another column.')
    if player == 1:
        for l in range(5, -1, -1):
            if count == 0:
                if drawField[moveColumn][l] == ' ':
                    drawField[moveColumn][l] = 'X'
                    count += 1
                    player = 2

    if player == 2:
        for c in range(5, -1, -1):
            if count == 0:
                if drawField[moveColumn][c] == ' ':
                    drawField[moveColumn][c] = 'O'
                    count += 1
                    player = 1

    board(drawField)








