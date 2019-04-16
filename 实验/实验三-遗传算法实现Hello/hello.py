import matplotlib.pyplot as plt
import math
import random
import timeit

goalText="Hello,201621123033"  #目标字符串

def main():
    start = timeit.default_timer()

    global goalText

    pop_size = 10000  # 种群数量

    chromosome_length = len(goalText)  # 染色体长度
    iter = 500
    pc = 0.6 # 杂交概率
    pm = 0.01  # 变异概率
    results = []  # 存储每一代的最优基因
    y_=[]  #存储每一代最优基因的适应度值
    pop = init_population(pop_size, chromosome_length) #初始种群

    for i in range(iter):

        best_individual= find_best(pop)  # 最优基因

        results.append(best_individual)
       
        selectpop=selection(pop, pop_size)  # 选择
        nextoff=[] #下一代
        while len(nextoff) != pop_size: #进化
            offspring = [random.choice(selectpop) for i in range(2)]
            if random.random()<pc:  #若小于交叉概率则进行交叉
                crossoff=crossover(offspring) 
                if random.random()<pm:  #若小于变异概率则变异
                    muteoff=mutation(crossoff,pm)
                    nextoff.append(muteoff)  #将交叉变异后的新个体加入到新种群中
            
        pop=nextoff #种群变为新一代
        print('Generation %d :%s' % (i,results[i][0]))
        fit=float(results[i][1])
        y_.append(fit)
        #print(type(results[i][0]))
        if fit==1:
            #print('break')
            break
    
    time = timeit.default_timer() - start
    print("用时：%10f" %time)

    #绘制迭代收敛图
    plt.figure(1)
    plt.subplot(111)
    x=range(i+1)
    y=y_[:]
    plt.plot(x,y)
    plt.show()


#初始化种群
def init_population(pop_size, chromosome_length):
    pop=[]        #种群列表
    geneinfo=[]   #个体列表两个元素：基因排序，适应度值
    for i in range(pop_size):
        geneinfo=[]
        #随机生成个体
        gene=''.join(random.sample([chr(i) for i in range(32,127)],int(chromosome_length)))
        
        geneinfo.append(gene)     
        fitness=calc_genefitness(gene)  #计算适应度值
        geneinfo.append(fitness)        
        pop.append(geneinfo) #将该个体加入种群列表中
    #print(pop)
    return pop

#计算个体适应度
def calc_genefitness(gene):
    score=1  #初始分数为1
    for i in range(len(gene)):     #比较个体与目标个体，每匹配到一个相同基因则分数加1
        if (goalText[i]==gene[i]):
            score=score+1
    fitness=(score/(len(gene)+1))  #计算适应度值，注意除数为个体长度加1，保证适应度值小于1
    return fitness
            


# 找出最优个体
def find_best(pop):

    best_individual = pop[0]  #默认最优个体为种群第一个个体

    best_fit = pop[0][1]      #默认最优适应度值为目前最优个体的适应度值
    for i in range(1, len(pop)):
        if (pop[i][1] > best_fit):    #循环比较找出适应度值最高的个体
            best_fit = pop[i][1]
            best_individual = pop[i]

    return best_individual


# 计算累积概率
def calc_sum(fit_value):   
    temp = fit_value[:]
    for i in range(len(temp)):    
        fit_value[i] = (sum(temp[:i + 1]))


# 轮赌法选择
def selection(pop,pop_size):
    fit_value = [] #放置种群个体适应度值概率的列表

    total_fit = sum(pop[i][1] for i in range(len(pop))) #适应度总和

    for i in range(len(pop)):
        fit_value.append(pop[i][1]/total_fit)  #算出此时每个个体适应度值的概率

    # https://www.cnblogs.com/LoganChen/p/7509702.html
    #print(pop)
    calc_sum(fit_value)  #计算累积概率
    pop_len = len(pop) #种群数量
    # 构造轮盘
    ms = sorted([random.random() for i in range(pop_len)])
    fitin = 0
    newin = 0
    newpop = pop[:]
    # 轮盘选择法
    while newin < pop_len:
        # 如果这个概率大于随机出来的那个概率，就选择它
        if (ms[newin] < fit_value[fitin]):
            newpop[newin] = pop[fitin]
            newin = newin + 1
        else:
            fitin = fitin + 1

    pop = newpop[:]
    #print(pop)
    return pop
    


#杂交
def crossover(offstring):
    off_len=len(offstring[0][0]) #计算个体长度
    gene1=offstring[0][0]
    gene2=offstring[1][0]

    pos=random.randint(0,off_len)  #随机选择一个交叉点

    newoff=[]
    temp=[]

    for i in range(off_len):      #交叉生成新个体
        if i<=pos :
            temp.append(gene1[i])
        else:
            temp.append(gene2[i])
            
    newgene=''.join(temp)
    newoff.append(newgene)
    newoff.append(calc_genefitness(newgene))

    return newoff
    #print (newoff)


# 基因突变
def mutation(crossoff,pm):
    off_len=len(crossoff[0])
   
    pos=random.randint(0,off_len)  #随机生成变异点
    for i in range(off_len):
        mutate=random.random()
        if mutate<pm:                  #若小于变异概率则变异，否则还为交叉后的个体
            j=random.randint(32,127)   #随机生成变异字符
            newchar=chr(j)
            s=list(crossoff[0])
            s[i]=newchar
            crossoff[0]=''.join(s)
            crossoff[1]=calc_genefitness(crossoff[0])
    
    return crossoff    


if __name__ == '__main__':
    main()
    
