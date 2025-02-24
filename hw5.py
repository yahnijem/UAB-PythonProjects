import string
from turtle import*
import random
##################################
"""This was a collaborative assignmet. 
   Me and a classmate Cheyenne worked together to create an assignment a turtle and a text fuction.
"""
##################################
print("Mandatory Functions")
def myName():
    return "Yahni Jemison"
def myBlazerID():
    return "yjemison"
print("My name is =", myName(), "and my BlazerId is =", myBlazerID())
""" I worked with Cheyenne Prevost.
    I did Q1 and she did Q2.
    We both worked on debugging eachother's code when a syntax error accured
"""

##################################

print("*** Problem 1 --- Yahni's Code ***")
def summarize_text(text):
    """ This fuction looks a multiline string and returns the total character, words, sentence, the most common word and its frequency.
    This fuction also ignores a list of stop word to be be consider for most common word.

    Step 1: define stop words
    Step 2: Make the passage a single string
    Step 3: Find the total character while ignoring the spaces
    Step 4: Split single string into list of words. 
            Remove puncuations from to make clean words
            Make the word lower case so that same words are only counted once
            Count the total words
    Step 5: Find end sentence puncuations to count total sentences
    Step 6: Define important words to store all non stop wrods
    Step 7: Count amount of times important words accure and make a dictionary for the word and its count
    Step 8: Look at important word dictionary to see which word has the highest count and make it the most common word

    Returns: A summary dictionary of totals and their counts. 
    
    """
    #These are the bonus stop word that we'll need later
    stop_words = ["the", "is", "in", "and", "to", "a", "of", "it", "that", "you", "he", "was", "for",
        "on", "are", "as", "with", "his", "they", "at", "this", "but", "not", "by", "from", "or"]

    #Makes the big text into a single string
    text = text.strip() #Removes spaces from beginning and end
    big_text= " ".join(text.split("\n")) #splits the big text into a list separating every new line before making one big string
    
    #Counts the characters
    total_characters= 0 #starter count
    for char in big_text:
        if not char.isspace(): #making sure the index/char isn't a space
            total_characters += 1
    
     
    words= big_text.split() #Cuts the big text into individual words every space
    cleaned_words= []
    for word in words:
        cleaned_word= word.strip(string.punctuation).lower() #takes away any punctations that might've been included in the split
        cleaned_words.append(cleaned_word) 
    total_words= len(cleaned_words) #Counts total words
    
    #Counts sentences
    total_sentences= 0 #start count
    for char in big_text:
        if char in ".!?":  #check if the sentence has an end punctuation
            total_sentences += 1
    
    #Remove stop words (begining list) so they don't count for most common 
    important_words= []
    for word in cleaned_words:
        if word not in stop_words: #only add to important words if it's not a stop word
            important_words.append(word)
    
    #Count how many times a word appears for most common
    word_counts= {}
    for word in important_words: #only take in account important words
        if word in word_counts:  #If the word is already in the dictionary add to its total
            word_counts[word] += 1
        else:  #if its new start a count at 1
            word_counts[word]= 1
    
    #Find the most common words and how many time its in the big text
    most_common_word= None #start with non since we dont have a common word yet
    word_frequency= 0
        #check at the key(words) and look at its value(count) to find out which key has the highest value
    for word, count in word_counts.items():
        if count > word_frequency:  #if the word cound is higher than the previous replace it as the new highest
            most_common_word= word
            word_frequency= count
    
    #Put everything into a dictionary and return it
    summary = {
        "total_characters": total_characters,
        "total_words": total_words,
        "total_sentences": total_sentences,
        "most_common_word": most_common_word,
        "word_frequency": word_frequency,
    }
    return summary

sampleText_1= """
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do.
Once or twice she had peeped into the book her sister was reading, but it had no pictures or
conversations in it. "And what is the use of a book," thought Alice, "without pictures or conversations?"
"""
print(summarize_text(sampleText_1))

sampleText_2= """
It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want
of a wife. However little known the feelings or views of such a man may be on his first entering a
neighborhood, this truth is so well fixed in the minds of the surrounding families, that he is considered
as the rightful property of someone or other of their daughters.
"""
print(summarize_text(sampleText_2))

##################################

print("*** Problem 2 --- Cheyenne's Prevost Code ***")
def draw_hexagon(t, size):
    #draws the shape of a hexagon
    for i in range(6):
        t.forward(size)
        t.left(60)

def recursive_hexagon(t, size):
    """This function uses Turtle graphics to 
    draw a series of nested hexagons. Each hexagon will have sides of length size, and the function will
    recursively call itself to draw smaller hexagons inside the larger ones. The recursion should stop when
    the side length of the hexagon reaches 4 pixels.
    
    """

    if size <= 4:
        return 
    r= random.random()
    g= random.random()
    b= random.random()
    t.pencolor(r, g, b)

    draw_hexagon(t,size)
    t.up()
    t.forward(2)
    t.right(60)
    t.backward(2/(3**0.5))
    t.left(60)
    t.pendown()

    recursive_hexagon(t,size-2)

t= Turtle()
t.speed("fastest")
t.width(2)

t.penup()
t.goto(0,0)
t.pendown()
size= random.randint(100,200)

recursive_hexagon(t,size)

exitonclick() #We used this to end the turtle instead of done()
