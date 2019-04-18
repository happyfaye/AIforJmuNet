# Tic-Tac-Toe 井字棋游戏
# 全局常量

X = "X"
O = "O"
EMPTY = " "
# 询问是否继续


def ask_yes_no(question):
    response=None;
    while response not in("y","n"):
        response=input(question).lower()
    return response
#输入位置数字
def ask_number(question ,low,high):
    response=None
    while response not in range(low,high):
        response=int(input(question))
    return response
#询问谁先走，先走方为X,后走方为O
#函数返回计算机方，玩家的角色代号
def pieces():
    go_first=ask_yes_no("玩家你是否先走（y/n):")
    if go_first=="y":
        print("\n玩家你先走.")
        human=X
        computer=O
    else:
        print("\n计算机先走.")
        computer=X
        human=O
    return computer,human
#产生新的棋盘
def new_board():
    board=[]
    for square in range(9):
        board.append(EMPTY)
    return board
#显示棋盘
def display_board(board):
    board2=board[:]
    for i in range(len(board)):
        if board[i]==EMPTY:
            board2[i]=i
    print("\t",board2[0],"|",board2[1],"|",board2[2])
    print("\t","----------")
    print("\t",board2[3],"|",board2[4],"|",board2[5])
    print("\t", "----------")
    print("\t",board2[6],"|",board2[7],"|",board2[8],"\n")
    #产生可以合法走棋位置序列（也就是还未下过子位置）
def legal_moves(board):
    moves=[]
    for square in range(9):
        if board[square]==EMPTY:
            moves.append(square)
    return moves
    #判断输赢
def winner(board):
        # 所有赢得可能情况，例如（0,1,2）就是第一行，（0,4,8,），（2,4,6）就是对角线
    WAYS_TO_WIN=((0,1,2,),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]]!=EMPTY:
            winner=board[row[0]]
            return winner
            #棋盘没有空位置
    if EMPTY not in board:
        return "TIE"
    return False
        #人走棋
def human_move (board,human):
    legal =legal_moves(board)
    move =None
    while move not in legal:
        move=ask_number("201621123016走哪个位置？（0-8）：",0,9)
        if move not in legal:
            print("\n此位置已经落过子了")
                    #print("Fine...")
    return  move
        #计算机走棋
def computer_move(board,computer ,human):
    board=board[:]
            #按优劣顺序排序的下棋走子
    BEST_MOVES=(4,0,2,6,8,1,3,5,7) #最佳下棋位置顺序表
            #如果计算机能赢，就走那个位置
    for move in legal_moves(board):
            board[move]=computer
            if winner(board)==computer:
                print("计算机下棋位置...",move)
                return move
                #取消走棋方案
            board[move]=EMPTY
            #如果玩家能赢就堵住那个位置
    for move in legal_moves(board):
            board[move]=human
            if winner(board)==human:
                print("计算机下棋位置...",move)
                return move
                #取消走棋方案
            board[move]=EMPTY
            #如果不是上面情况，也就是这一轮赢不了
            #则是从最佳下棋位置表中挑出第一个合法位置
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print("计算机下棋位置....",move)
            return move
        #转换角色
def next_turn(turn):
    if turn ==X:
         return  O
    else:
        return  X
        #主函数
def main():
        computer,human=pieces()
        turn =X
        board=new_board()
        display_board(board)
        while not winner(board):
            if turn ==human:
                move=human_move(board,human)
                board[move]=human
            else:
                move=computer_move(board,computer,human)
                board[move]=computer
            display_board(board)
            turn=next_turn(turn)   #转换角色
                    #游戏结束输出输赢或和棋信息
        the_winner=winner(board)
        if the_winner==computer:
            print("计算机赢！\n")
        elif the_winner==human:
            print("玩家赢！\n")
        elif the_winner=="TIE":
            print("平局，游戏结束\n")

main()
input("按任意键退出游戏")
