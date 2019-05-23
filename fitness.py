import math


def sumOfDistance(population, isAPopulation):

    if (isAPopulation):
        fitnesses = []
        for individual in population:
            currentFitness = 0
            # Get fitness
            i = 0
            while i < len(individual) - 1:
                currentFitness += distanceBetween(individual[i], individual[i+1])
                i += 1
            currentFitness += distanceBetween(individual[i], individual[0])
            fitnesses.append(round(currentFitness, 2))

        return fitnesses
    else: # Is just an individual
        i = 0
        fitnesses = 0
        currentFitness = 0
        while i < len(population) - 1:
            currentFitness += distanceBetween(population[i], population[i+1])
            i += 1
        currentFitness += distanceBetween(population[i], population[0])
        #fitnesses.append(round(currentFitness, 2))
        fitnesses = round(currentFitness, 2)
        return fitnesses

def distanceBetween(node1, node2):
    xDif = abs(node1[1] - node2[1])
    yDif = abs(node1[2] - node2[2])

    totalDistance = math.sqrt(xDif*xDif + yDif*yDif)
    return totalDistance

def fitnessCorrection(fitnessArray):
    newFitness = []
    minFitness = min(fitnessArray)
    #print(str(minFitness) + " index: " + str(fitnessArray.index(minFitness)) + " (printed in fitness)")
    buffer = (minFitness - (max(fitnessArray) - minFitness)) - 1
    for fit in fitnessArray:
        fit = minFitness - (fit - minFitness)
        fit -= buffer
        newFitness.append(round(fit, 2))
    return newFitness

# Sum of Distance using Pre Calculation Dictionary
def preCalSumOfDistance(population, distanceDictionary, isAPopulation):
    if (isAPopulation):
        fitnesses = []
        for individual in population:
            currentFitness = 0
            i = 0
            while i < len(individual) - 1:
                currentFitness += distanceDictionary[individual[i][0]][individual[i+1][0]]
                i += 1
            currentFitness += distanceDictionary[individual[i][0]][individual[0][0]]
            fitnesses.append(round(currentFitness,2))
        print("Pre Calculation sum of distance - Done")

        return fitnesses

    else: # Just a individual
        i = 0
        fitnesses = 0
        currentFitness = 0
        while i < len(population) - 1:
            currentFitness += distanceDictionary[population[i][0]][population[i+1][0]]
            i += 1
        currentFitness += distanceDictionary[population[i][0]][population[0][0]]
        fitnesses = round(currentFitness, 2)

        return fitnesses
