from random import randint
rand = randint(1, 100)
print(rand)

solved = 0
while solved == 0:
    num = int(input("Guess a number between 1 and 100: "))
    if num == rand:
        print("Bravo! Hidden number was : {}.".format(rand))
        solved = 1
    elif abs(num-rand)<=5:
        if num < rand:
            print("You're VERY close! Hidden number is bigger, try higher than {}.".format(num))
        else:
            print("You're VERY close! Hidden number is smaller, try smaller than {}.".format(num))
    elif abs(num-rand)<=10:
        if num < rand:
            print("You're kind of close... Hidden number is bigger than {}.".format(num))
        else:
            print("You're kind of close... Hidden number is smaller than {}.".format(num))
    else:
        if num < rand:
            print("You're still far... Hidden number is bigger than {}.".format(num))
        else:
            print("You're still far... Hidden number is smaller than {}.".format(num))

