
def firstpo(n) :

    position = 1
    mask = 1

    while (not(mask & position)) :

        mask = mask << 1
        position += 1

    return position

n = int(input("enter a number"))
print(firstpo(n))
