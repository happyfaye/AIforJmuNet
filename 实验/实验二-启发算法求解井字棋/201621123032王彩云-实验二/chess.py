#coding=utf-8
"""
[0,1,2]
[3,4,5]
[6,7,8]
"""

#胜利的走法
win_chess = [[0,4,8],[2,4,6],[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]]
#最佳下棋顺序
best_way = [4,0,2,6,8,1,3,5,7]
#棋盘
chess = [0,0,0,0,0,0,0,0,0]

def is_win(now_chess,who):
    """
    判断游戏方（who）是否赢局
    """
    temp = now_chess[:]
    for w_c in win_chess:
        if temp[w_c[0]] == who and temp[w_c[1]] == who and temp[w_c[2]] == who :
            return who
    return 0

def count_zero(now_chess):
    """
    统计剩余格子
    返回个数
    """
    temp = now_chess[:]
    count = 0
    for te in temp:
        if te == 0:
            count = count + 1
    return count

def evaluation(now_chess):
    """
    估价函数（以X为对象）
    可以赢的行数 +1
    可以赢的行数上有自己的棋子 +2
    可导致自己赢 +2
    可导致对手赢 -2
    """
    temp = now_chess[:]
    count = 0
    for w_c in win_chess:
        if temp[w_c[0]] >= 0 and temp[w_c[1]] >= 0 and temp[w_c[2]] >= 0 :
            if temp[w_c[0]] == 1 or temp[w_c[1]] == 1 or temp[w_c[2]] == 1 :
                count += 1
            count += 1
    if is_win(temp,1) == 1:
        count = count + 2
    if is_win(temp,-1) == -1:
        count = count - 2
    return count

def all_go(now_chess,who):
    """
    遍历所有走法
    """
    temp = now_chess[:]
    tempp = []
    for i in best_way:
        if temp[i] == 0:
            temppp = temp[:]
            temppp[i]=who
            tempp.append([temppp,i])
    return tempp

def get_next_x(now_chess,who):
    """
    x获取下一个位置
    """
    temp = now_chess[:]
    best_list = None
    best_one = -1
    if count_zero(temp) <= 3 :
        for te in all_go(temp,who):
            if best_one == -1:
                best_list = te[0]
                best_one = te[1]
            else :
                if evaluation(te[0]) > evaluation(best_list):
                    best_list = te[0]
                    best_one = te[1]
        return best_one
    for te in all_go(temp,who):
        for tee in all_go(te[0],who*-1):
            for teee in all_go(tee[0],who):
                if best_list is None:
                    best_list = teee[0]
                    best_one = te[1]
                else:
                    if evaluation(teee[0]) > evaluation(best_list) :
                        best_list = teee[0]
                        best_one = te[1]
    return best_one

def get_next_o(now_chess,who):
    """
    o获取下一个位置
    """
    temp = now_chess[:]
    best_list = None
    best_one = -1
    if count_zero(temp) <= 2 :
        for te in all_go(temp,who):
            if best_one == -1:
                best_list = te[0]
                best_one = te[1]
            else :
                if evaluation(te[0]) < evaluation(best_list):
                    best_list = te[0]
                    best_one = te[1]
        return best_one
    for te in all_go(temp,who):
        for tee in all_go(te[0],who*-1):
            if best_list is None:
                best_list = tee[0]
                best_one = te[1]
            else:
                if evaluation(tee[0]) < evaluation(best_list) :
                    best_list = tee[0]
                    best_one = te[1]
    return best_one

def is_danger(now_chess,who=0):
    """
    判断自己是否处于危险状态（即 对手可能已经差一子赢局）
    """
    temp = now_chess[:]
    for te in all_go(temp,who*-1):
        if is_win(te[0],who*-1) == who*-1:
            return te[1]
    return -1

if __name__ == "__main__":
    """
    测试用
    """
    chess = [0,0,0,\
            0,1,0,\
            0,0,0]
    #print(get_next_old(chess,-1,1))
    #print(all_go(chess,1))
    print(get_next_o(chess,-1))