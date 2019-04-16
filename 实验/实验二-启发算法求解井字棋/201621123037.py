# 棋盘
class Board(object):
 def __init__(self):
  #self._board = '-'*9 # 坑！！
  
  self._board = ['-' for _ in range(9)]
  self._history = [] # 棋谱
  
  
 # 按指定动作，放入棋子
 def _move(self, action, take):
  if self._board[action] == '-':
   self._board[action] = take
   self._history.append((action, take)) # 加入棋谱
   
   
 # 撤销动作，拿走棋子
 def _unmove(self, action):
  self._board[action] = '-'
  self._history.pop()
  
  
 # 棋盘快照
 def get_board_snapshot(self):
  return self._board[:]


 # 取棋盘上的合法走法
 def get_legal_actions(self):
  actions = []
  for i in range(9):
   if self._board[i] == '-':
    actions.append(i)
  return actions

 # 判断走法是否合法
 def is_legal_action(self, action):
  return self._board[action] == '-'


 # 终止检测
 def teminate(self):
  board = self._board
  lines = [board[0:3], board[3:6], board[6:9], board[0::3], board[1::3], board[2::3], board[0::4], board[2:7:2]]
  if ['X']*3 in lines or ['O']*3 in lines or '-' not in board:
   return True
  else:
   return False


 # 胜负检查
 def get_winner(self):
  board = self._board
  lines = [board[0:3], board[3:6], board[6:9], board[0::3], board[1::3], board[2::3], board[0::4], board[2:7:2]]
  if ['X']*3 in lines:
   return 0
  elif ['O']*3 in lines:
   return 1
  else:
   return 2


 # 打印棋盘
 def print_b(self):
  board = self._board
  for i in range(len(board)):
   print(board[i], end='')
   if (i+1)%3 == 0:
    print()
    
 # 打印棋谱
 def print_history(self):
  print(self._history)
  
  
# 玩家
class Player(object):
 '''
 玩家只做两件事：思考、落子
  1. 思考 --> 得到走法
  2. 落子 --> 执行走法，改变棋盘
 '''
 def __init__(self, take='X'): # 默认执的棋子为 take = 'X'
  self.take=take
 def think(self, board):
  pass
 def move(self, board, action):
  board._move(action, self.take)
  
  
# 人类玩家
class HumanPlayer(Player):
 def __init__(self, take):
  super().__init__(take)
 def think(self, board):
  while True:
   action = input('Please input a num in 0-8:')
   if len(action)==1 and action in '012345678' and board.is_legal_action(int(action)):
    return int(action)



# 电脑玩家
class AIPlayer(Player):
 def __init__(self, take):
  super().__init__(take)
 def think(self, board):
  print('AI is thinking ...')
  take = ['X','O'][self.take=='X']
  player = AIPlayer(take)  # 假想敌！！！
  _, action = self.minimax(board, player)
  #print('OK')
  return action



 # 极大极小法搜索，α-β剪枝
 def minimax(self, board, player, depth=0) :
  if self.take == "O":
   bestVal = -10
  else:
   bestVal = 10
  if board.teminate() :
   if board.get_winner() == 0 :
    return -10 + depth, None
   elif board.get_winner() == 1 :
    return 10 - depth, None
   elif board.get_winner() == 2 :
    return 0, None
  for action in board.get_legal_actions() : # 遍历合法走法
   board._move(action, self.take)
   val, _ = player.minimax(board, self, depth+1) # 切换到 假想敌！！！
   board._unmove(action) # 撤销走法，回溯
   if self.take == "O" :
    if val > bestVal:
     bestVal, bestAction = val, action
   else :
    if val < bestVal:
     bestVal, bestAction = val, action
  return bestVal, bestAction


# 游戏
class Game(object):
 def __init__(self):
  self.board = Board()
  self.current_player = None
  
  
 # 生成玩家
 def mk_player(self, p, take='X'): # p in [0,1]
  if p==0:
   return HumanPlayer(take)
  else:
   return AIPlayer(take)


 # 切换玩家
 def switch_player(self, player1, player2):
  if self.current_player is None:
   return player1
  else:
   return [player1, player2][self.current_player == player1]


 # 打印赢家
 def print_winner(self, winner): # winner in [0,1,2]
  print(['player1获得了胜利','player2获得了胜利','平局'][winner])
  
  
 # 运行游戏
 def run(self):
  ps = input("请选择进行对抗的两个对象，先手在前:\n\t0.人\n\t1.AI\n例如:0 0（表示人人对战）\n")
  p1, p2 = [int(p) for p in ps.split(' ')]
  player1, player2 = self.mk_player(p1, 'X'), self.mk_player(p2, 'O') # 先手执X，后手执O
  print('\nGame start!\n')
  self.board.print_b() # 显示棋盘
  while True:
   self.current_player = self.switch_player(player1, player2) # 切换当前玩家
   action = self.current_player.think(self.board) # 当前玩家对棋盘进行思考后，得到招法
   self.current_player.move(self.board, action) # 当前玩家执行招法，改变棋盘
   self.board.print_b() # 显示当前棋盘
   if self.board.teminate(): # 根据当前棋盘，判断棋局是否终止
    winner = self.board.get_winner() # 得到赢家 0,1,2
    break
  self.print_winner(winner)
  print('Game over!')
  self.board.print_history()
  
if __name__ == '__main__':
    for i in range(10):
        Game().run()


