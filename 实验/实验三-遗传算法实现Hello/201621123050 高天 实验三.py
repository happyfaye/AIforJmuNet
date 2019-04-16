import numpy as np
import timeit
from time import sleep

TARGET = '201621123050 hello'
DNA_SIZE = len(TARGET)
GENERATION = 2000
CROSSOVER_RATE = 0.4
MUTATE_RATE = 0.01
POP_SIZE = 300
DNA_BOUND = [32,123]
TARGET_ARR = np.fromstring(TARGET,dtype = np.uint8)

class GA(object):
    def __init__(self):
        self.pop = np.random.randint(DNA_BOUND[0],DNA_BOUND[1],(1,DNA_SIZE)).astype(np.int8).repeat(POP_SIZE,axis=0)
    
    def getFitness(self,pop):
        root = np.fromstring(TARGET,dtype = np.int8).reshape(1,DNA_SIZE).repeat(POP_SIZE,axis=0)
        root = root - pop
        return np.sum(root==0,axis=1)
        
        
    def select(self,fitness):
        
        idx = np.random.choice(np.arange(POP_SIZE),size = POP_SIZE,replace = True,p = fitness/fitness.sum())
        #print("idx : ",idx)
        
        return self.pop[idx]
    
    def mutate(self,child):
        for index in range(DNA_SIZE):
            if np.random.rand() < MUTATE_RATE:
                child[index] = np.random.randint(DNA_BOUND[0],DNA_BOUND[1],size=1)
        return child
    
    def crossover(self,parent,pop):
        if np.random.rand() < CROSSOVER_RATE:
            i = np.random.randint(0,POP_SIZE,size=1)
            
            cross_points = np.random.randint(0,2,size=DNA_SIZE).astype(np.bool)
            parent[cross_points] = pop[i,cross_points]
        return parent
            
    def translateDNA(self,row):
        return row.tostring().decode('ascii')
    
    def evolution(self,gen):
        fitness = self.getFitness(self.pop) + 1e-4
        
        self.pop = self.select(fitness)
        
        bestRes = self.translateDNA(self.pop[np.argmax(fitness)])

        print("Gen : ",gen, " Result : ",bestRes)
        
        pop_copy = self.pop.copy()
        
        for parent in self.pop:
            child = self.crossover(parent,pop_copy)
            child = self.mutate(child)
            parent[:] = child
            
        return bestRes
    
    
if __name__ == '__main__':
    start_time = timeit.default_timer()
    a = GA()
    for gen in range(GENERATION):
        res = a.evolution(gen)
        if res == TARGET :
            break
    elapsed = timeit.default_timer() - start_time
    print("Finished in%10f seconds." % elapsed)
