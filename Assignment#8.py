myMusicFile = open('music.txt', 'w')
tempData = [['Whitney Huston', 'Always Love You', '1992'], ['Ed Sheeran', 'Photograph', '2020'], ['Maroon 5', 'Memories', '2019']]
for lst in tempData:
    for data in lst:
        myMusicFile.write(data)
        myMusicFile.write(' ')
    myMusicFile.write('\n')
myMusicFile.close()

myCountriesFile = open('countries.txt', 'w')
TempData = ['Mozambique', 'U.K.', 'Germany', 'Brazil']
for data in TempData:
    myCountriesFile.write(data)
    myCountriesFile.write(' ')
    myCountriesFile.write('\n')
myCountriesFile.close()

fileName = str(input('Please Enter the file Name: ')).strip()
fileSet = {'music', 'countries'}
while True:
    if fileName not in fileSet:
        fileName = open('fileData.txt', 'w')
        inputData = str(input('Please enter the text you want to write to the file: '))
        fileName.write(inputData)
        fileName.close()
        break
    else:
        print('What would you like to do? \n'
              '[ A ] Read the file\n'
              '[ B ] Delete the file and start over\n'
              '[ C ] Append the file\n'
              '[ D ] Replace a single line\n'
              '[ E ] Quit')
        user = str(input('Your Option: ')).strip().upper()[0]
        if user in 'A':
            fileNameInput = open(f'{fileName}.txt', 'r')
            for line in fileNameInput:
                print(line)
            fileNameInput.close()

        elif user in 'C':
            moreText = str(input('Please enter more text in the file: ')).strip()
            fileNameInput = open(f'{fileName}.txt', 'a')
            fileNameInput.write(moreText)
            fileNameInput.write(' ')
            fileNameInput.write('\n')
            fileNameInput.close()
            fileNameInput = open(f'{fileName}.txt', 'r')

        elif user in 'D':
            lineNumber = int(input('Please enter the line number: '))
            moreText = str(input('Please enter the text: '))
            fileNameInput = open(f'{fileName}.txt', 'r+')
            fileNameList = []
            for line in fileNameInput:
                fileNameList.append(line)
            fileNameList[lineNumber - 1] = moreText
            for data in fileNameList:
                fileNameInput.write(data)
                fileNameInput.write(' ')
                fileNameInput.write('\n')
            fileNameInput.close()
            fileNameInput = open(f'{fileName}.txt', 'r')
            for line in fileNameInput:
                print(line)
            fileNameInput.close()

        elif user in 'E':
            break


