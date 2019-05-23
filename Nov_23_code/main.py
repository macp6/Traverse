import initialization
import fitness
import parentSelection
import survivorSelection
import recombination
import mutation

import random
# Comp 3201 - Final Project


def main():

    populationSize = 20
    matingPoolSize = int(populationSize * 0.5)
    tournamentSize = 5
    mutRate = 0.2
    xOverRate = 0.9
    genLimit = 50
    fileName = "TSP_WesternSahara_29.txt"

    # Asks user which file they want to load
    # files = ["TSP_WesternSahara_29.txt", "TSP_Uruguay_734.txt", "TSP_Canada_4663.txt"]
    # print("Which is the file you want to load?\n[1] "+ files[0] + "\n[2] " + files[1] + "\n[3] " + files[2] + "\n")
    # fileNum = input("Enter number: ")
    # type(fileNum)
    # fileName = files[int(fileNum) - 1]
    # print("\nLoading:" + fileName + "\n")
    coordinates = []
    current = []

    # Get data from file
    with open(fileName, 'r') as file:
        for line in file:
            line = line.replace("\n", "")
            current = line.split(" ")
            for i in range(len(current)):
                current[i] = float(current[i])
            coordinates.append(current)
            current = []
    #print(coordinates)

    gen = 0
    population = initialization.randomization(populationSize, coordinates)
    fitnessArray = fitness.sumOfDistance(population)
    print(fitnessArray)
    newFitnessArray = fitness.fitnessCorrection(fitnessArray)
    print("new fitness")
    print(newFitnessArray)
    #print(fitnessArray)


    while gen < genLimit:

        # Pick parents
        parentsIndex = parentSelection.MPS(fitnessArray, matingPoolSize)

        # To randomly pair up parents
        random.shuffle(parentsIndex)

        # Reproduction
        offspring = []
        offspringFitness = []
        i = 0 # Initialize the counter for parents in the mating pool
        # offspring are generated using selected parents in the mating pool
        while len(offspring) < matingPoolSize:

            # recombination
            if random.random() < xOverRate:
                off1, off2 = recombination.modifiedNPointCrossover(population[parentsIndex[i]], population[parentsIndex[i+1]])
            else:
                off1 = population[parentsIndex[i]].copy()
                off2 = population[parentsIndex[i+1]].copy()

            # mutation
            if random.random() < mutRate:
                off1 = mutation.scrambleMutation(off1)
            if random.random() < mutRate:
                off2 = mutation.scrambleMutation(off2)

            offspring.append(off1)
            offspringFitness.append(fitness.sumOfDistance(off1))
            offspring.append(off2)
            offspringFitness.append(fitness.sumOfDistance(off2))
            # update counter
            i += 2

        # Form the population for the next generation
        population, newFitnessArray = survivorSelection.tournament(newFitnessArray, mating_pool_size, tournament_size)

        # Update the generation counter
        gen += 1
        print("Generation", gen, ": best fitness", min(fitnessArray), "average gitness", sum(fitnessArray)/len(fitnessArray))

    # Evolution ends

    # Print the final best solution(s)
    k = 0
    for i in range(0, populationSize):
        if fitness[i] == min(fitness):
            print("best solution", k, population[i], fitness[i])
            k += 1

# End of main

main()
