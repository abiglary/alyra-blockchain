def isPalindrome(string):
    temp = string.lower()
    print("passage en minuscules",temp)
    temp = temp.split(' ')
    print("liste de mots",temp)
    temp = ''.join(temp)
    print("recolle les mots",temp)
    temp2 = list(temp)
    print("découpe en liste de caractères",temp2)
    list.reverse(temp2)
    print("inverse l'ordre de la liste de caractères",temp2)
    temp2 = ''.join(temp2)
    print("recolle les caractères", temp2)
    return(temp == temp2)

print(isPalindrome("Ce satrape repart a sec"))