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
                        

#AIPlayer
def minimax(board,depth):
    bestMoves=[0,0,0,0,0,0,0,0,0]
    index=0
    
    bestValue = -INFINITY
    for p in range(0,9):
        if board[p]=='□':
            board[p]='x'          
            value=Min(board,depth)
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


def AIplayerset():
    global board
    p=minimax(board,3)
    if 0<=p and p<=8:
        if board[p]=='□':
            board[p]='x'
        

    
def printGame(error=0):
    global board
    L1=board[0:3]
    L2=board[3:6]
    L3=board[6:9]
    print("棋盘：")
    print(" ".join(L1))
    print(" ".join(L2))
    print(" ".join(L3))
        
    if error==1:
        print("\n输入坐标越界，请重新输入！")

    elif error==2:
        print("\n输入的坐标已经有棋子，请重新输入！")

    

def playerSet():
    global board
    print("请输入落子序号（从左到右，从上到下依次为0~8）：")
    p=int(input())
    if 0<=p and p<=8:
        if board[p]=='□':
            board[p]='●'
            printGame()
        else:
            printGame(2)
            playerSet()
    else:
        printGame(1)
        playerSet()
    
    
#playerSet()

def winner():
    global board
    printGame()
    if gameState(board)==WIN:
        print("\n游戏结束！胜利者：机器\n")
        os.system("pause")
    elif gameState(board)==LOSE:
        print("\n游戏结束！胜利者：玩家\n")
        os.system("pause")
    elif gameState(board)==DRAW:
        print("\n棋逢对手！201621123033和AI双方平局！\n")
        os.system("pause")

while True:
    winner()
    AIplayerset()
    winner()
    playerSet()
    
    
