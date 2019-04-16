#coding=utf-8
"""
"""
import time
import threading
import random
import chess

init_chess = [0,0,0,0,0,0,0,0,0]    #原始棋盘
the_chess = [0,0,0,0,0,0,0,0,0]    #记录棋盘
show_chess = ''
flag = True
who = 1
count_x = 0
count_y = 0
count_z = 0
def run(i,id):
    """
    创建一个机器对打局
    """
    new_chess = init_chess[:]
    global count_x
    global count_y
    global count_z
    if id == 1 :
        new_chess[random.randint(0,8)] = -1
    else :
        new_chess[random.randint(0,8)] = 1
    x = 0
    for x in range(10):
        if chess.count_zero(new_chess) > 0 :
            #print(chess.count_zero(new_chess))
            if id == 1:
                #print('*****')
                #print(chess.get_next_x(new_chess,id))
                pos = chess.get_next_x(new_chess,id)
                if pos != -1 :
                    new_chess[int(chess.get_next_x(new_chess,id))] = id
                else :
                    for xx in range(9):
                        if new_chess[xx] == 0 :
                            new_chess[xx] = id
            else :
                pos = chess.get_next_o(new_chess,id)
                if pos != -1 :
                    new_chess[int(chess.get_next_o(new_chess,id))] = id
                else :
                    for xx in range(9):
                        if new_chess[xx] == 0 :
                            new_chess[xx] = id
            id = id * -1
            if chess.is_win(new_chess,id) == id :
                name = ''
                if id == 1 :
                    name = 'X'
                    update_chess()
                    print("第 {} 局 ： {} 赢了！".format(i+1,name) + ' ' + str(new_chess))
                   # tips.set("第 {} 局 ： {} 赢了！".format(i+1,name))
                    threading.Lock()
                    count_x = count_x + 1
                    threading.RLock()
                    time.sleep(3)
                    break
                else :
                    name = 'O'
                    update_chess()
                    print("第 {} 局 ： {} 赢了！".format(i+1,name) + ' ' + str(new_chess))
                   # tips.set("第 {} 局 ： {} 赢了！".format(i+1,name))
                    threading.Lock()
                    count_y = count_y + 1
                    threading.RLock()
                    time.sleep(3)
                    break
            elif chess.is_win(new_chess,id*-1) == id*-1 :
                id = id * -1
                name = ''
                if id == 1 :
                    name = 'X'
                    print("第 {} 局 ： {} 赢了！".format(i+1,name) + ' ' + str(new_chess))
                   # tips.set("第 {} 局 ： {} 赢了！".format(i+1,name))
                    threading.Lock()
                    count_x = count_x + 1
                    threading.RLock()
                    break
                else :
                    name = 'O'
                    print("第 {} 局 ： {} 赢了！".format(i+1,name) + ' ' + str(new_chess))
                   # tips.set("第 {} 局 ： {} 赢了！".format(i+1,name))
                    threading.Lock()
                    count_y = count_y + 1
                    threading.RLock()
                    break
            elif chess.count_zero(new_chess) == 0:
                print("第 {} 局 ： 平局".format(i+1) + ' ' + str(new_chess))
               # tips.set("第 {} 局 ： 平局".format(i+1))
                threading.Lock()
                count_z = count_z + 1
                threading.RLock()
                break
            else :
                pass
        else :
            print("第 {} 局 ： 平局".format(i+1) + ' ' + str(new_chess))
            #tips.set("第 {} 局 ： 平局".format(i+1))
            threading.Lock()
            count_z = count_z + 1
            threading.RLock()
            break
    
    time.sleep(3)
    
id = 1   
th = []
for i in range(50):
        id = id * -1
        try:
            th.append(threading.Thread(target=run,args=(i,id)))
            th[i].start()
        except Exception as e:
            print(e)
            i = i - 1
            
print("50局已经结束！\nX 共赢 {}次\nO 共赢 {}次\n平局 {} 次".format(count_x,count_y,count_z))




