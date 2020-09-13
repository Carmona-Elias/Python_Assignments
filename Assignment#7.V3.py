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

for ke, va in meta_Data.items():
    print(f'{ke}: {va}')


def guess(key, value):
     if key in meta_Data:
        if value == meta_Data[key]:
            return True
        else:
            return False


print('Try to guess the value of any key in the Dictionary')
ky = str(input('Type in the key: ')).strip()
vl = str(input('Type in the value: ')).strip()
print(guess(ky, vl))
