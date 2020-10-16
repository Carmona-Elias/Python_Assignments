Month = 'August'
Date = 4
Year = 1901
Duration = 2.21


def Artist():
    print('Louis Armstrong')


def Birthday(month, date, year):
    print(f'Born on {Month} the {Date}th {Year}')


def Song_Title():
    print('Song: Wonderful World')


def MoreThanFive(Duration):
    if Duration > 5.0:
        return True
    else:
        return False


Artist()
Birthday(Month, Date, Year)
Song_Title()
print(f'Duration: {Duration} secs ')
print(f'Duration more than 5 secs: {MoreThanFive(Duration)} ')
