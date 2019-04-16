import numpy as np
import matplotlib.pyplot as plt
import datetime

class GeneticAlgorithm(object):
    def __init__(self, cross_rate, mutation_rate, n_population, n_iterations, target_string):
        self.cross_rate = cross_rate
        self.mutate_rate = mutation_rate
        self.n_population = n_population
        self.n_iterations = n_iterations
        self.target_string = target_string
        self.target_string_size = len(self.target_string)
        self.target_string_ascii = np.fromstring(self.target_string, dtype=np.uint8)
        self.ascii_bounder = [32, 126 + 1]
        self.y = []
        self.x=[]
    # 初始化一个种群
    def init_population(self):
        population = np.random.randint(low=self.ascii_bounder[0], high=self.ascii_bounder[1],
                                       size=(self.n_population, self.target_string_size)).astype(np.int8)
        return population

    # 将个体的DNA转换成ASCII
    def translateDNA(self, DNA):
        return DNA.tostring().decode('ascii')

    # 计算种群中每个个体的适应度，适应度越高，说明该个体的基因越好
    def fitness(self, population):
        match_num = (population == self.target_string_ascii).sum(axis=1)
        return match_num

    # 对种群按照其适应度进行采样，这样适应度高的个体就会以更高的概率被选择
    def select(self, population):
        fitness = self.fitness(population) + 1e-4
        idx = np.random.choice(np.arange(self.n_population), size=self.n_population, replace=True,
                               p=fitness / fitness.sum())
        return population[idx]

    # 进行交叉
    def create_child(self, parent, pop):
        if np.random.rand() < self.cross_rate:
            index = np.random.randint(0, self.n_population, size=1)
            cross_points = np.random.randint(0, 2, self.target_string_size).astype(np.bool)
            parent[cross_points] = pop[index, cross_points]
            # print(np.random.rand())
        #     self.temp.append(np.random.rand())
        # else:
        #     self.temp.append(self.cross_rate)
            # child = parent
        return parent

    # 基因突变
    def mutate_child(self, child):
        for point in range(self.target_string_size):
            if np.random.rand() < self.mutate_rate:
                child[point] = np.random.randint(*self.ascii_bounder)
        return child

    # 进化
    def evolution(self):
        population = self.init_population()
        print(population)
        print(len(population))
        for i in range(self.n_iterations):
            self.x.append(i)
            fitness = self.fitness(population)
            # print(len(set(fitness)))
            self.y.append(len(set(fitness))/10)
            best_person = population[np.argmax(fitness)]
            best_person_ascii = self.translateDNA(best_person)
            # print()
            if i % 10 == 0:
                print(u'第%-4d次进化后, 基因最好的个体(与目标字符串最接近)是: \t %s' % (i, best_person_ascii))
            if best_person_ascii == self.target_string:
                print(u'第%-4d次进化后, 找到了目标字符串: \t %s' % (i, best_person_ascii))
                break
            # print(self.n_population)
            population = self.select(population)
            # print(population[i])
            population_copy = population.copy()

            for parent in population:
                child = self.create_child(parent, population_copy)
                child = self.mutate_child(child)
                parent[:] = child

            population = population
        print(len(self.y))
        print(len(self.x))
        plt.plot(self.x,self.y)
        plt.show()

def main():
    target_string = 'hello,201621123021'
    ga = GeneticAlgorithm(cross_rate=0.8, mutation_rate=0.01, n_population=10000, n_iterations=500,
                          target_string=target_string)

    ga.evolution()


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    main()
    endtime = datetime.datetime.now()
    print(endtime - starttime)