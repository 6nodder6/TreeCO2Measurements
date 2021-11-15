TreeName = input("What is the name of the tree? ")
valid = False
while valid != True:
    while True:
        try:
            TreeDiam = float(input("What is the diameter of the tree in centimeters? "))
            TreeHeight = float(input("What is the height of the tree in meters? "))
            TreeNumber = int(input("How many trees are there? "))
            break
        except:
            print("I'm sorry but one of your inputs is invalid. Please make sure that your total number of trees is a whole number, and that your diameter and height are numbers.")
    if TreeDiam < 2 or TreeHeight < 0.2 or TreeNumber <= 0:
        print("I'm sorry but you have entered a number that is too small! Please ensure that the diameter of the tree is greater than 2cm and the height is greater than 0.2m")
    else:
        valid = True
def calcGW():
    global GreenWeight
    if TreeDiam < 28:
        GreenWeight = 0.0577*TreeDiam*TreeDiam*TreeHeight
    elif TreeDiam >= 28:
        GreenWeight = 0.0346*TreeDiam*TreeDiam*TreeHeight
    return
def calcCarbon():
    global Carbon
    Carbon = GreenWeight * 0.25
    return
def calcCO2():
    global CO2PerTree
    CO2PerTree = Carbon * 3.67
    return
def calcForest():
    global CO2ForForest
    CO2ForForest = CO2PerTree * TreeNumber
    return
calcGW(); calcCarbon(); calcCO2(); calcForest(); 
print("The following information corrisponds to the ",TreeName," tree:", sep="")
print("The greenweight mass is ",round(GreenWeight,4)," KG. The carbon of is ",round(Carbon,4),". The CO2 for the ",TreeName," tree is ",round(CO2PerTree,4),". The total CO2 for the entire forest is ", round(CO2ForForest,4),". All these values have been rounded to the nearest four decimals.", sep="")