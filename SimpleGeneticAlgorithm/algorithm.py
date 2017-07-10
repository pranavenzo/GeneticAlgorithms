from random import *
import math


# mutate chromosome based on stepsize and probability of mutation
# direction is -1 or 1
def mutate(chromosome, mutationProbability, randomFunction):
    x = 0
    for bits in chromosome:
        ran = randomFunction()
        if ran <= mutationProbability:
            chromosome[x] = 1 - chromosome[x]
        x += 1
    return chromosome


def crossover(chromosomeA, chromosomeB, crossOverProbability, randomFunction, myrandInt):
    ran = randomFunction()
    if ran > crossOverProbability:
        return (chromosomeA, chromosomeB)
    crossOverLength = myrandInt(0, len(chromosomeA))
    # random length of first chromosome
    # crossed over with the same sized piece in the second half of second chromosome
    newchromosomeA = chromosomeA[0:crossOverLength] + chromosomeB[crossOverLength:len(chromosomeB)]
    newchromosomeB = chromosomeB[0:crossOverLength] + chromosomeA[crossOverLength:len(chromosomeA)]
    return (newchromosomeA, newchromosomeB)


# Simple fitness function that counts the number of 1s in chromosome
def fitnessFuntion(chromosome):
    # number = int(''.join(str(e) for e in chromosome), 2)
    # return int(-4 * math.pow(number, 3) + math.pow(number, 6))
    matches = 0
    for i in range(0, len(chromosome)):
        if chromosome[i] == targetChromosome[i]:
            matches += 1
    return matches


def myprint(chromosomePool, generationNumber):
    print 'Generation :' + str(generationNumber)
    for chromosome in chromosomePool:
        print str(chromosome) + '--> fitness : ' + str(fitnessFuntion(chromosome))


def cleanUp(nextGenChromosomePool, randomFunction):
    cleanedUp = []
    total = 0.0
    nextGenChromosomePool.sort(comparator)
    for chromosome in nextGenChromosomePool:
        total += fitnessFuntion(chromosome)

    for chromosome in nextGenChromosomePool:
        ran = random()
        if ran <= (fitnessFuntion(chromosome) / total):
            cleanedUp.append(chromosome)

    return cleanedUp


def comparator(x, y):
    return fitnessFuntion(x) - fitnessFuntion(y)


def evolve(chromosomePopulation, myrandint, eliteNum):
    chromosomePopulation.sort(comparator, reverse=True)
    for i in range(eliteNum, len(chromosomePopulation)):
        i = myrandint(eliteNum, len(chromosomePopulation) - 1)
        j = myrandint(eliteNum, len(chromosomePopulation) - 1)
        (chromosomePopulation[i], chromosomePopulation[j]) = crossover(chromosomePopulation[i], chromosomePopulation[j],
                                                                       .25, random, randint)
    for i in range(eliteNum, len(chromosomePopulation)):
        chromosomePopulation[i] = mutate(chromosomePopulation[i], .25, random)
    return chromosomePopulation


def createGenePool(length):
    genes = []
    for i in range(0, length):
        if random() <= .5:
            genes.append(1)
        else:
            genes.append(0)
    return genes


def createChromosomePool(length, lengthPerGene):
    chromosomePool = []
    for i in range(0, length):
        chromosomePool.append(createGenePool(lengthPerGene))
    return chromosomePool


targetChromosome = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def main():
    target = len(targetChromosome)
    chromosomePool = createChromosomePool(10, target)
    for i in range(1, 4000):
        chromosomePool.sort(comparator, reverse=True)
        myprint(chromosomePool, i)
        if fitnessFuntion(chromosomePool[0]) == target:
            break
        chromosomePool = evolve(chromosomePool, randint, 3)


main()
