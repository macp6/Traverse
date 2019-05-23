import random

def modifiedNPointCrossover(parent1, parent2):
    offspring1 = []
    offspring2 = []
    xOverPoints = []
    xOver = False

    limitOfPoints = len(parent1)/2
    numPoints = random.randint(1,int(limitOfPoints))

    for i in range(numPoints):
        print("1")
        xOverPoints.append(random.randint(0,len(parent1)))

    xOverPoints.sort()
    xOverPoints.append(len(parent1)-1)
    print(xOverPoints)

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
            print(offspring1)
            print(offspring2)
        if xOver:
            xOver = False
        else:
            xOver = True




    print("2")

    while len(offspring2) < len(parent2):
        for h in range(len(parent2)):
            if not (parent1[h] in offspring2):
                offspring2.append(parent1[h])

    while len(offspring1) < len(parent1):
        for h in range(len(parent1)):
            if not (parent2[h] in offspring1):
                offspring1.append(parent2[h])


    print("4")
    print(xOverPoints)
    print(offspring2)
    print(offspring1)


#modifiedNPointCrossover([1,4,2,5,6,7,3,8,9], [8,6,5,7,9,1,3,2,4])