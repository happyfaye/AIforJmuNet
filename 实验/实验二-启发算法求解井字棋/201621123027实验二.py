# 穷举出所有可能棋局情况作为判断输入，选择胜率最高的位置下子
import time
import functools
import random
import pickle
# import copy
# import numpy

class Chess:
    '''
    棋盘类，提供私有棋盘，以及落子、判断胜局方法
    '''
    def __init__(self,size:tuple,win:int):
        '''
        为实例初始化自己的棋盘大小,定义几连子获胜
        '''
        self.size = size
        self.win = win
        self.__state = self.get_chess()

    def __str__(self):
        '''
        将当前棋盘转换为网格格式字符串
        :return: 网格格式字符串表示的当前棋盘
        '''
        str_ = ''
        for i in self.__state:
            for j in i:
                str_ += str(j) + '\t'
            str_ += '\n'
        return str_

    def set_position(self,position:tuple,player_id:int):
        '''
        安插玩家落子位置，利用编号区分不同玩家，提供位置值错误、位置重复校验并抛出相应自定义Inp_excep错误
        :param position: 位置用（x,y）表示
        :param player: 区分玩家编号
        :return: 是否胜出
        '''
        try:
            x = int(position[0]) - 1
            y = int(position[1]) - 1
        except TypeError:
            raise Inp_excep('您输入的落子位置不存在')
        if x not in range(self.size[0]) or y not in range(self.size[1]):
            raise Inp_excep('您输入的落子位置不存在')
        # x = (position-1) // 3
        # y = abs((position-1) % 3)
        if self.__state[x][y]:
            raise Inp_excep('该位置已有棋子！')
        self.__state[x][y] = player_id

        return self.__get_result((x,y))

    def __get_result(self,pos):
        if self.max_done(pos) >= self.win:
            return self.__state[pos[0]][pos[1]]
        for i in self.__state:
            for j in i:
                if not j:
                    return None
        return 0

    # def is_win(self):
    #     '''
    #     判断当前棋局是否结束,并返回获胜玩家编号
    #     :return: 胜利玩家编号
    #     '''
    #     win_line = copy.deepcopy(self.__state)
    #     st = self.__state
    #
    #     oth =  [ [st[0][0],st[1][0],st[2][0]],[st[0][1],st[1][1],st[2][1]],[st[0][2],st[1][2],st[2][2]],
    #              [st[0][0],st[1][1],st[2][2]],[st[0][2],st[1][1],st[2][0]] ]
    #     win_line.extend(oth)
    #     for line in win_line:
    #         if line[0] is line[1] is line[2] and line is not 0:
    #             return line[0]
    #     for i in self.__state:
    #         for j in i:
    #             if j == 0:
    #                 return None
    #     return -1

    def max_done(self,position:tuple):
        '''
        调用__extend_延展八个方向递归求得最大成线值
        :param position: 包含x,y落子位置坐标的元祖
        :return: 最大连线值
        '''
        done_num = []
        dires = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(4):
            done_num.append(self.__extend_(position, dires[i]) + 1 + self.__extend_(position, dires[-i-1]))
        max_ = max(done_num)
        # print(max_)
        return max_
        # return max(done_num)

    def __extend_(self,position:tuple,direction:tuple):
        '''
        判定最大成线子数用到的递归延展函数
        :param position: 当前位置（x，y）
        :param direction: 当前延展方向（x，y），abx(x) == abs(y） == 1 表示
        :return: 继续延展成子数量加上本身的1
        '''
        new_position = (position[0] + direction[0],position[1] + direction[1])
        if new_position[0] not in range(self.size[0]) or new_position[1] not in range(self.size[1]):
            return 0
        if self.__state[new_position[0]][new_position[1]] and \
                self.__state[new_position[0]][new_position[1]] == self.__state[position[0]][position[1]]:
            return self.__extend_(new_position,direction) + 1
        return 0

    def get_chess(self):
        return [[0 for i in range(self.size[1])] for i in range(self.size[0])]

    def reset_chess(self):
        self.__state = self.get_chess()

class Inp_excep(Exception):
    '''
    用户输入错误总类
    '''
    def __init__(self,info:str):
        self.info = info


class Player:
    '''
    玩家对象，实例属性有player名称、player_id、对局棋盘。初始化一方法为棋盘落子方法的偏函数
    '''
    def __init__(self,name:str,id:int,chess:Chess):
        self.name = name
        self.id = id
        self.chess = chess
        self.turn_on = functools.partial(chess.set_position, player_id=self.id)


class AI(Player):
    '''
    定义电脑棋手类，继承自玩家，拥有额外属性功能
    '''

    def __init__(self, name: str, id: int, chess: Chess):
        super(AI,self).__init__(name,id,chess)
        self.virtual_chess = Chess(self.chess.size,self.chess.win)

        try:
            with open("3_3.pkl", "rb") as file:
                self.all_state = pickle.load(file)
        except:
            self.all_state = self.__get_all_state()
            with open("3_3.pkl", "wb") as file:
                pickle.dump(self.all_state, file, True)

        self.me_win = 2

    def __get_all_state(self):
        row = self.chess.size[0]
        col = self.chess.size[1]
        chess = [[0 for i in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                chess[i][j] = i * row + j + 1
        chess_flat = []
        for i in chess:
            chess_flat.extend(i)
        path = []
        all_state = {'first_win': [], 'second_win': [], 'draw': []};

        self.__iter_fun(chess_flat,path,all_state)
        return all_state

    def __iter_fun(self,chess_flat: list, path: list,all_state):
        for sing in chess_flat:
            # 如果当前路径(path)中已包含该位置，则跳过
            if sing in path:
                continue
            # 调用接口判断结果，若分出胜负, 保存结果并继续下一分支遍历
            path.append(sing)
            result = self.__get_result(path)
            if result == 1 or result == 2 or result == 0:
                res = {1: 'first_win', 2: 'second_win', 0: 'draw'}
                all_state[res[result]].append(path.copy())
                path.remove(sing)
                continue
            # 未结束继续下一层遍历
            self.__iter_fun(chess_flat, path,all_state)
            # 该分支遍历结束继续遍历该层次下一分支
            path.remove(sing)
            continue

    def __get_result(self,set_list:list):
        flag = 1
        id = 1
        for pos in set_list:
            x = (pos - 1) // self.chess.size[1] + 1
            y = (pos - 1) % self.chess.size[1] + 1
            # print(pos)
            over = self.virtual_chess.set_position((x,y),id)
            if over != None:
                self.virtual_chess.reset_chess()
                return over
            id += flag
            flag *= -1
        self.virtual_chess.reset_chess()

    def reset_AI(self):
        with open("3_3.pkl", "rb") as file:
            self.all_state = pickle.load(file)
        self.me_win = 2

    def feedback(self,player_posion, fault: bool = 0):
        row = self.chess.size[0]
        col = self.chess.size[1]
        if not player_posion:
            self.me_win = 1
            first_ai_posiion = random.randint(1, row * col)
            self.__shrink(first_ai_posiion)
            x = (first_ai_posiion - 1) // col + 1
            y = (first_ai_posiion - 1) % col + 1
            return (x, y)

        ai_position = (int(player_posion[0]) - 1) * col + int(player_posion[1])
        self.__shrink(ai_position)
        next = self.__calculate()
        x = (next - 1) // col + 1
        y = (next - 1) % col + 1
        self.__shrink(next)
        return (x, y)

    def __shrink(self,ai_position: int):
        for key, values in self.all_state.items():
            len = values.__len__()
            for reverse_index in range(len - 1, -1, -1):
                if values[reverse_index][0] == ai_position:
                    values.pop(reverse_index)

    def __calculate(self, regula: list = [2, -2, 1]):
        refer = {}
        res = {'first_win': regula[0], 'second_win': regula[1], 'draw': regula[2]}
        for key, values in self.all_state.items():
            for value in values:
                if value[0] not in refer:
                    refer[value[0]] = res[key]
                else:
                    refer[value[0]] += res[key]
        print(refer)
        if self.me_win == 1:
            return max(refer, key=refer.get)
        if self.me_win == 2:
            return min(refer, key=refer.get)



# 创建各个实例对象
chess = Chess((3,3),3)
player_one = Player('学号尾号027',1,chess)
player_two = Player('玩家二',2,chess)

# 业务逻辑的函数封装：某玩家落子到判断胜负并打印
def player_inp(player:Player,pre_pos = 0):
    if player.name.startswith('AI'):
        print('正在计算，请稍后...'.format(player.name))
        before = time.clock()
        pos = player.feedback(pre_pos)
        after = time.clock()
        print('用时{}，{}计算出的落子位置为：({},{})'.format(after-before,player.name,pos[0],pos[1]))
        res = player.turn_on(list(pos))
        print(player.chess)
        pre_pos = list(pos)
    else:
        while True:
            inp = input('请{}落子【行 列】：'.format(player.name)).split()
            try:
                res = player.turn_on(inp)
                pre_pos = inp.copy()
                print(player.chess)
                break
            except Inp_excep as err:
                print(err.info,end=' ')
                continue
            except:
                print('输入行列号即可，以空格为区分\t', end=' ')
                continue

    if res and res > 0:
        print('游戏结束，{}获胜！'.format(player.name))
        print(player.chess)
        player.chess.reset_chess()
        raise Inp_excep("本局已结束")
    elif res == 0:
        print('游戏结束，该局为平局！')
        print(player.chess)
        player.chess.reset_chess()
        raise Inp_excep("本局已结束")
    print(pre_pos)
    print('*'*20)
    return pre_pos



inp = input('输入1进入AI对战模式，输入2进入双人对战模式，3为AI互博：')
if inp == '2':
    while True:
        try:
            player_inp(player_one)
            player_inp(player_two)
        except Inp_excep as err:
            print(err.info,end='\t')
            input('按下回车继续开始下一局...')
            print('\n已开启新一轮')

if inp == '3':
    print('请等候AI创建(大约两分钟)...')
    before = time.clock()
    AI_nine = AI('AI_nine', 9, chess)
    AI_eight = AI('AI_eight', 8, chess)
    after = time.clock()
    print('AI创建成功，用时：', after - before)

    player_inp(AI_nine)
    while(True):
        try:
            pre_pos = player_inp(AI_eight)
            player_inp(AI_nine,pre_pos)
        except Inp_excep as err:
            print(err.info,end='\t')
            input('按下回车继续开始下一局...')
            AI_nine.reset_AI()
            AI_eight.reset_AI()
            print('\n已开启新一轮')

            player_inp(AI_nine)

if inp == '1':
    print('请等候AI创建(大约两分钟)...')
    before = time.clock()
    AI_nine = AI('AI_nine', 9, chess)
    after = time.clock()
    print('AI创建成功，用时：', after - before)

    player_inp(AI_nine)
    while (True):
        try:
            pre_pos = player_inp(player_one)
            player_inp(AI_nine, pre_pos)
        except Inp_excep as err:
            print(err.info, end='\t')
            input('按下回车继续开始下一局...')
            AI_nine.reset_AI()
            print('\n已开启新一轮')

            player_inp(AI_nine)

