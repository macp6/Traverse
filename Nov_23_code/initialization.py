from random import shuffle


def randomization(popSize, coordinatesArray):

    population = []

    for i in range(popSize):

        shuffle(coordinatesArray)
        population.append(coordinatesArray.copy())

    return population