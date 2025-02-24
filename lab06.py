"""Computes muliples of three until it reaches the input number 
"""
def mOfThree (n):
    index=0
    while index<n:
        print (index)
        index+= 3
mOfThree(14)
mOfThree(32)

######################
""" Gets user input for words until "done" is typed.
    Done will combine all the previously entered words to make one complete sentence
"""
def sConcatenate():
    result=""
    string=""
    while string!="done":
        string= input("Enter a string:")
        if string == "done":
            break
        else:
            result = result+string+" "
    print(result)
sConcatenate()