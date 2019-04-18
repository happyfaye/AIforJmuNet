

# 未完成的失败代码


import random


population = ['a', 'b', 'c', 'd', 'e', 'f',
              '1', '2', '3', '4', '1', '2', '3', '4', '1', '2', '3', '4']



target = ['H', 'e', 'l', 'l', 'o', ',',
              '2', '0', '1', '6', '2', '1', '1', '2', '3', '0', '8', '6']


def output(list):
    for x in list:
        print(chr(int(x, 2)), end='')


def evaluate(list, tar):
    s = 0
    chance = []
    for i in range(len(list)):
        s = s + abs(ord(tar[i]) - ord(list[i]))
        chance.append(s)
    print(chance)
    return s, chance


def create_child(list):
    l1 = random.randrange(0, 9)
    l2 = random.randrange(9, 18)
    index = random.randint(1, 6)
    t1 = (ord(list[l1]) & (2**index - 1)) + (ord(list[l2]) & (2**8 - 2**index))
    t2 = (ord(list[l2]) & (2**index - 1)) + (ord(list[l1]) & (2**8 - 2**index))
    print(l1, ' ', l2)
    print(index)
    print(bin(ord(list[l1]) & (2**index - 1)))
    print(bin(ord(list[l2]) & (2**8 - 2**index)))
    print(bin(t1))


def mutation(list, pm):
    px = len(list)
    for i in range(px):
        if random.random() < pm:




