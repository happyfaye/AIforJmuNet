import random
import math
import os
INFINITY= 100
WIN = + INFINITY
LOSE = - INFINITY
DOUBLE_LINK = INFINITY/2
INPROGRESS = 1
DRAW =0
WIN_STATUS = ['012','345','678','036','147','258','048','246']#胜利情况
board=['□','□','□','□','□','□','□','□','□']
win=0
lose=0
draw=0
flag=0
k=0

def gameState(board):
    result = INPROGRESS
    isFull = True
    
    #is game over?
    for p in range(0,9):
        chess = board[p]
        if '□'==chess:
            isFull=False

    
    #is Max win/lose?
    for status in WIN_STATUS:
        chess = board[int(status[0])]
        if chess==None:
            break
        j=1
        while j <len(status):
            if board[int(status[j])]!=chess:
                break
            j+=1
            
        if j == len(status):
            if chess == 'x':
                result=WIN
            elif chess == '●':
                result=LOSE
            break
            
    if result!=WIN and result!=LOSE:
        if isFull==True:
            result=DRAW
        else:
            #check double link
            #finds[0]->'x',finds[1]->'●'
            finds=[0,0]
            for status in WIN_STATUS:
                chess = '□'
                hasEmpty = False
                count=0
                for i in range(0,len(status)):
                    if board[int(status[i])] == '□':
                        hasEmpty=True
                    else:
                        if chess == '□':
                            chess = board[int(status[i])]
                        if board[int(status[i])]==chess:
                            count += 1
                if hasEmpty and count>1:
                    if chess == 'x':
                        finds[0] += 1
                    else:
                        finds[1] += 1
            
            #check if two in one line
            if finds[1]>0:
                result = -DOUBLE_LINK
            elif finds[0]>0:
                result = +DOUBLE_LINK
            
    return result
                        

#AIPlayer1
def minimax(board,depth):
    bestMoves=[0,0,0,0,0,0,0,0,0]
    index=0
    
    bestValue = -INFINITY
    for p in range(0,9):
        if board[p]=='□':
            board[p]='x'          
            value=Min(board,depth)
            if value==DRAW:
               print('我如果下在 %d ,将导致 平局' %p)
            elif value==WIN:
               print('我如果下在 %d ,将导致 胜利' %p)
            elif value==LOSE:
               print('我如果下在 %d ,将导致 失败' %p)
            if value>bestValue:
                bestValue = value
                index=0
                bestMoves[index]=p

            elif value == bestValue:
                index += 1
                bestMoves[index]=p
            
                
            board[p]='□'

            
    if index>1:
        index = random.randint(0,index)
    
    return bestMoves[index]



#对于AI,估值越大对其越有利
def Max(board,depth):
    evalValue = gameState(board)
    isGameOver=(evalValue==WIN or evalValue==LOSE or evalValue==DRAW)
    if depth==0 or isGameOver==True:
        return evalValue
    
    bestValue = -INFINITY
    for p in range(0,9):
        if board[p]=='□':
            board[p]=='x'
            bestValue=max(bestValue,Min(board,depth-1))
            board[p]='□'
            
    return evalValue

#对于假想敌，估值越小对其越有利
def Min(board,depth):
    evalValue=gameState(board)
    isGameOver=(evalValue==WIN or evalValue==LOSE or evalValue==DRAW)
    if depth==0 or isGameOver==True:
        return evalValue
    
    bestValue = +INFINITY
    for p in range(0,9):
        if board[p]=='□':
            board[p]=='●'
            bestValue=min(bestValue,Max(board,depth-1))
            board[p]='□'
            
    return evalValue


def AIplayerset1():
    global board
    p=minimax(board,3)
    if 0<=p and p<=8:
        if board[p]=='□':
            board[p]='x'
            print('我选择下在 %d' %p)
            printGame(board)
            

def AIplayerset2():
    global board
    p=minimax(board,2)
    if 0<=p and p<=8:
        if board[p]=='□':
            board[p]='●'
            print('我选择下在 %d' %p)
            printGame(board)


def printGame(error=0):
    global board
    L1=board[0:3]
    L2=board[3:6]
    L3=board[6:9]
    print("棋盘：")
    print(" ".join(L1))
    print(" ".join(L2))
    print(" ".join(L3))



def winner():
    global board
    global win,lose,draw,flag
    #printGame()
    if gameState(board)==WIN:
        print("\n游戏结束！胜利者：机器1\n")
        win+=1
        flag=1
    elif gameState(board)==LOSE:
        print("\n游戏结束！胜利者：机器2\n")
        lose+=1
        flag=1
    elif gameState(board)==DRAW:
        print("\n棋逢对手！双方平局！\n")
        draw+=1
        flag=1

def reset():
    global board,flag
    board=['□','□','□','□','□','□','□','□','□']
    flag=0
    print('reset')

while True:
    global k
    if flag==1:
        k+=1
        reset()
        print('k:%d' %k)
    AIplayerset1()
    winner()
    if flag==1:
        k+=1
        reset()
        print('k:%d' %k)
    AIplayerset2()
    winner()

    if k==50:
        print(draw)
        print(win)
        print(lose)
        print('平局次数：%d  x机器玩家赢的次数：%d  x机器玩家输的次数：%d '%(draw,win,lose))
        break
    
