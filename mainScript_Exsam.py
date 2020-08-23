# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:32:12 2015

@author: Christian (s144207), Frederik (s145418) og Kresten (s144204)
"""

import numpy as np
import math
import matplotlib.pyplot as plt

# Lindenmayer Iteration
def LindIter(System, N):
    
    # We start by determain if it is Koch or Sierpinski we shall run.
    
    if System == "Koch":
        # We start with "S" as it should start.
        LMString = "S"
        # We make a array with symbol that shall change and
        # what they change to, because ti easier to access in the code.
        sym = np.array(["S", "SLSRSLS"])
        for i in range(N):
            # We break the string into a array,
            # because it is easier to access and change this way
            LMArray = list(LMString)
            for j in range(np.size(LMArray)):
                # We then checks if there is a "S",
                # if it is a "S" we change it to "SLSRSLS".
                if LMArray[j] == sym[0]:
                    LMArray[j] = sym[1]
                # If is isn't a "S", then it most be a "L" or "R",
                # and in that case we shall not change it.
                else:
                    LMArray[j] = LMArray[j]
            # We now join the array to a string so that it can be returned,
            # and so we can split it agian.
            LMString = "".join(LMArray)
            
    elif System == "Sierpinski":
        # If it on the other hand is Sierpinski we shall run,
        # we do the same thing, and opperate according to PDF file.
        LMString = "A"
        sym = np.array(["A", "BRARB", "B", "ALBLA"])
        for i in range(N):
            
            LMArray = list(LMString)
            
            for j in range(np.size(LMArray)):
                
                if LMArray[j] == sym[0]:
                    LMArray[j] = sym[1]
                elif LMArray[j] == sym[2]:
                    LMArray[j] = sym[3]
                else:
                    LMArray[j] = LMArray[j]
            
            LMString = "".join(LMArray)
            
    return LMString

# Translation to turtle graphics commands
def turtleGraph(LMString):
    # Create the array and varabls
    turtleCommands = np.array([1,0])
    deg = 0  
    if LMString[0] == "S":
        St = True
        AB = False
        leng = 1
    elif LMString[0] == "A" or LMString[0] == "B":
        AB = True
        St = False
        leng = 1/2
    for i in range(len(LMString)):
        # If it is a line then add length to the array,
        # and if it is "L" or "R" add the angle of the next line
        if St:
            if LMString[i] == "L":
                deg = (2/6) * math.pi
                turtleCommands = np.append(turtleCommands, deg)
            elif LMString[i] == "R":
                deg = - (4/6) * math.pi
                turtleCommands = np.append(turtleCommands, deg)
            else:
                turtleCommands = np.append(turtleCommands, leng)
        if AB:
            if LMString[i] == "L":
                deg = (2/6) * math.pi
                turtleCommands = np.append(turtleCommands, deg)
            elif LMString[i] == "R":
                deg = - (2/6) * math.pi
                turtleCommands = np.append(turtleCommands, deg)
            else:
                turtleCommands = np.append(turtleCommands, leng)
    turtleCommands = np.append(turtleCommands, 0)
    return turtleCommands
    
# Turtle graphics plot function
def turtlePlot(tCom):
    plt.close("all")
    # Make two arrays x- and y-coordinats, and direction,
    # according to initial point and initial direction.
    X = np.array([0])
    Y = np.array([0])
    D = np.array([1,0])
    
    i = 0
    
    while i < np.size(tCom):
        # Calculate the direction according to the equation given.
        d = np.array([[math.cos(tCom[i+1]), - math.sin(tCom[i+1])],
                      [math.sin(tCom[i+1]), math.cos(tCom[i+1])]])
        D = np.dot(d,D)
        
        # Calculate the point according to the equation.
        x = np.array([X[np.size(X) - 1], Y[np.size(Y) - 1]]) 
        x = x + (tCom[i] * D)
        
        X = np.append(X, x[0])
        Y = np.append(Y, x[1])
        
        i += 2
    
    plt.figure()
    plt.plot(X,Y,"b-")
    plt.show()
    plt.draw()
# Main script
running = True
LindenmayerString = ""
while running:
    # Gives the user options.1
    print("1. Choose the type of Lindenmayer" 
    + " system and the number of iterations.")
    print("2. Generate plots.")
    print("3. Quit.")
    
    while True:
        # The code will only proceed if the user 
        # insert a valid number.
        try:
            option = int(input("Enter a valid number: "))
            if 1 <= option <= 3:
                break
        except ValueError:
            print("Not valid number. Please try again.")
    
    if option == 1:
        # Gives the user options.
        print("Choose a Lindenmayer system")
        print("1. Koch curve")
        print("2. Sierpinski triangle")
        
        while True:
            # The code will only proceed if the user 
            # insert a valid number.
            try:
                option = int(input("Enter a valid number: "))
                if 1 <= option <= 2:
                    break
            except ValueError:
                print("Not valid number. Please try again.")
        while True:
            # The code will only proceed if the user 
            # insert a valid number.
            try:
                N = int(input("Choose numer of iterations: "))
                break
            except ValueError:
                print("Not valid number. Please try again.")
        # Runs the LindIter function according to the user input.
        if option == 1:
            LindenmayerString = LindIter("Koch", N)
        else:
            LindenmayerString = LindIter("Sierpinski", N)
        print("Lindenmayer system, succesfully created")
    
    elif option == 2:
        # Checks if the user have run Lindenmayer system, if not,
        # then the user can't access the function
        if LindenmayerString == "":
            print("404 Error: Lindenmayer system not found")
        else:
            # Runs the turteleGraph and turtlePlot, so we get a plot.
            turtleCommands = turtleGraph(LindenmayerString)
            turtlePlot(turtleCommands)
        
    elif option == 3:
        # Close the system
        print("Shutting down")
        running = False
