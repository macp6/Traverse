import random
# 
def tournament(fitness, mating_pool_size, tournament_size):
    selectedToMate = []

    while len(selectedToMate) < mating_pool_size:
        bestIndex = 0
        bestFitness = -1
        # Create a list of random index's from 0 to length of fitness-1
        indexSelection = random.sample(range(0, len(fitness), tournament_size))
        for x in range(0, tournament_size):
            if fitness[indexSelection[x]] > bestFitness:
                bestFitness = fitness[indexSelection[x]]
                bestIndex = indexSelection[x]
        selectedToMate.append(bestIndex)

    return selectedToMate

