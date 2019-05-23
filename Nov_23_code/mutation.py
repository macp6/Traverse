import random
from random import shuffle

def scrambleMutation(individual):

    newIndividual = individual.copy()
    scramblePortion = []

    point1 = random.randint(0,len(individual))
    point2 = random.randint(0,len(individual))
    while point2 == point1:
        point2 = random.randint(0, len(individual) - 1)
    print(point1,point2)

    if point1 < point2:
        for i in range(point2-point1):
            scramblePortion.append(individual[point1 + i])
            print(scramblePortion)
        scramblePortion = random.sample(scramblePortion, len(scramblePortion))
        for j in range(len(scramblePortion)):
            newIndividual[point1 + j] = scramblePortion[j]

    else:
        for i in range(point1-point2):
            scramblePortion.append(individual[point2 + i])
            print(scramblePortion)
        scramblePortion = random.sample(scramblePortion, len(scramblePortion))
        for j in range(point1-point2):
            newIndividual[point2 + j] = scramblePortion[j]
    print(newIndividual)
