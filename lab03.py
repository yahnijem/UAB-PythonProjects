import math

def bmiCalculator (wt,h):
    bmi= (wt*703.0)/h**2
    return bmi
bmiCalculator(250,72)

#######################

def nMultiplier (n):
    return int(n+n*11+n*111)
n=5
print(nMultiplier(n))
#######################

def simpleGrader (average):
    if average >=70:
        return True
    else :
        return False
average=68
print(simpleGrader(average))

#######################

def volCone(r,h):
    return (math.pi*(r**2)*h)/3

r=1
h=1
print (volCone(r,h))
r=2
h=2
print (volCone(r,h))
r=3
h=2
print (volCone(r,h))
#######################





