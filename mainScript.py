# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:04:01 2015

@author: Frederik(s145418), Christian(s144207) and Kresten(s144204)
"""
import numpy as np

bacta = np.array([1,2,3,4])
tempmin = 10
tempmax = 60
# der er ikke noget maksimum på growth rate, men 500 burde være 
# tilstrækkeligt stort
growmin = 0
growmax = 500
tfilter = False

# Data load function
def dataLoad(filename):
    # Open the file in to a array
    filein = open(filename, "r")
    lines = filein.readlines()
    l = np.size(lines)
    data = np.empty(0)
    temp = True
    grow = True
    bact = True
    count = 0
    for i in range(l):
        #Convert the i line from the file in to a array 
        values = list(map(float, lines[i].split()))
        #Checks if there is a error and print a error message
        if values[0] < tempmin or values[0] > tempmax:
            #Error temperature
            print("Error: line " + str(i) + ". Temperature is out of range")
            temp = False
        if values[1] < growmin or values[1] > growmax:
            #Error growth rate
            print("Error: line " + str(i) + ". Growth rate is not positive")
            grow = False
        if values[2] not in bacta:
            #Error bacteria
            print("Error: line " + str(i) + ". Unknown bacteria")
            bact = False
        #Sets the vlueas in the matix
        if temp and grow and bact:
            data = np.append(data, values)
            count += 1
        temp = True
        grow = True
        bact = True
    data = np.reshape(data,[count,3])
    return data

# data statistics function
def dataStatistics(data, statistic):
    
    # size of dataset, or rows
    size = np.size(data[:,0])
    # mean temperatur
    meant = np.mean(data[:,0])
    # mean growth rate
    meang = np.mean(data[:,1])
    
    if statistic == 'Mean Temperature':
        result = meant
        
    elif statistic == 'Mean Growth rate':
        result = meang
        
    elif statistic == 'Std Temperature':
        r = (data[:,0]-meant)**2
        result = np.sum(r)/size
        
    elif statistic == 'Std Growth rate':
        r = (data[:,1]-meang)**2
        result = np.sum(r)/size        
        
    elif statistic == 'Rows':
        result = size
        
    elif statistic == 'Mean Cold Growth rate':
        d = data[:,1]<=20.0
        r = np.sum(d)
        s = np.size(d)
        result = r/s
        
    else:
        d = data[:,1]>=50.0
        r = np.sum(d)
        s = np.size(d)
        result = r/s
    
    return result
            
# Data plot funktion
def dataPlot(data):
    import matplotlib.pyplot as plt
    plt.close("all")
    # Data
    d=data[:,2]
        
    # Number of bacteria
    plt.figure()
    plt.hist(d, 4)
    plt.title("Number of bacteria")
    plt.show()
    plt.draw()
    
    # Data
    data = data[np.lexsort(np.fliplr(data).T)]
    d=data[:,2]
    z1 = data[:,0]
    x1 = z1[d==1]
    x2 = z1[d==2]
    x3 = z1[d==3]
    x4 = z1[d==4]
    z2 = data[:,1]
    y1 = z2[d==1]
    y2 = z2[d==2]
    y3 = z2[d==3]
    y4 = z2[d==4]
    
    # Growth rate by temperature
    plt.figure()
    plt.plot(x1, y1, "ro-", label="Salmonella enterica")
    plt.plot(x2, y2, "bo-", label="Bacillus cereus")
    plt.plot(x3, y3, "go-", label="Listeria")
    plt.plot(x4, y4, "yo-", label="Brochothrix thermosphacta")
    plt.legend(loc="lower center")
    plt.title("Growth rate by temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    plt.show()
    plt.draw()
            
# Main script
running=True
data='none'
while running:
    print("1. Load data.")
    print("2. Filter data.")
    print("3. Display statistics.")
    print("4. Generate plots.")
    print("5. Quit.")
    
    while True:
        # her stopper koden hvis input er en string
        try:
            option = int(input("Enter a valid number: "))
            if 1 <= option <= 5:
                break
        except ValueError:
            print("Not valid number. Please try again.")
        
    if option == 1:
        while True:
            try:
                filename = input("Enter a file name: ")
                open(filename, "r")
                break
            except IOError:
                print("404 Error: File not found")
        #det originale dataset som vi ikke modifisere
        data = dataLoad(filename)
    
    elif option == 2:
        if data == 'none':
            print("No file is loaded")
        else:
            print("1. Temperature filter")
            print("2. Growth rate filter")
            print("3. Bacteria filter")
            if tfilter:
                print("4. Remove filter")
            
            while True:
                try:
                    # her stopper koden hvis input er en string
                    optio3 = int(input("Enter a valid number: "))
                    if tfilter:
                        if 1 <= optio3 <= 4:
                            break
                    else:
                        if 1 <= optio3 <= 3:
                            break
                except ValueError:
                    print("Not valid number. Please try again.")
            
            if optio3 == 1:
                #Temperature filter
                while True:
                    try:
                        tempmin = int(input("Set minimum temperature: "))
                        break
                    except ValueError:
                        print("Not valid number. Please try again.")
                while True:
                    try:
                        tempmax = int(input("Set maximum temperature: "))
                        break
                    except ValueError:
                        print("Not valid number. Please try again.")
                tfilter = True
                print("Temperature limit: " + str(tempmin) 
                + " to " + str(tempmax))
            elif optio3 == 2:
                #Growthrate filter
                while True:
                    try:
                        growmin = int(input("Set minimum Groth rate: "))
                        break
                    except ValueError:
                        print("Not valid number. Please try again.")
                while True:
                    try:
                        tempmax = int(input("Set maximum Groth rate: "))
                        break
                    except ValueError:
                        print("Not valid number. Please try again.")
                tfilter = True
                print("Growth rate limit: " + str(growmin) 
                + " to " + str(growmax))
            elif optio3 == 3:
                #Bactaria filter
                bCount = 0
                bRun = True
                bacta = np.empty(0)
                while bRun:
                    if bCount > 0:
                        print("Add another bacteria")
                    else:
                        print("Add a bacteria")
                    print("1. Salmonella enterica")
                    print("2. Bacillus cereus")
                    print("3. Listeria")
                    print("4. Brochothrix thermosphacta")
                    if bCount > 0:
                        print("5. No more bacteria")
                    
                    while True:
                        try:
                            ba = int(input("Chosse a bacteria to include: "))
                            if bCount > 0:
                                if ba == 5:
                                    bRun = False
                                    break
                            elif 1 <= ba <=4:
                                if ba in bacta:
                                    print("Bacteria already selected")
                                    break
                                else:
                                    bacta = np.append(bacta,ba)
                                    bCount += 1
                                    break
                            else:
                                print("Not valid number. Please try again.")
                        except ValueError:
                            print("Not valid number. Please try again.")
            elif optio3 == 4:
                #Remove filter
                bacta = np.array([1,2,3,4])
                tempmin = 10
                tempmax = 60
                growmin = 0
                growmax = 500
                tfilter = False
                print("Filter set to default")
            data = dataLoad(filename)
            
    elif option == 3:
        if data == 'none':
            print("No file is loaded")
        else:
            print("1. Mean Temperature.")
            print("2. Mean Growth rate.")
            print("3. Std Temperature.")
            print("4. Std Growth rate.")
            print("5. Rows.")
            print("6. Mean Cold Growth rate.")
            print("7. Mean Hot Growth rate.")
            
            while True:
                # her stopper koden hvis input er en string
                try:
                    optio2 = int(input("Enter a valid number: "))
                    if 1 <= optio2 <= 7:
                        break
                except ValueError:
                    print("Not valid number. Please try again.")
                
            if optio2 == 1:
                statistic = 'Mean Temperature'
            elif optio2 == 2:
                statistic = 'Mean Growth rate'
            elif optio2 == 3:
                statistic = 'Std Temperature'
            elif optio2 == 4:
                statistic = 'Std Growth rate'
            elif optio2 == 5:
                statistic = 'Rows'
            elif optio2 == 6:
                statistic = 'Mean Cold Growth rate'
            else:
                statistic = 'Mean Hot Growth rate'
                
            print(dataStatistics(data, statistic))
    
    elif option == 4:
        if data == 'none':
            print("No file is loaded")
        else:
            dataPlot(data)
    
    else:
        print("Shutting down.")
        running = False
    
        
                
    