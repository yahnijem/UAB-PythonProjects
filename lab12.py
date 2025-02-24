print("*** Exersice 1 ***")
def hailstone(n2):
    while (n2 != 1):
        if n2 %2 != 0:
            n2= ((n2*3)+1)
        else :
            n2=(n2//2)
        
        if n2 != 1:
            print(n2, end=", ")
        else:
            print(n2)

hailstone(3)
hailstone(6)
hailstone(7)
#####################################
print("*** Exersice 2 ***")
def keysToRemove(d1,l1):
    for i in range(len(l1)):
        if l1[i] in d1:
            del d1[l1[i]]
        return d1
    
print(keysToRemove({"FirstName": "Mark", "LastName": "Zuckerberg", "Salary": 2000000,"City": "Palo Alto", "Company":"Facebook"}, ["Salary", "Company"]))
#####################################
print("*** Exersice 3 ***")
def animalLegs(d2):
    animal_leg_counts={"chickens": 2, "cows": 4, "rabbits": 4, "dogs": 4}
    total_legs= 0

    for animal in d2:
        total_legs += animal_leg_counts[animal] * d2[animal]
    
    return total_legs

print(animalLegs({"chickens": 10, "rabbits" : 5}))
print(animalLegs({"dogs": 10, "chickens": 5, "cows" : 5}))
                

