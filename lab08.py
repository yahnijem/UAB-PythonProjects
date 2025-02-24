def listCheckAndSort(L):
    newL = []
    for i in range(len(L)):
        if i % 2 == 0 and L[i] >= -20 and L[i] < 20:
            newL.append(L[i])
    lowToHigh = sorted(newL)
    highToLow = sorted(newL, reverse=True)
    return (lowToHigh, highToLow)

print(listCheckAndSort([2, -16, 6, 77, 100, -3, 62, 18, 0, 123, 1, 18, -18]))  

##########################

def finalGrade(classList):
    students = len(classList)
    attend = 0
    exam = 0
    hw = 0
    
    for i in range(len(classList)):
        attend += classList[i][0]
        exam += classList[i][1]
        hw += classList[i][2]
    return (attend/students, exam/students, hw/students)

print(finalGrade([[20, 80, 90], [10, 60, 40], [17, 77, 56], [21, 99, 99]]))  

##########################

def listCompare(L1, L2):
    missing = []
    extra = []

    for i in range(len(L1)):
        if L1[i] not in L2:
            missing.append(L1[i])
    for i in range(len(L2)):
        if L2[i] not in L1:
            extra.append(L2[i])
            
    print("The missing values: ")
    for e in missing:
        print(e)
    print("The extra values: ")
    for e in extra:
        print(e)

listCompare(["a", "b", "c", "d", "e"], ["b", "d", "e", "f", "g"])

##########################

def listCompare2(L1, L2):  
    missing = []
    extra = []

    for i in range(len(L1)):
        if L1[i] not in L2:
            missing.append(L1[i])
    for i in range(len(L2)):
        if L2[i] not in L1:
            extra.append(L2[i])
            
    print("The missing values: ", end="")
    print(",".join(missing))
    print("The extra values: ", end="")
    print(",".join(extra))

listCompare2(["a", "b", "c", "d", "e"], ["b", "d", "e", "f", "g"])  

##########################

def findMinIndex(L):
    imin = 0
    for i in range(1, len(L)):
        if L[i] < L[imin]:
            imin = i
    return imin

print(findMinIndex([3, 6, 20, 2, 12, -4, 20]))  

##########################

def isPrime(n):
    if n <= 1:  
        return False
        
    for num in range(2, int(n**0.5) + 1):
        if n % num == 0:
            return False
    return True  

print(isPrime(11))  
print(isPrime(17))  
print(isPrime(6))   