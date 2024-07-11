import random
from Schedule import *
from Population import *
from Individual import *
from typing import List


class GeneticAlgorithm:
    def __init__(self, popSize, rateOfMutation, rateOfCrossover, count, tournSize):
        self.popSize = popSize
        self.rateOfMutation = rateOfMutation
        self.rateOfCrossover = rateOfCrossover
        self.count = count
        self.tournSize = tournSize

    def calcFitness(self, individual, schedule):
        threadSchedule = Schedule(schedule)
        threadSchedule.createClasses(individual)
        clashes = threadSchedule.calcClashes(self.popSize)
        fitness = clashes / 100.0
        individual.setFitness(fitness)
        return fitness







    def isTerminating(self, population):
        if population.getFittest(0).getFitness() == 1.0 or population.getFittest(0).getFitness() >= 100.0 :
          return population.getFittest(0).getFitness()

    def selectionFunction(self, population):
        tournament = Population(self.tournSize)
        population.shuffle()
        for i in range(self.tournSize):
            tournamentIndividual = population.getIndividual(i)
            tournament.setIndividual(i, tournamentIndividual)
        return tournament.getFittest(0)

    def crossoverPopulation(self, population):
        newPopulation = Population(population.size())
        for populationIndex in range(population.size()):
            parent1 = population.getFittest(populationIndex)
            if self.rateOfCrossover > random.random() and \
                    populationIndex > self.count:# How many individual should not crossover and should just pass on to next generation
                offspring = Individual()
                offspring.init_with_chromlen(parent1.getChromosomeLength())
                parent2 = self.selectionFunction(population)
                for geneIndex in range(parent1.getChromosomeLength()):
                    if random.random() < 0.5:
                        offspring.setGene(geneIndex, parent1.getGene(geneIndex))
                    else:
                        offspring.setGene(geneIndex, parent2.getGene(geneIndex))
                newPopulation.setIndividual(populationIndex, offspring)
            else:
                newPopulation.setIndividual(populationIndex, parent1)
        return newPopulation

    def mutatingPopulation(self, population, schedule):
        newPopulation = Population(self.popSize)

        for populationIndex in range(population.size()):
            individual = population.getFittest(populationIndex)
            randomIndividual = Individual()
            randomIndividual.init_with_sched(schedule)

            for geneIndex in range(individual.getChromosomeLength()):
                if populationIndex > self.count:
                    if random.random() < self.rateOfMutation:
                        individual.setGene(geneIndex, randomIndividual.getGene(geneIndex))
            newPopulation.setIndividual(populationIndex, individual)
        return newPopulation

    def initializingPopulation(self, schedule):
        population = Population(self.popSize)
        population.init_with_schedule(self.popSize, schedule)
        return population

    def calcPopulation(self, population, schedule):
        for individual in population.getIndividuals():
            self.calcFitness(individual, schedule)
        populationFitness = sum(individual.getFitness() for individual in population.getIndividuals())
        population.setPopulationFitness(populationFitness)
