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











