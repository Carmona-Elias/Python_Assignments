myUniqueList = list()
myLeftovers = list()


def add(element):
    if element not in myUniqueList:
        myUniqueList.append(element)
        return True
    else:
        myLeftovers.append(element)
        return False


print(add('Carmona'))
print(add('Elias'))
print(add('Carmona'))
print(add(23))
print(add('Cheila'))
print(add('Elias'))
print(add(23))
print(add(29))

print(f'Elements added to myUniqueList: {myUniqueList}')
print(f'Elements rejected for non-uniqueness: {myLeftovers}')


