print("Exercise 1")
def listToDict(L1,L2):
    myDict={}

    for i in range (len(L1)):
        myDict[str(L1[i])]= str(L2[i])
    return myDict

L3= [1,2,3]
L4= ['first','second','third']
print(listToDict(L3,L4))


print("Exercise 2")
def dString(s):
    myDict={}
    for i in range(len(s)):
        if s[i] != " ":
            if s[i] in myDict:
                temp=int(myDict[s[i]])
                temp +=1
                myDict[s[i]] =str(temp)
            else:
                myDict[s[i]] =str(1)
    return myDict

print(dString("UAB CS BS"))


print("Exercise 3")
def dMerge(d1,d2):
    for key in d2:
        if key not in d1:
            d1[key]= d2[key]
        else:
            d1[key]= d1[key]+d2[key]
    return d1

d3= {'orange': 500, 'apple': 1100, 'carrot':600}
d4= {'orange': 50, 'apple': 10,'grapes':300}
print(dMerge(d3,d4))