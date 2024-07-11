import random
from Individual import *

class Population:
    def __init__(self, populationSize):
        self.population = [None] * populationSize
        self.populationFitness = -1


    def init_with_chromelength(self, populationSize, chromosomeLength):
        self.population = [Individual().init_with_chromlen(chromosomeLength) for _ in range(populationSize)]
        self.populationFitness = -1

    def getIndividuals(self):
        return self.population

    def getFittest(self, offset):
        self.population.sort(key=lambda individual: individual.getFitness(), reverse=True)
        return self.population[offset]

    def setPopulationFitness(self, fitness):
        self.populationFitness = fitness

    def getPopulationFitness(self):
        return self.populationFitness

    def size(self):
        return len(self.population)

    def setIndividual(self, offset, individual):
        self.population[offset] = individual

    def getIndividual(self, offset):
        return self.population[offset]

    def shuffle(self):
        random.shuffle(self.population)

    def init_with_schedule(self, populationSize, schedule):
        self.population = [Individual() for _ in range(populationSize)]
        for i in self.population:
            i.init_with_sched(schedule)


    def getAvgFitness(self):
        if self.populationFitness == -1:
            totalFitness = sum(individual.getFitness() for individual in self.population)
            self.populationFitness = totalFitness
        return self.populationFitness / self.size()
