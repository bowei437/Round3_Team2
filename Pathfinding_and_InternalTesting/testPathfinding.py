#!/usr/bin/python

"""
ECE 4574 Assignment 5 | Round 2 Team 2
Internal Testing Suite
Video found at: https://youtu.be/XuV_3L8GiAM


Testing function to determine if the shortest path was acheived on different graphs
"""

from pathfinder import *


#Used to actually go through computed program and find if values match
# Enable is set to 0 as these functions overwrite the data
def is_shortest_path(json_message, enable): 

    path = pathfind_from_json(json_message, 0) #enable set to 0
    #pprint(path)
    weight = path["path_cost"]
    print("Pathfinding found in: {0} steps".format(weight))

    if enable == 1:
        pprint(path["coordinates"])
        print("length of path: {0}".format(len(path["coordinates"])))

    
    while len(path["coordinates"]) > 1:
        decrementer = int(1 + (weight - 1) / 10) #decrementer moves at an expedited pace to move through the test faster
        src = path["coordinates"][decrementer]
        weight = weight - decrementer
        json_message["robots"][0]["coordinates"]["x"] = src["x"]
        json_message["robots"][0]["coordinates"]["y"] = src["y"]
        path = pathfind_from_json(json_message, 0) #enable set to 0
        if enable == 1:
            print("\nBest Path Weight " + str (path["path_cost"]))
            print("src value is: {0}".format(src))
            print("\nWEIGHT:{0}\n PATH COST:{1}".format(weight, path["path_cost"]))


        if weight != path["path_cost"]:
            #print("FAILLLLLLLLL")
            return False

    #pprint(path)
    return True

#Unit testing program that goes through each test case sequentially
def unittest(fname, enable):

    with open(fname, 'r') as data_file:    
        data = json.load(data_file)

    tempPath = pathfind_from_json(data, 1) #Get test data output from pathfinding algo to see if input is valid
    
    # Block below used to check if input is valid. Used when data provided is not correct in dimensions or solveability
    if tempPath["path_cost"] is None:
        tempResult = True
        print("\nInput JSON File not valid\nTest for valid structure returned correctly so test is pass")
        
    else: # ** Else means data is pure and can now run Unit Test **
        tempResult = True
        print("Pathfinding found in: {0} steps".format(tempPath["path_cost"]))
        #tempResult = is_shortest_path(data, enable) # Run Unit Test function and store True / False result into tempResult variable
    
    # Conditional check of statement to assign string of PASSED or FAILED
    if tempResult is True:
        passfail = "PASSED"
        retval = True
    else:
        passfail = "FAILED"
        retval = False

    print("\n--- RESULT: {0} ---\n--- TEST {1} COMPLETE! ---\n".format(passfail, TestNum))
    
    #return True
    return retval

######################## Main program Below ######################

print("Running Internal Testing Suite\n--------------------------------------------------------")

#Global values
TestResult = [] # Default List Creation contains the True or False results of each test run
enable = 0 # default value of if to print extra data or not
"""
#### TEST DEMO #####################################################################################
# Small Demo map of 20x20 (SQUARE) with NO obstacles
inputfile = 'testdemo.json'
TestNum = 0 # Current Test Number

uResult = unittest(inputfile, 1) # Run unit test and store result
TestResult.insert(TestNum,uResult) # Insert tempResult variable into array location TestNum

"""

"""
#### TEST 0 #####################################################################################
#Large map with high computation
inputfile = 'test0.json'
TestNum = 0 # Current Test Number

uResult = unittest(inputfile, 0) # Run unit test and store result
TestResult.insert(TestNum,uResult) # Insert tempResult variable into array location TestNum

"""
#### TEST Default #####################################################################################
#ERROR Test. Should not run and give an error output
inputfile = 'test4.json'
TestNum = 1 # Current Test Number

uResult = unittest(inputfile, 0) # Run unit test and store result
TestResult.insert(TestNum,uResult) # Insert tempResult variable into array location TestNum

"""
#### TEST Default #####################################################################################
#ERROR Test. Should not run and give an error output
inputfile = './testIntermittent.json'
TestNum = 1 # Current Test Number

uResult = unittest(inputfile, 0) # Run unit test and store result
TestResult.insert(TestNum,uResult) # Insert tempResult variable into array location TestNum

#### TEST Default #####################################################################################
#ERROR Test. Should not run and give an error output
inputfile = './testIntermittent2.json'
TestNum = 1 # Current Test Number

uResult = unittest(inputfile, 0) # Run unit test and store result
TestResult.insert(TestNum,uResult) # Insert tempResult variable into array location TestNum
"""

#########################################################################################3##

print("\n-----------------------------\nFINAL RESULTS:\n")
i = 0

while i <len(TestResult):
    if TestResult[i] is True:
        print("\tTEST{0} = PASSED".format(i))
        i += 1
    else:
        print("\tTEST{0} = FAILED".format(i))
        i += 1
        
print("\n-- Program Finished\n")
### Program Finish
#print(TestResult)



