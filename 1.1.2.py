solution = int(input("Input a number between 1 and 100: "))
print("Solution: ",solution)

from random import randint
estimation = randint(1, 100)
print("Estimation: ",estimation)

solved = 0

def compare(a,b):
    if a - b == 0:
        return 0
    elif a < b:
        return 1
    elif a > b:
        return -1

def lookup(a,b):
    while compare(a,b) != 0:
        a += compare(a,b)
        print(a)
    print("Solution is : {}".format(a))

lookup(estimation,solution)