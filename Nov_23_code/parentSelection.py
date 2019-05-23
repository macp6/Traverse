import random

# Multi-pointer selection (MPS)
def MPS(fitnessArray, matingPoolSize):
    selectToMate = []
    cumulProp = []
    fitSum = sum(fitnessArray)
    cumulProp.append(fitnessArray[0]/fitSum)

    for x in range(1, len(fitnessArray)):
        cumulProp.append(cumulProp[x-1] + fitnessArray[x]/fitSum)

    rv = random.uniform(0, 1/matingPoolSize)
    i = 0

    while len(selectToMate) < matingPoolSize:
        while rv <= cumulProp[i]:
            selectToMate.append(i)
            rv = rv + 1/matingPoolSize
        i += 1
    return selectToMate

