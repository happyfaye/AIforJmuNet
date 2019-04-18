#coding=utf-8
"""
"""
import tkinter as tk
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

top = tk.Tk()
top.title('井字棋 by boxker')
top.geometry("300x300")
top.resizable()
show_str = tk.StringVar(top)
tips = tk.StringVar(top)    #提示信息

#初始化棋盘信息
ch = []
for i in range(9):
    ch.append(tk.StringVar(top))

#初始化提示信息
tips.set("")

frame_top = tk.Frame(top)
frame_cont = tk.Frame(top)
frame_bot = tk.Frame(top)
frame_cont1 = tk.Frame(frame_cont)
frame_cont2 = tk.Frame(frame_cont)
frame_cont3 = tk.Frame(frame_cont)

label1 = tk.Label(frame_cont,justify=tk.CENTER,textvariable=show_str,font=("幼圆",30))

# 棋盘显示label 0~9
l0 = tk.Label(frame_cont1,textvariable=ch[0],font=("幼圆",30),padx=0)
l1 = tk.Label(frame_cont1,textvariable=ch[1],font=("幼圆",30),padx=0)
l2 = tk.Label(frame_cont1,textvariable=ch[2],font=("幼圆",30),padx=0)

l3 = tk.Label(frame_cont2,textvariable=ch[3],font=("幼圆",30),padx=0)
l4 = tk.Label(frame_cont2,textvariable=ch[4],font=("幼圆",30),padx=0)
l5 = tk.Label(frame_cont2,textvariable=ch[5],font=("幼圆",30),padx=0)

l6 = tk.Label(frame_cont3,textvariable=ch[6],font=("幼圆",30),padx=0)
l7 = tk.Label(frame_cont3,textvariable=ch[7],font=("幼圆",30),padx=0)
l8 = tk.Label(frame_cont3,textvariable=ch[8],font=("幼圆",30),padx=0)

label_bottom = tk.Label(frame_bot,justify=tk.CENTER,textvariable=tips,font=("幼圆",20),padx=0)

def update_chess():
    """
    更新棋盘
    """
    for i in range(9):
        if the_chess[i] == 1 :
            ch[i].set('|X|')
        elif the_chess[i] == -1 :
            ch[i].set('|O|')
        else :
            ch[i].set('| |')
        #print(i)

def init_ch():
    """
    初始化棋盘
    """
    for i in range(9):
        the_chess[i] = init_chess[i]
    update_chess()
    return the_chess

def ai_go_first():
    if chess.count_zero(the_chess) == 9:
        the_chess[random.randint(0,8)] = -1
    update_chess()
    forget()

ai_go_fir_b = tk.Button(frame_cont,text='机器先下',command=ai_go_first)

update_chess()

def forget():
    ai_go_fir_b.pack_forget()

def but1():
    """
    人机对战
    """
    flag = True
    init_ch()
    tips.set("人机对战模式")
    l0.bind("<Button-1>", touch_l0)
    l1.bind("<Button-1>", touch_l1)
    l2.bind("<Button-1>", touch_l2)
    l3.bind("<Button-1>", touch_l3)
    l4.bind("<Button-1>", touch_l4)
    l5.bind("<Button-1>", touch_l5)
    l6.bind("<Button-1>", touch_l6)
    l7.bind("<Button-1>", touch_l7)
    l8.bind("<Button-1>", touch_l8)
    ai_go_fir_b.pack(side=tk.TOP)

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
                    tips.set("第 {} 局 ： {} 赢了！".format(i+1,name))
                    threading.Lock()
                    count_x = count_x + 1
                    threading.RLock()
                    time.sleep(3)
                    break
                else :
                    name = 'O'
                    update_chess()
                    print("第 {} 局 ： {} 赢了！".format(i+1,name) + ' ' + str(new_chess))
                    tips.set("第 {} 局 ： {} 赢了！".format(i+1,name))
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
                    tips.set("第 {} 局 ： {} 赢了！".format(i+1,name))
                    threading.Lock()
                    count_x = count_x + 1
                    threading.RLock()
                    break
                else :
                    name = 'O'
                    print("第 {} 局 ： {} 赢了！".format(i+1,name) + ' ' + str(new_chess))
                    tips.set("第 {} 局 ： {} 赢了！".format(i+1,name))
                    threading.Lock()
                    count_y = count_y + 1
                    threading.RLock()
                    break
            elif chess.count_zero(new_chess) == 0:
                print("第 {} 局 ： 平局".format(i+1) + ' ' + str(new_chess))
                tips.set("第 {} 局 ： 平局".format(i+1))
                threading.Lock()
                count_z = count_z + 1
                threading.RLock()
                break
            else :
                pass
        else :
            print("第 {} 局 ： 平局".format(i+1) + ' ' + str(new_chess))
            tips.set("第 {} 局 ： 平局".format(i+1))
            threading.Lock()
            count_z = count_z + 1
            threading.RLock()
            break
    #print(str(i + 1) + ' ' + str(new_chess))
    '''if i == 9:
        print("第 {} 局 ： 平局".format(i+1) + ' ' + str(new_chess))
        tips.set("第 {} 局 ： 平局".format(i+1))
        threading.Lock()
        count_z = count_z + 1
        threading.RLock()'''
    time.sleep(3)
    for i in range(9):
        the_chess[i] = new_chess[i]
    update_chess()
    threading.Lock()
    tips.set("50局已经结束！\nX 共赢 {}次\nO 共赢 {}次\n平局 {} 次".format(count_x,count_y,count_z))
    threading.RLock()

def but2():
    """
    机器对战
    """
    print(" ")
    ai_go_fir_b.pack_forget()
    flag = False
    global count_x
    global count_y
    global count_z
    count_x = 0
    count_y = 0
    count_z = 0
    init_ch()
    tips.set("机器对战模式")
    l0.unbind("<Button-1>")
    l1.unbind("<Button-1>")
    l2.unbind("<Button-1>")
    l3.unbind("<Button-1>")
    l4.unbind("<Button-1>")
    l5.unbind("<Button-1>")
    l6.unbind("<Button-1>")
    l7.unbind("<Button-1>")
    l8.unbind("<Button-1>")
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
    #tips.set("50 局已经结束！ X 共赢 {}次， O 共赢 {}次， 平局 {} 次".format(count_x,count_y,count_z))
        

def ai_go(w):
    """
    机器走棋 O
    """
    if chess.count_zero(the_chess) < 9:   
        po = chess.is_danger(the_chess,1)
        if po != -1 :
            the_chess[po] = w
            update_chess()
        elif constraint(w) == False:
            pass
        else :
            the_chess[chess.get_next_o(the_chess,-1)] = w
            update_chess()
        if chess.is_win(the_chess,-1) == -1:
            tips.set("AI赢了！")
    if chess.count_zero(the_chess) == 0:
            tips.set("棋逢对手！201621123068与AI打成平局！")

def constraint(w):
    """
    判断是否处于危险状态
    """
    po = chess.is_danger(the_chess,-1)
    if po != -1:
        the_chess[po] = w
        update_chess()
        return False
    return True

def peo_go(po):
    """
    获取人们按键，并下棋
    """
    if the_chess[po] == 0 :
        the_chess[po] = who
        update_chess()
        if chess.is_win(the_chess,who) == who:
            tips.set('201621123068赢了！')
        elif chess.count_zero(the_chess) == 0:
            tips.set("棋逢对手！201621123068与AI打成平局！！")
        else :
            ai_go(who*-1)

def touch_l0(e):
    peo_go(0)

def touch_l1(e):
    peo_go(1)

def touch_l2(e):
    peo_go(2)

def touch_l3(e):
    peo_go(3)

def touch_l4(e):
    peo_go(4)

def touch_l5(e):
    peo_go(5)

def touch_l6(e):
    peo_go(6)

def touch_l7(e):
    peo_go(7)

def touch_l8(e):
    peo_go(8)
        

tk.Button(frame_top,text='人机对决',command=but1).pack(side=tk.LEFT)
tk.Button(frame_top,text='机器对决',command=but2).pack(side=tk.RIGHT)

update_chess()

l0.pack(side=tk.LEFT)
l1.pack(side=tk.LEFT)
l2.pack(side=tk.LEFT)
l3.pack(side=tk.LEFT)
l4.pack(side=tk.LEFT)
l5.pack(side=tk.LEFT)
l6.pack(side=tk.LEFT)
l7.pack(side=tk.LEFT)
l8.pack(side=tk.LEFT)

label_bottom.pack()

frame_cont1.pack()
frame_cont2.pack()
frame_cont3.pack()

frame_top.pack()
frame_cont.pack()
frame_bot.pack()

top.mainloop()