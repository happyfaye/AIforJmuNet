from random import (choice, random, randint)
import timeit
from time import sleep
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

__all__ = ['Chromosome', 'Population']

class Chromosome:
    
   
    _target_gene = "hello,201421123042"
    
    def __init__(self, gene):
        self.gene = gene
        self.fitness = Chromosome._update_fitness(gene)
    
    def mate(self, mate):
        pivot = randint(0, len(self.gene) - 1)
        gene1 = self.gene[:pivot] + mate.gene[pivot:]
        gene2 = mate.gene[:pivot] + self.gene[pivot:]
        
        return Chromosome(gene1), Chromosome(gene2)
    
    def mutate(self):
        gene = list(self.gene)
        delta = randint(32, 121)
        idx = randint(0, len(gene) - 1)
        gene[idx] = chr((ord(gene[idx]) + delta) % 122)
        
        return Chromosome(''.join(gene))

    @staticmethod            
    def _update_fitness(gene):
        fitness = 0
        for a, b in zip(gene, Chromosome._target_gene):
            fitness += abs(ord(a) - ord(b))
        return fitness
        
    @staticmethod
    def gen_random():
        gene = []
        for x in range(len(Chromosome._target_gene)):
            gene.append(chr(randint(32, 121)))
                
        return Chromosome(''.join(gene))
        
class Population:
    
    _tournamentSize = 3
    
    def __init__(self, size=2000, crossover=0.8, elitism=0.1, mutation=0.03):
        self.elitism = elitism
        self.mutation = mutation
        self.crossover = crossover
        
        buf = []
        for i in range(size): buf.append(Chromosome.gen_random())
        self.population = list(sorted(buf, key=lambda x: x.fitness))
                        
    def _tournament_selection(self):
        best = choice(self.population)
        for i in range(Population._tournamentSize):
            cont = choice(self.population)
            if (cont.fitness < best.fitness): best = cont
                    
        return best

    def _selectParents(self):
                    
        return (self._tournament_selection(), self._tournament_selection())
        
    def evolve(self):
        size = len(self.population)
        idx = int(round(size * self.elitism))
        buf = self.population[:idx]
        
        while (idx < size):
            if random() <= self.crossover:
                (p1, p2) = self._selectParents()
                children = p1.mate(p2)
                for c in children:
                    if random() <= self.mutation:
                        buf.append(c.mutate())
                    else:
                        buf.append(c)
                idx += 2
            else:
                if random() <= self.mutation:
                    buf.append(self.population[idx].mutate())
                else:
                    buf.append(self.population[idx])
                idx += 1
        
        self.population = list(sorted(buf[:size], key=lambda x: x.fitness))

if __name__ == "__main__":
    
        start_time = timeit.default_timer()
        vals=[]
        maxGenerations = 3000
        pop = Population(size=2000, crossover=0.8, elitism=0.1, mutation=0.3)
        
        for i in range(1, maxGenerations + 1):
                print("Generation %d: %s" % (i, pop.population[0].gene))
                vals.append(pop.population[i].fitness)
                if pop.population[0].fitness == 0: break
                else:pop.evolve()
        else:
                print("Maximum generations reached without success.")
        elapsed = timeit.default_timer() - start_time
        print("Finished in%10f seconds." % elapsed)
        plt.figure(1)
        plt.subplot(111)
        x = range(i)
        y = vals[:]
        plt.plot(x,y)
        plt.xlabel("gar",fontsize=14)
        plt.ylabel("val",fontsize=14)
        plt.show()
        vals.sort()
        print(vals[0])
       
