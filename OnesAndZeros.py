
# func tak num

def nofbit(n) :

    ones , zeros = 0,0

    while(n) :

        if n&1 == 1 :
            ones += 1

        else :
            zeros += 1

        # right shift 

        n >>= 1

    print("ones :" , ones , "seros :" , zeros)


n = int(input("Enter a number"))

nofbit(n)