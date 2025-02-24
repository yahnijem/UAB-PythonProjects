""" A cashier fuction that take user imput to compute the total price
"""
def cashier(c):
    total=0
    for i in range (c):
        print("For item "+ str(i+1))
        price= float(input("Enter the price: "))
        tax= float(input("Enter the tax rate: "))
        tax= tax/100
        price=price+(price*tax)
        total=total+price
    print ("Your total price is " + str(total))
cashier(2)
cashier(3)

########################

""" Star design that puts a number of stars per row.
"""
def starline(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print("*", end=" ")
        print ()
starline(7)
starline(3)

########################
""" Pair matching index from a string
"""
def stringPair(s1, s2):
    for i in range(len(s1)):
        char1=s1[i]
        char2=s2[i]
        print(char1,char2)
stringPair('abc', 'xyz')

########################

def smallestSum (L1,L2):
    smallsum= L1[0]+L2[0]
    for i in range (len(L1)):
        startingsum= L1[i]+L2[i]
        if startingsum < smallsum:
            smallsum=startingsum
    return smallsum
smallestSum([0, 1, 8, 12, 65, 34534],[120, 2, 4, 55, 323, 12])

########################

def stringBlenders(s1):
    for char in s1:
        if len(s1)<3:
            return " "
        else:
            newstring= str(s1[0:3])+str(s1[-3:])
            return newstring
print(stringBlenders('uabcs2019'))
print(stringBlenders('uab'))
print(stringBlenders('ua'))