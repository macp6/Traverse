import random

# Multi Pointer Selection
def MPS(fitnessArray, matingPoolSize):
    selectedToMate = []
    cumulProp = []
    fitSum = sum(fitnessArray)
    cumulProp.append(fitnessArray[0]/fitSum)

    for x in range(1, len(fitnessArray)):
        cumulProp.append(cumulProp[x-1] + fitnessArray[x]/fitSum)

    rv = random.uniform(0, 1/matingPoolSize)
    x = 0
    while len(selectedToMate) < matingPoolSize:
        while rv <= cumulProp[x]:
            selectedToMate.append(x)
            rv = rv + 1/matingPoolSize
        x += 1
    return selectedToMate
