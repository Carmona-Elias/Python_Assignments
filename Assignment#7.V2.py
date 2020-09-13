meta_Data = {"Artist": "Louis Armstrong",
             "Birthday": "August, 4, 1901",
             "City": "New Orleans, Louisiana, U.S.",
             "Genre": "Jazz",
             "Title": "Wonderful World",
             "Duration": "2.21",
             "Author": "Bob Thiele and George David Weiss",
             "Release": "1967",
             "Label": "ABC"
             }


while True:
    user = str(input('Which item would you like to access?\n '
                     'Type "Quit" to Exit: '))
    if user in 'Quit':
        break
    for ke, va in meta_Data.items():
        if ke in user:
            print(f'{ke}: {va}')


def guess(key, value):
    aux = False
    for k, v in meta_Data.items():
        if k in key and v in value:
            aux = True
    if aux:
        return True
    else:
        return False


print('Try to guess the value of any key in the Dictionary')
ky = str(input('Type in the key: ')).strip()
vl = str(input('Type in the value: ')).strip()
print(guess(ky, vl))
