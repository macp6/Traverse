import matplotlib.pyplot as plt

# Draws the tour of the given individual
def drawGraph(individual, minFitness, genLimit, fileName, populationSize):
    drawX = []
    drawY = []

    for x in range(0,len(individual)):
        drawX.append(individual[x][1])
        drawY.append(individual[x][2])

    drawX.append(individual[0][1])
    drawY.append(individual[0][2])

    fsize = plt.rcParams["figure.figsize"]
    fsize[0] = 8
    fsize[1] = 6
    plt.rcParams["figure.figsize"] = fsize
    plt.gca().invert_xaxis()
    plt.figure(1)
    plt.plot(drawY, drawX, 'ro-')
    plt.title(fileName + " - Best Fitness: " + str(minFitness) + " - PopSize: " +str(populationSize) + " - Gens: " + str(genLimit))
    fig1 = plt.gcf()
    plt.show() ### Displays graph ###
    plt.draw()

    ### For saving visual ###
    # myPath = 'D:/Dev/Git_Repos/COMP-3201-Project/figure_routes/'
    # location = ""
    # if fileName == "TSP_WesternSahara_29.txt":
    #     location = "WS_"
    # elif fileName == "TSP_Uruguay_734.txt":
    #     location = "UR_"
    # elif fileName == "TSP_Canada_4663.txt":
    #     location = "CA_"
    # else:
    #     location = "Unknown"
    # # File output name => (location)_(best fitness)_g-(# of generations)_p-(popSize).png
    # myFile = location + str(minFitness) + "_g-" + str(genLimit) + "_p-"+ str(populationSize) +".png"
    # fig1.savefig(myPath + myFile) ### Saves .png file of graph ###

# Draws an average fitness Vs. generations graph
def avgFitVsGen(avgFitArray, minFitness, genLimit, fileName, populationSize):
    draw = avgFitArray.copy()
    gen = list(range(1,genLimit+1))

    plt.figure(1)
    plt.plot(gen, avgFitArray, 'r-')
    fig2 = plt.gcf()
    plt.ylabel('Average Fitness')
    plt.xlabel('Generation')
    plt.title(fileName + " - Best Fitness: " + str(minFitness) + " - PopSize: " +str(populationSize) + " - Gens: " + str(genLimit))
    plt.show() ### Displays graph ###
    plt.draw()
    ### For saving visual ###
    # myPath = 'D:/Dev/Git_Repos/COMP-3201-Project/figure_routes/'
    # location = ""
    # if fileName == "TSP_WesternSahara_29.txt":
    #     location = "WS_"
    # elif fileName == "TSP_Uruguay_734.txt":
    #     location = "UR_"
    # elif fileName == "TSP_Canada_4663.txt":
    #     location = "CA_"
    # else:
    #     location = "Unknown"
    # File output name => (location)_(best fitness)_g-(# of generations)_p-(popSize).png
    # myFile = location + str(minFitness) + "_g-" + str(genLimit) + "_p-"+ str(populationSize) +"-line.png"
    # fig2.savefig(myPath + myFile) ### Saves .png file of graph ###
