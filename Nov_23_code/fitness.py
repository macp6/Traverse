import math

def sumOfDistance(population):
    fitnesses = []
    for individual in population:
        currentFitness = 0
        #get fitness
        i = 0
        while i < len(individual) - 1:
            currentFitness += distanceBetween(individual[i], individual[i+1])
            i += 1
            #print(currentFitness)

        currentFitness += distanceBetween(individual[i], individual[0])
        #print("break")
        fitnesses.append(round(currentFitness,2))

    return fitnesses

def distanceBetween(node1, node2):
    print("node1: ")
    print(node1)
    xDif = abs(node1[1] - node2[1])
    yDif = abs(node1[2] - node2[2])

    totalDistance = math.sqrt(xDif*xDif + yDif*yDif)
    return totalDistance


def fitnessCorrection(fitnessArray):
    newFitness = []
    minFitness = min(fitnessArray)
    buffer = (minFitness - (max(fitnessArray) - minFitness)) - 1
    print(minFitness)
    for fit in fitnessArray:
        fit = minFitness - (fit - minFitness)
        fit -= buffer
        newFitness.append(round(fit, 2))

    return newFitness
