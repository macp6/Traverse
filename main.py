import initialization
import fitness
import parentSelection
import survivorSelection
import recombination
import mutation
import distance
import visual

import random
import math
from datetime import datetime

# Comp 3201 - Final Project
# Authors: Mackenzie Peyton, David MacInnis

def main():

    distanceDictionary = {}
    populationSize = 500
    matingPoolSize = int(populationSize * 0.5)
    mutRate = 0.2
    xOverRate = 0.9
    genLimit = 15000
    fileName = "TSP_WesternSahara_29.txt"

    # Asks user which file they want to load
    files = ["TSP_WesternSahara_29.txt", "TSP_Uruguay_734.txt", "TSP_Canada_4663.txt"]
    print("Which is the file you want to load?\n[1] "+ files[0] + "\n[2] " + files[1] + "\n[3] " + files[2] + "\n")
    fileNum = input("Enter number: ")
    type(fileNum)
    fileName = files[int(fileNum) - 1]
    print("\nLoading:" + fileName + "\n")

    startTime = datetime.now()

    coordinates = []
    current = []
    avgFitVsGenArray = [] # for ploting at the end

    # Get data from file
    with open(fileName, 'r') as file:
        for line in file:
            line = line.replace("\n","")
            current = line.split(" ")
            for i in range(len(current)):
                current[i] = float(current[i])
            coordinates.append(current)
            current = []

    # Pre Calculations of all possible distances
    distanceDictionary = distance.preCal(coordinates)

    gen = 0
    # Create initial population
    population = initialization.randomization(populationSize, coordinates)

    # For fitness pass in array and if it is a population
    fitnessArray = fitness.preCalSumOfDistance(population, distanceDictionary, True) # Pre Calculation Method

    # To be used in MPS
    correctedFitnessArray = fitness.fitnessCorrection(fitnessArray)

    pastFit = 0
    stall = 0
    while gen < genLimit:

        # Pick parents
        parentsIndex = parentSelection.MPS(correctedFitnessArray, matingPoolSize)

        # Randomly pair up parents
        random.shuffle(parentsIndex)

        # Reproduction
        offspring = []
        offspringFitness = []
        # Initialize the counter(i) for the parents in the mating pool
        i = 0
        # Offspring are generated using selected parents in the mating pool
        while len(offspring) < matingPoolSize:
            # Recombination
            if random.random() < xOverRate:
                off1, off2 = recombination.modifiedNPointCrossover(population[parentsIndex[i]].copy(),population[parentsIndex[i+1]].copy())
            else:
                off1 = population[parentsIndex[i]].copy()
                off2 = population[parentsIndex[i+1]].copy()

            # Mutation
            if random.random() < mutRate:
                if stall > 10: # Switch to random swap
                    off1 = mutation.randomSwap(off1)
                else: # Scramble Mutation
                    off1 = mutation.scrambleMutation(off1)
            if random.random() < mutRate:
                if stall > 10: # Switch to random swap
                    off1 = mutation.randomSwap(off1)
                else: # Scramble Mutation
                    off2 = mutation.scrambleMutation(off2)

            offspring.append(off1)
            offspringFitness.append(fitness.preCalSumOfDistance(off1, distanceDictionary, False)) # Pre Calculation Method

            offspring.append(off2)
            offspringFitness.append(fitness.preCalSumOfDistance(off2, distanceDictionary, False)) # Pre Calculation Method
            # Update counter
            i += 2
        if pastFit == round(sum(fitnessArray)/len(fitnessArray),2):
            stall += 1
        else:
            pastFit = round(sum(fitnessArray)/len(fitnessArray),2)
            stall = 0

        # Plot for avg fit vs gen
        avgFitVsGenArray.append(round(sum(fitnessArray)/len(fitnessArray),2))
        # Population for the next generation
        population, fitnessArray = survivorSelection.mu_plus_lambda(population, fitnessArray, offspring, offspringFitness)

        # Update the generation counter
        gen += 1
        print("generation", gen, ": best fitness", min(fitnessArray), "average fitness", round(sum(fitnessArray)/len(fitnessArray),2))
    # Evolution ends

    # Stop timing of program
    print('\nTime elasped: ', datetime.now() - startTime, '\n')

    # The final best solution(s)
    drawThis = -1
    bestSolAppeared = 0
    for i in range (0, populationSize):
        if fitnessArray[i] == min(fitnessArray):
            bestSolAppeared += 1
            drawThis = i

    print("best solution", min(fitnessArray),"appeared",bestSolAppeared,"time(s)\n")


    # Draw solution to screen
    visual.drawGraph(population[drawThis], math.floor(min(fitnessArray)), genLimit, fileName, populationSize)

    # Draw avg fit vs gen to screen
    visual.avgFitVsGen(avgFitVsGenArray, math.floor(min(fitnessArray)), genLimit, fileName, populationSize)

# end of main

main()
