import numpy as np
#根据浏览器的那个拼图游戏计算迭代次数和gpf的值
 
class GeneticAlgorithm(object):

    def __init__(self, cross_rate, mutation_rate, n_population, n_iterations, password):
        self.cross_rate = cross_rate
        self.mutate_rate = mutation_rate
        self.n_population = n_population
        self.n_iterations = n_iterations
        self.password = password                                            
        self.password_size = len(self.password)                           
        self.password_ascii = np.fromstring(self.password, dtype=np.uint8)  
        self.ascii_bounder = [32, 126+1]
 
 
    # 初始化
    def init_population(self):
        population = np.random.randint(low=self.ascii_bounder[0], high=self.ascii_bounder[1], 
                                       size=(self.n_population, self.password_size)).astype(np.int8)
        return population
 

    def translateDNA(self, DNA):                
        return DNA.tostring().decode('ascii')
 
    # 计算适应度
    def fitness(self, population):
        match_num = (population == self.password_ascii).sum(axis=1)
        return match_num
 
    # 对种群按照其适应度进行采样
    def select(self, population):
        fitness = self.fitness(population) + 1e-4     
        idx = np.random.choice(np.arange(self.n_population), size=self.n_population, replace=True, p=fitness/fitness.sum())
        return population[idx]
 
    # 交配
    def create_child(self, parent, pop):
        if np.random.rand() < self.cross_rate:
            index = np.random.randint(0, self.n_population, size=1)                       
            cross_points = np.random.randint(0, 2, self.password_size).astype(np.bool)   
            parent[cross_points] = pop[index, cross_points]                            
            #child = parent
        return parent
 
    # 基因突变
    def mutate_child(self, child):
        for point in range(self.password_size):
            if np.random.rand() < self.mutate_rate:
                child[point] = np.random.randint(*self.ascii_bounder) 
        return child
 
    # 进化
    def evolution(self):
        population = self.init_population()
        for i in range(self.n_iterations):
            fitness = self.fitness(population)
 
            best_person = population[np.argmax(fitness)]
            best_person_ascii = self.translateDNA(best_person)
 
            if i % 1 == 0:
                print(u'Generation %d:%s'% (i, best_person_ascii))
 
            if best_person_ascii == self.password:
                print(u'Generation %d:%s'% (i+1, best_person_ascii))
                print(u'适应度为%s'% (fitness))
                break
 
            population = self.select(population)
            population_copy = population.copy()
 
            for parent in population:
                child = self.create_child(parent, population_copy)
                child = self.mutate_child(child)
                parent[:] = child
 
            population = population
 
def main():
    password = 'Hello,201621123014'   
 
    ga = GeneticAlgorithm(cross_rate=0.9, mutation_rate=0.014, n_population=200, n_iterations=5000, password=password)
 
    ga.evolution()
 
if __name__ == '__main__':
    main()
