from random import shuffle

# Randomizes the order of the given coordinatesArray
# returns a population of size 'popSize'
def randomization(popSize, coordinatesArray):

    population = []

    for i in range(popSize):

        shuffle(coordinatesArray)
        population.append(coordinatesArray.copy())

    return population
