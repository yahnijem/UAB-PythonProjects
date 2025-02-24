from turtle import*
import numpy as np

print("**Exercise 1**")
def draw_square(n):
    setheading(0)
    for i in range(4):
        forward(n)
        left(90)

def draw_triangle(n):
    setheading(0)
    for i in range(3):
        forward(n)
        left(120)

def tHouse(n1):
    up()
    color("black")
    goto(0,0)
    down()

    draw_square(n1)

    up()
    forward(n1/4)
    down()
    draw_square(n1/2)

    up()
    back(n1/4)
    left(90)
    forward(n1)
    down()

    draw_triangle(n1)

    up()

tHouse(80)

print("**Exercise 2**")
def twoDmatrix(n2,m):
    assert type(n2) == int and n2>=1 and n2<=10
    assert type(m) == int and m>=0 and m<=90

    startM=0

    while(startM <= m):
        for i in range(n2):
            if (startM <= m):
                print(f'{startM:4}', end = "")
                startM += 1
        print()

twoDmatrix(6,21)
print()

print("**Exercise 3**")
def armstrongChecker(a):
    armstrong_value=0
    change_a= a

    while(change_a > 0):
        digit = change_a % 10
        armstrong_value += digit**3
        change_a //= 10
    return armstrong_value == a

print (armstrongChecker(371))

print("**Practice Problem**")
"""
    Grabs the company name in an email
"""
def cEmail(s1):
    at_sign= 0
    period= 0
    company_name= ""

    for i in range(len(s1)):
        if s1[i] == '@':
            at_sign = i
            break

    for j in range(at_sign+1, len(s1)):
        if s1[j] == '.':
            period = j
            break
    
    for c in range(at_sign + 1, period):
        company_name += s1[c]
    
    return company_name

print(cEmail("yjemison@uab.edu"))
print(cEmail("oldguy123@amazon.com"))

print("**Problem 2**")
def basicStats(npArray):
    mean= np.mean(npArray)
    standard_deviation= np.std(npArray)
    variance= np.var(npArray)
    return [mean, standard_deviation, variance] #is this what you mean by return a list[ ]

print(basicStats([0,1,2,3,4,5]))

done() #for the turtle function at the beginning


