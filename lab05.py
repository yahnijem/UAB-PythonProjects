def evenNumbers(x):
    evens=" "
    for i in range (0,x+1,2):
        evens+=str(i)+ " "
    print(evens)
evenNumbers(12)

def factorial(f):
    product= 1
    while(f>1):
        product *=f
        f-=1
    return product
factorial(6)

import random 
def randNumbers(r):
    total=0
    for i in range (r):
        temp=random.randint(0,9)
        total += temp
        print (f"{i+1}.Random Number: {temp}")
    average =total/r
    print(f"The average of these random numbers is {average}")
randNumbers(5)

def oddNumbers(x):
    odds=" "
    for i in range (x,100):
        if i%2 !=0:
            odds+=str(i)+ " "
    print(odds)
oddNumbers(90)

def fibonacci(n):
    a=0
    b=1
    for i in range (0,n):
        print (a, end=" ")
        c=a+b
        a=b
        b=c
fibonacci(10)