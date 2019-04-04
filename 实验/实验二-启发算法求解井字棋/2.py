#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
from abc import ABCMeta, abstractmethod

ROW = COL = 3  # 棋盘大小
SPACE = '-'  # 空格标签
COMPUTERa = 'COMPUTERa'  # 电脑棋子标签
COMPUTERb = 'COMPUTERb'  # 电脑棋子标签
a=0
b=0
aa=0
# 棋盘是否有空位
def empty(board):
    if board.count(SPACE) == 0:
        return False
    else:
        return True


# 判断player是否胜利
def winner(board, player):
    """
        --------------
        | 0 || 1 || 2 |
        | 3 || 4 || 5 |
        | 6 || 7 || 8 |
        --------------
        获胜的算法：
        012     345     678
        036     147     258
        048     246
    """
    wins = [[board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]],
            [board[0], board[3], board[6]], [board[1], board[4], board[7]], [board[2], board[5], board[8]],
            [board[0], board[4], board[8]], [board[2], board[4], board[6]]]            #穷举出所有可能赢棋的方法
    state = [player, player, player]                    
    if state in wins:
        return True
    else:
        return False


class Player(metaclass=ABCMeta):

    def __init__(self, chess):
        self.chess = chess

    @abstractmethod
    def move(self):
        pass


class Computera(Player):

    def __init__(self, chess='O'):
        Player.__init__(self, chess)

    def minimax(self, board, player, next_player, alpha=-2, beta=2):
        if winner(board, COMPUTERa):  # 电脑胜利
            return +1
        if winner(board, COMPUTERb):  # 人类胜利
            return -1
        elif not empty(board):
            return 0  # 平局

        for move in range(ROW * COL):
            if board[move] == SPACE:  # 尝试下棋
                board[move] = player  # 记录
                val = self.minimax(board, next_player, player, alpha, beta) 
                board[move] = SPACE  # 重置
                if player == COMPUTERa:  # 极大 max value
                    if val > alpha:
                        alpha = val
                    if alpha >= beta:  # 剪枝
                        return beta
                else:  # 极小 min value
                    if val < beta:
                        beta = val
                    if beta <= alpha:  # 剪枝
                        return alpha

        if player == COMPUTERa:
            return alpha
        else:
            return beta

    def move(self, board):
        best = -2
        my_moves = []
        for move in range(ROW * COL):
            if board[move] == SPACE:  # 尝试下棋
                board[move] = COMPUTERa  # 记录
                score = self.minimax(board,COMPUTERb , COMPUTERa)
                board[move] = SPACE  # 重置

                if score > best:  # 找到更优的位置
                    best = score
                    my_moves = [move]
                if score == best:  # 一样优秀的位置
                    my_moves.append(move)

        pos = random.choice(my_moves)  # 随机挑出一个位置
        board[pos] = COMPUTERa




class Computerb(Player):

    def __init__(self, chess='O'):
        Player.__init__(self, chess)

    def minimax(self, board, player, next_player, alpha=-2, beta=2):
        if winner(board, COMPUTERa):  # 电脑胜利
            return +1
        if winner(board, COMPUTERb):  # 人类胜利
            return -1
        elif not empty(board):
            return 0  # 平局

        for move in range(ROW * COL):
            if board[move] == SPACE:  # 尝试下棋
                board[move] = player  # 记录
                val = self.minimax(board, next_player, player, alpha, beta) 
                board[move] = SPACE  # 重置
                if player == COMPUTERa:  # 极大 max value
                    if val > alpha:
                        alpha = val
                    if alpha >= beta:  # 剪枝
                        return beta
                else:  # 极小 min value
                    if val < beta:
                        beta = val
                    if beta <= alpha:  # 剪枝
                        return alpha

        if player == COMPUTERb:
            return alpha
        else:
            return beta

    def move(self, board):
        best = -2
        my_moves = []
        for move in range(ROW * COL):
            if board[move] == SPACE:  # 尝试下棋
                board[move] = COMPUTERb  # 记录
                score = self.minimax(board,COMPUTERb , COMPUTERa)
                board[move] = SPACE  # 重置

                if score > best:  # 找到更优的位置
                    best = score
                    my_moves = [move]
                if score == best:  # 一样优秀的位置
                    my_moves.append(move)

        pos = random.choice(my_moves)  # 随机挑出一个位置
        board[pos] = COMPUTERb




class Game:
    def __init__(self):
        # 初始化游戏
        self.board = [SPACE] * (ROW * COL)
        self.computera = Computera()
        self.computerb = Computerb()
        self.computera.chess = 'X'
        self.computerb.chess = 'O'
        self.current_player = self.computera

    # 切换玩家
    def switch(self):
        if self.current_player == self.computera:
            self.current_player = self.computerb
        else:
            self.current_player = self.computera

    def render(self):
        print('***************')
        for i in range(ROW):
            for j in range(COL):
                k = i * ROW + j
                if self.board[k] == COMPUTERb:
                    print('|', self.computerb.chess, '|', end='')
                elif self.board[k] == COMPUTERa:
                    print('|', self.computera.chess, '|', end='')
                else:
                    print('|', self.board[k], '|', end='')
            print()
        print('***************')

    def start(self):
        # 游戏状态机
        global a,b,aa
        while True:
            self.current_player.move(self.board)     #走棋
            if winner(self.board,COMPUTERb ):
                print()
                print("  电脑b获得胜利(*^ω^*)")
                a+=1
                return 0
            elif winner(self.board, COMPUTERa):
                print()
                print("  电脑a获得胜利(*^ω^*)")
                b+=1
                return 0
            elif not empty(self.board):
                print()
                print("  两台电脑打成平局( ˃̶̤́ ꒳ ˂̶̤̀ )")
                aa+=1
                return 0
            # 切换玩家
            self.switch()
        

if __name__ == '__main__':
        for i in range(1,51):
            Game().start()
        print("第一台电脑获得胜利的次数是：",a)
        print("第二台电脑获得胜利的次数是：",b)
        print("平局的次数是：",aa)
