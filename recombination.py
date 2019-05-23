import random

def removeDuplicates(arrayWithDuplicates):
    seen = set()
    unique = [] # unique numbers in arrayWithDuplicates
    for x in arrayWithDuplicates:
        if x not in seen:
            unique.append(x)
            seen.add(x)
    return unique

# Picks a random number of crossover points
def modifiedNPointCrossover(parent1, parent2):
    offspring1 = []
    offspring2 = []
    xOverPoints = []
    xOver = False

    limitOfPoints = len(parent1)/2
    numPoints = random.randint(1,int(limitOfPoints))

    for i in range(numPoints):
        xOverPoints.append(random.randint(0,len(parent1)))


    newXOP = removeDuplicates(xOverPoints)
    xOverPoints.clear()
    xOverPoints = newXOP.copy()

    xOverPoints.sort()
    xOverPoints.append(len(parent1)-1)

    j = 0
    for i in range(len(xOverPoints)):

        while j < xOverPoints[i]:
            if xOver:
                if not(parent1[j] in offspring2):
                    offspring2.append(parent1[j])

                if not (parent2[j] in offspring1):
                    offspring1.append(parent2[j])
                j+=1
            else:
                if not (parent1[j] in offspring1):
                    offspring1.append(parent1[j])
                if not (parent2[j] in offspring2):
                    offspring2.append(parent2[j])
                j+=1
        if xOver:
            xOver = False
        else:
            xOver = True

    while len(offspring2) < len(parent2):
        for h in range(len(parent2)):
            if not (parent1[h] in offspring2):
                offspring2.append(parent1[h])

    while len(offspring1) < len(parent1):
        for h in range(len(parent1)):
            if not (parent2[h] in offspring1):
                offspring1.append(parent2[h])


    return offspring1, offspring2
