import random
import fitness
import operator

# From min to max, in terms of the fitness value
def sortPopulation(population, fitness):
    popFitPair = list(map(list,zip(population, fitness)))
    popFitPair.sort(key=operator.itemgetter(1), reverse=False)

    sortedPop = []
    sortedFit = []

    for entry in popFitPair:
        sortedPop.append(entry[0])
        sortedFit.append(entry[1])

    return sortedPop, sortedFit

# Takes the best individuals (in terms of fitness) from both the offspring and the
# current population into a new population the size of 'currentPopulation' this
# discards all the worst individuals (in terms of fitness)
def mu_plus_lambda(currentPopulation, currentFitnessArray, offspring, offspringFitness):

    population = []
    fitness = []

    tempPop = currentPopulation.copy() + offspring.copy()
    tempFit = currentFitnessArray.copy() + offspringFitness.copy()
    sortedPop, sortedFit = sortPopulation(tempPop,tempFit)

    for i in range(0, len(currentPopulation)):
        population.append(sortedPop[i])
        fitness.append(sortedFit[i])

    return population, fitness

# Tournament Selection
# def tournament(correctedFitness, originalFitness, currPop, mating_pool_size, tournament_size):
#     newPopulation = []
#     newFitness = []
#     tournamentPlayers = []
#     while(len(newPopulation) < mating_pool_size):
#         tournamentPlayers = random.sample(correctedFitness,tournament_size)
#         bestFit = -1
#         for individual in tournamentPlayers:
#             if(individual > bestFit):
#                 bestFit = individual
#         for i in range(len(correctedFitness)):
#             if correctedFitness[i] == bestFit:
#                 newFitness.append(originalFitness[i])
#                 newPopulation.append(currPop[i])
#
#
#    return newPopulation, newFitness
