

def tick_tack_board(row, column):
    if row == column and row or column <= 10:
        for r in range(row):
            if r % 2 == 0:
                for c in range(1, column+1):
                    if c % 2 != 0:
                        if c != 5:
                            print(' ', end='')
                        else:
                            print(' ')
                    else:
                        print('|', end='')
            else:
                print('-----')
        return True
    else:
        return False


height = 5
width = 5
print(tick_tack_board(height, width))
