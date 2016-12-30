# -StartPython.py *- coding: utf-8 -*-
"""
Spyder Editor

#%% starts a new cell. Use second green triangle to run just the cell that
your mouse has last clicked in (or Ctrl-Enter on a PC or Command-Return on a
Macintosh or Menu>Run>Run Cell)
"""
#%%
def hello():
    print("Hello, world!")

#%%
def myname():
    print("My name is Bill")
    
#%%
def ourschool():
    print("Coursera is our school")

#%%  
  
""" This will run forever. In this case Ctrl-C will stop it, but sometimes
that doesn't work. In that case, click away IP Console to stop; click yes to 
kill kernel. Open a new IPConsole on the Console menu to restart """
#%%
def forever():
    while True:
        pass
  
#%%
def name():
    """This is Documentation"""
    #This is a Comment
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    print("Your Name is:", fname, lname)
#%%
def absolutevalue(num):
    if num < 0:
        print("The absolute value of", num, "is", num*-1)
    elif num > 0:
        print("The absolute value of", num, "is", num)
    else:
        print("The absolute value of 0 is 0")
    
#%%
def inches_to_feet(inches):
    feet = inches//12
    inches = inches % 12
    print(inches, "inches is", feet,"feet and", inches, "inches")
#%%
def countdown():
    count = 10
    while count > 0:
        print(count,end=" ")
        count = count - 1
    print()
    print("BLASTOFF!")
#%%
def countdown1():
    #count = 10
    for count in range(10, 0, -1):
        print(count, end= " ")
    print()
    print("BLASTOFF!")
#%%
"""Working With Lists"""

"""Lists in python can be a combination of integers, characters & strings"""
def createMlist(): #Manual List Creation
    intList = [1,2,3,4,5,6]
    strList = ['a', 'b', 'c']
    stringList = ["my","name","is"]
    comboList = ["string",24, 'a', -3]
    
"""list[2:4] --> Prints elements at position 2, 3"""
"""intList[:3] --> Prints elements till position 3 excluding 3 [1, 2, 3]"""
"""intlist.append(7) --> appends 7 to the end"""
#%%
"""Average of numbers in a list"""
def averagelist(lis):
    sum_ = 0
    #count = 0
    for val in lis: #Iterate over the list
        sum_ += val
        #count += 1
    print("The average of given list is", sum_/len(lis))
#%%
"""Create a List using the range() function and converting to a list"""
def createAutoList():
    print(list(range(2, 21, 3)))
#%%
""" Accessing Lists Inside a List """
def printlist():
    newList = [["CMPE200", 100], ["CMPE220", 90], ["CMPE240", 80]]
    print(newList[0]) #Prints ['CMPE200', 100]
    print(newList[1][1]) #Prints 90

#%%
""" Importing & Working with Python Libraries """
import random

print (random.random()) #Prints a random real number between 0 and 1

print (random.randint(4, 6)) #Prints random number in range 4, 6 including 4 & 6

""" random.choose(list) for choosing a random position from a list"""
#%%
""" Working With Tuples """
def createTuple():
    tup = ('a', 'b', 'c')
    """ Tuples are immutable"""
    """ Ordered Data type. i.e., tup[0] gives 'a' """
#%%
""" Working with Dictonaries """
def createDictonary():
    dic = {"key":"Value", "Key1":"Value1"}
    """ Un ordered Data type. i.e., dic[0] will not work."""
    """ dic["key"] gives 'Value' """
    """ items, keys, values """
    """ items are tuples. e.g., ('key', 'value')"""
    for item in dic.items():
        print(item) #prints Tuple
    
    for key, value in dic.items():
        print(key,"      ", value) #Key Value Pair
    
    for value in dic.values():
        print(value) #Prints Values of all keys

    for key in dic.keys():
        print(key) #Prints Keys
    
    dic["key2"] = "Value2" #Appends New Tuple to Dictonary
    print (dic)
#%%
""" Working with files """
def readfile(fileName):
    infile = open(fileName) #open file
    
    for line in infile:
        print(line, end="") #print each line

    infile.close();
#%%

def copyfile(fileName, newFile):
    infile = open(fileName)
    outfile = open(newFile, 'w')
    
    for line in infile:
        outfile.write(line)
        
    infile.close()
    outfile.close()
#%%

def createFile(fileName, name, age, major):
    outfile = open(fileName, 'w')
    
    outfile.write("My Name is " + name + "\n")
    outfile.write("My Age is " + str(age) + "\n")
    outfile.write("My Majoe is " + major + "\n")
    
    outfile.close()
    

#%%
def count_words(filename):        
    text_file = open(filename)
    words_dic = {}
    
    for line in text_file:         # step through each line in the text file
        for word in line.lower().split():   # split into a list of words
            word = word.strip("'?,.;!-/\"") # strip out the stuff we ignore
            if word not in words_dic:
                words_dic[word] = 0      # add word to words with 0 count
            words_dic[word] = words_dic[word] + 1    # add 1 to the count
    
    text_file.close() 
                   
    # Sorts the dictionary words into a list and then print them out
    print("List of words in the file with number of times each appears.")
    word_list = sorted(words_dic)
    for word in word_list:
        print(words_dic[word], word)

#%%
import csv
def readCSVFile(filename):
    
    infile = open(filename)
    
    for row in csv.reader(infile):
        #print(row) #Prints a Tuple
        for i in range(0, len(row) -1 ):
            print(row[i])
    
    infile.close()
#%%
import csv

def writeCSVFile(filename):
    file = open(filename, 'w', newline="")
    
    while True:
        newName = input("Enter Your Friend's Name: ")
        if newName =="":
            break
        newPhone = input("Enter His Phone Number: ")
        
        print(newName)
        print(newPhone)
        
        newLine = []
        newLine.append(newName)
        newLine.append(newPhone)
        csv.writer(file).writerow(newLine)
        
    file.close()
#%%
    
    
    
    
    
    
