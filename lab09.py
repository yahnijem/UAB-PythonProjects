#Exercise 1
def isSorted(L):
    if L==sorted(L):
        print("Sorted")
    elif L==sorted(L,reverse=True):
        print("Sorted")
    else:
        print("Unsorted")

isSorted([26,8,6,2,1])

#Exercise 2
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

#Exercise 3
def fChecker():
    try:
        openFile = open("testFile", "r")
        firstName = openFile.readline().strip()
        lastName = openFile.readline().strip()
        age = int(openFile.readline().strip())
        print(f"Hello, {firstName} {lastName}. You will be {age + 5} years old in 5 years.")
        openFile.close()
    except FileNotFoundError:
        print("Error: File 'testFile' not found.")
    except ValueError:
        print("Error: Could not convert age to an integer.")

fChecker()

#Practice Problem 1
from turtle import*
def tPolygon(n):
    if n%2==0:
        pencolor("blue")
    else:
        pencolor("black")

    sideLength=n*n
    angle= 360/n
    up()
    goto(0,0)
    down()

    for i in range(n):
        forward(sideLength)
        left(angle)
    return

tPolygon(5)

#Practice Problem 2
def triangleChecker():
    try:
        triSides=open("triangle.txt", "r")

        firstSide= triSides.readline()
        firstSide= int(firstSide.strip())

        secondSide= triSides.readline()
        secondSide= int(secondSide.strip())

        thirdSide= triSides.readline()
        thirdSide= int(thirdSide.strip())

        triSides.close()  # Added file closing

        if (firstSide + secondSide > thirdSide) and (firstSide + thirdSide > secondSide) and (secondSide + thirdSide > firstSide):
            print("The triangle is valid.")
            if firstSide == secondSide == thirdSide:
                print("equilateral")
            elif firstSide == secondSide or firstSide == thirdSide or secondSide == thirdSide:
                print("isosceles")
            else:
                print("scalene")
        else:
            print("The triangle is invalid.")
    except FileNotFoundError:
        print("Error: File 'triangle.txt' not found.")
    except ValueError:
        print("Error: Could not convert sides to integers.")

triangleChecker()

done()
