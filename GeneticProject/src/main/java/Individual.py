import random


class Individual:
    def init_with_chrom(self, chromosome):
        self.chromosome = chromosome
        self.fitness = -1

    def init_with_chromlen(self, chromosomeLength):
        self.fitness = -1
        individual = list(range(chromosomeLength))
        random.shuffle(individual)
        self.chromosome = individual

    def init_with_sched(self, schedule):
        self.fitness = -1
        numClasses = schedule.getNumClasses()
        chromosomeLength = numClasses * 3
        newChromosome = []

        for group in schedule.getGroupsAsArray():
            for courseId in group.getCourseIds():
                timeslotId = schedule.getRandomTimeslot().getTimeslotId()
                newChromosome.append(timeslotId)

                roomId = schedule.getRandomRoom().getRoomId()
                newChromosome.append(roomId)

                course = schedule.getCourse(courseId)
                newChromosome.append(course.getRandomProfessorId())

        self.chromosome = newChromosome

    def getChromosome(self):
        return self.chromosome

    def getChromosomeLength(self):
        return len(self.chromosome)

    def setGene(self, offset, gene):
        self.chromosome[offset] = gene

    def getGene(self, offset):
        return self.chromosome[offset]

    def setFitness(self, fitness):
        self.fitness = fitness

    def getFitness(self):
        return self.fitness

    def toString(self):
        return "".join(str(gene) for gene in self.chromosome)

    def containsGene(self, gene):
        return gene in self.chromosome
