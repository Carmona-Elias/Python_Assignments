# Hangman Game
from random import choice
wordAttempt = []
Attempt = 7
word_list = [
    'wares',
    'soup',
    'mount',
    'extend',
    'brown',
    'expert',
    'tired',
    'humidity',
    'backpack',
    'crust',
    'dent',
    'market',
    'knock',
    'smite',
    'windy',
    'coin',
    'throw',
    'silence',
    'bluff',
    'downfall',
    'climb',
    'lying',
    'weaver',
    'snob',
    'kickoff',
    'match',
    'quaker',
    'foreman',
    'excite',
    'thinking',
    'mend',
    'allergen',
    'pruning',
    'coat',
    'emerald',
    'coherent',
    'manic',
    'multiple',
    'square',
    'funded',
    'funnel',
    'sailing',
    'dream',
    'mutation',
    'strict',
    'mystic',
    'film',
    'guide',
    'strain',
    'bishop',
    'settle',
    'plateau',
    'emigrate',
    'marching',
    'optimal',
    'medley',
    'endanger',
    'wick',
    'condone',
    'schema',
    'rage',
    'figure',
    'plague',
    'aloof',
    'there',
    'reusable',
    'refinery',
    'suffer',
    'affirm',
    'captive',
    'flipping',
    'prolong',
    'main',
    'coral',
    'dinner',
    'rabbit',
    'chill',
    'seed',
    'born',
    'shampoo',
    'italian',
    'giggle',
    'roost',
    'palm',
    'globe',
    'wise',
    'grandson',
    'running',
    'sunlight',
    'spending',
    'crunch',
    'tangle',
    'forego',
 ]


def printMan(pos):
    man = [
        '''
        ----------
                 |
                 |
                 |
                 |
                 |
        -----------------
        ''',
        '''
        -----------
        o         |
                  |
                  |
                  |
                  |
        -------------------
        ''',
        '''
        -----------
        o         |
        |         |
                  |
                  |
                  |
        -------------------
        ''',
        '''
        -----------
        o         |
        |         |
       /          |
                  |
                  |
        -------------------
        ''',
        '''
         -----------
        o         |
        |         |
       / \        |
                  |
                  |
        -------------------
        ''',
        '''
        -----------
        o         |
       /|         |
       / \        |
                  |
                  |
        -------------------
        ''',
        '''
         -----------
        o         |
       /|\        |
       / \        |
                  |
                  |
        -------------------
        ''',
        '''
        -----------
        |         |
        o         |
       /|\        |
       / \        |
                  |
                  |
        -------------------
        '''
    ]
    print(man[-pos])


# Print Blanks
def printBlanks():
    for letter in Player1:
        if letter not in ' ':
            wordAttempt.append('_')
        else:
            wordAttempt.append(' ')
    for pos, item in enumerate(wordAttempt):
        if pos != (len(wordAttempt) - 1):
            print(item, end=' ')
        else:
            print(item)


# Fill Blank spaces
def fillBlanks():
    for pos, letter in enumerate(Player1):
        if letter == Player2:
            wordAttempt[pos] = letter
    for pos, item in enumerate(wordAttempt):
        if pos != (len(wordAttempt) - 1):
            print(item, end=' ')
        else:
            print(item)


print('-'*30)
print(f'{"HANGMAN GAME":^30}')
print('-'*30)
print('Choose the player mode'
      '\n[ 1 ] 1 Player Mode'
      '\n[ 2 ] 2 Players Mode')
PlayerMode = int(input('Please enter Your option: '))
if PlayerMode == 1:
    Player1 = str(input('Type a word: ')).strip().upper()
    print(chr(27) + "[2J")
else:
    Player1 = choice(word_list).upper()
printMan(8)
printBlanks()
while True:
    Player2 = str(input('Try to guess the letters of the word: ')).strip().upper()
    if Player2 in Player1:
        print(chr(27) + "[2J")
        fillBlanks()
    else:
        printMan(Attempt)
        Attempt -= 1
        print(f'{Player2} is not correct! Try again.')
    if '_' not in wordAttempt:
        print('Congratulations!! You Won the Game')
        break
    elif Attempt == 0:
        print(f'Sorry you ran out of attempts the word was {Player1}')
        print('Game Over!!')
        break



