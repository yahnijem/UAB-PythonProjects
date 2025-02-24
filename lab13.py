print("*** Exercise 1 ***")
def fileExtention(s):
    """This fuction take the file name and returns the fle extention.
    
    """
    #start from the back of the string and go to the dot
    if '.' in s:
        last_period= s.rindex('.')
        
        if last_period != -1:
            return s[last_period + 1:]
    return ""
print(fileExtention("lab13_103sp19.pdf"))
print(fileExtention("test.docx"))
print(fileExtention("lab.13.cs.103.pdf"))
print(fileExtention("testcase."))
print(fileExtention("testing_testing123"))

############################
print("*** Exercise 2 ***")
def calculate_my_final_grade(lab_grades, hw_grades, bonus_hw_grades, exams):
    midterm= exams[0] #sets the index for the midterm and final
    final= exams[1]

    if midterm < final:
        midterm= final

#makes sure the bonus homework exists
    if bonus_hw_grades is not None:
        lowest_hw_grade= min(hw_grades)
        lowest_index= hw_grades.index(lowest_hw_grade) #finds the index of the lowest homework grade
        if bonus_hw_grades > lowest_hw_grade:
            hw_grades[lowest_index] = bonus_hw_grades #replaces the lowest homework with the bonus hw grade
    
    #take only the highest 10 lab grades
    lab_grades= sorted(lab_grades, reverse=True) #sets the grades from lowest to highest
    lab_grades= lab_grades[:10]

#calculates the average grade
    final_lab_grade= sum(lab_grades)/ len(lab_grades)
    final_hw_grade= sum(hw_grades)/len(hw_grades)
    final_exam_grade= final

#takes the average grades and weighs it by percent and prints the float grade
    final_grade= (0.20* midterm + 0.20*final_lab_grade + 0.30*final_hw_grade + 0.30*final_exam_grade)
    print(final_grade)

    #Letter Grade
    if final_grade > 89:
        grade= "A"
    elif final_grade > 79:
        grade= "B"
    elif final_grade > 69:
        grade= "C"
    elif final_grade > 59:
        grade= "D"
    else:
        grade= "F"

    return grade

lab_grades=[100, 100, 100, 100, 100, 100, 94, 94, 87, 110, 100, 60, 100]
hw_grades= [100, 79, 97, 20, 100]
bonus_hw_grades= 60.0
exams= [87.25, 88]

print(calculate_my_final_grade(lab_grades, hw_grades, bonus_hw_grades, exams))