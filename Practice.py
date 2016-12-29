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
