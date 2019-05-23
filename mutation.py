import random
from random import shuffle

# Picks two random points and 'scrambles' (randomizes) the order of all the values between them
def scrambleMutation(individual):
    newIndividual = individual.copy()
    scramblePortion = []

    point1 = random.randint(0,len(individual))
    point2 = random.randint(0,len(individual))
    while point2 == point1:
        point2 = random.randint(0, len(individual) - 1)

    if point1 < point2:
        for i in range(point2-point1):
            scramblePortion.append(individual[point1 + i])
        scramblePortion = random.sample(scramblePortion, len(scramblePortion))
        for j in range(len(scramblePortion)):
            newIndividual[point1 + j] = scramblePortion[j]

    else:
        for i in range(point1-point2):
            scramblePortion.append(individual[point2 + i])
        scramblePortion = random.sample(scramblePortion, len(scramblePortion))
        for j in range(point1-point2):
            newIndividual[point2 + j] = scramblePortion[j]

    return newIndividual

# Picks two random points in the given individual and swaps them
def randomSwap(individual):
    newIndividual = individual.copy()
    point1 = random.randint(0,len(individual)-1)
    point2 = random.randint(0,len(individual)-1)
    while point2 == point1:
        point2 = random.randint(0, len(individual) - 1)

    temp = newIndividual[point1]
    newIndividual[point1] = newIndividual[point2]
    newIndividual[point2] = temp

    return newIndividual
