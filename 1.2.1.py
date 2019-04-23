def factorielle(a):
    result = 1

    if a < 0:
        return "Incorrect"
    elif a == 0:
        return 1
    elif a == 1:
        return 1
    elif a >= 2:
        while a > 1:
            result *= a
            a -= 1
        return result

print(factorielle((10)))