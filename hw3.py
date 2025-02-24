def myName():
    return "Yahni Jemison"
def myBlazerID():
    return "yjemison"
print("My Name is =", myName(),"and my BlazerId is =", myBlazerID())

################
def myName():
    return "Yahni Jemison"

def myBlazerID():
    return "yjemison"

print("My Name is =", myName(), "and my BlazerId is =", myBlazerID())

################

def shortenStrings(lst, num):
    newlist = []
    for char in lst:
        if len(char) < num:
            newlist.append(char)
        else:
            newlist.append(char[:num])
    return newlist

print(shortenStrings(["Programming", "is", "fun"], 4))
print(shortenStrings(["Testing", "functions", "in", "Python"], 5))
print(shortenStrings(["A", "short", "test"], 2))

################

def extractUpper(s):
    capital = ""
    for char in s:
        if char.isupper():
            capital = capital + char
    return capital

print(extractUpper("The Quick Brown Fox"))
print(extractUpper("HWORLD"))
print(extractUpper("abcDEFghiJKL"))

################

def indexOfVowels(s):
    vowels = "aeiouAEIOU"  # Fixed: removed commas and added uppercase vowels
    place = []
    for i in range(len(s)): 
        if s[i] in vowels:
            place.append(i)  # Fixed: removed space after place
    return place

print(indexOfVowels("Hello World"))
print(indexOfVowels("Data Science"))
print(indexOfVowels("Python"))

################

def dataTypeChecker(x):
    if type(x) == str:
        return x.upper()
    elif type(x) == list:
        return sorted(x)
    elif type(x) == float:
        return float(x)**2
    elif type(x) == int:  # Added: handle integers separately
        return x**2  # Return integer squared
    else:
        return "Unrecognized data type"  # Fixed: removed str() as it's already a string

print(dataTypeChecker("hello"))
print(dataTypeChecker([3, 1, 2]))
print(dataTypeChecker(5.2))
print(dataTypeChecker(42))
print(dataTypeChecker((3, 4)))

################

def sumOfDigits(n):
    sum = 0
    for i in str(n):
        sum = sum + int(i)
    return sum

print(sumOfDigits(1234))
print(sumOfDigits(29000000))
print(sumOfDigits(10001))