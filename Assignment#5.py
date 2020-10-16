

def findprime(num):
    contdiv = 0
    for n in range(1, num + 1):
        if num % n == 0:
            contdiv += 1
    if contdiv == 2:
        return True



for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0:
        print('Fizz')
    elif findprime(number):
        print('Prime')
    else:
        print(number)


