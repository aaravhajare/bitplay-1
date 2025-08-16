
def setnot(n,number) :

    if number & (1 << (n -1)) :
        print("SET")

    else :
        print("NOt SET")

number = int(input("Eneter a number"))
n = int(input("enyer number of bits"))
setnot(n,number)

