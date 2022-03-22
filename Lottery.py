#Power Ball & Mega Millions
from random import *

def powerBall():
    numbers = []
    for i in range(5):
        numbers.append(randrange(1, 70))
        for j in range(i):
            if numbers[j] == numbers[i]:
                numbers[j] = int(random()*69)+1
    numbers.sort()
    numbers.append(int(random()*26)+1)
    print(numbers)
    print("Power Play?")
    extra()

def megaMillion():
    numbers = []
    for i in range(5):
        numbers.append(randrange(1,71))
        for j in range(i):
            if numbers[j] == numbers[i]:
                numbers[j] = randrange(1,71)
    numbers.sort()
    numbers.append(int(random()*25)+1)
    print(numbers)
    print("Megaplier?")
    extra()

def extra():
    chance = randrange(0,2)
    if chance == 1:
        print("YES")
    else:
        print("NO")

print("Which lottery are you having?")
choose = input("1. Power Ball \n2. Mega Millions  \n3. quit\n")

while choose != 3:
    if choose == '1' or choose == "Power Ball" or \
        choose == "power ball" or choose == "power":
        powerBall()
    elif choose == '2' or choose == "Mega Millions" or \
        choose == "mega millions" or choose == "mega":
        megaMillion()
    elif choose == '3':
        exit()
    print("\n\nWhich lottery are you having?")
    choose = input("1. Power Ball \n2. Mega Millions  \n3. quit\n")