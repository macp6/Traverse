import fitness

# Distance pre calculation
# Find in dictionary using city number
def preCal (coordinates):
    num = 0
    distanceDictionary = {}
    for index in range(len(coordinates)): # 0-28
        tempD = {}
        for x in range(len(coordinates)): # 0-28
            tempD[coordinates[x][0]] = fitness.distanceBetween(coordinates[index], coordinates[x])

        distanceDictionary[coordinates[index][0]] = tempD
    print("Pre Calculation - Done")

    return distanceDictionary
