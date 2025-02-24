def myName (firstName,lastName):
    return firstName+ " "+lastName
print(myName("Yahni","Jemison"))

firstName = "Yahni"
lastName = "Jemison"
print (myName(firstName,lastName))

########################

def myAge (year):
    return 2024-year
myAge(2004)

########################

def myDepartment (department):
    if department == "CS":
        return "Computer Science"
    elif department == "DS":
        return "Data Science"
    elif department == "BIF":
        return "Bioinformatics"
    else:
        return "not an option"
    
print (myDepartment("CS"))
print (myDepartment("DS"))
print (myDepartment("BIF"))
print  (myDepartment("THR"))

########################

def whoAMI (firstName, lastName, year, department):
    name= myName(firstName, lastName)
    age= myAge(year)
    dep= myDepartment(department)
    print("Hello there. My name is"+ " " + name + " "+ "and I am"+ " " + str(age)+ " " + "years old. I work in the"+ " " + dep + " "+ "department")
whoAMI("Yahni", "Jemison", 2004, "CS")

########################

def squareOrNot(length,width):
    if width==length:
        return True
    else:
        return False
squareOrNot(20,5)

########################

def stringChanger(s):
    if (len(s)>=3):
        if s[-3:]=='ing':
            s= s+'ly'
        else:
            s= s+'ing'
    return s
print(stringChanger("staggering"))
print (stringChanger("target"))
print(stringChanger("cs"))
print(stringChanger("camp"))




