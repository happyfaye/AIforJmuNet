#include<stdio.h>
#include<windows.h>
typedef struct position {
    int x;
    int y;
}POS;   //坐标结构体
#define N 3
#define STEP 9
#define COMPUTER 1
#define MANAGER -1
#define INT_MAX 4096 
int CurrentDepth;
int player;
int chess[N][N];
int TempChess[N][N];    //虚拟的chess
int isEnd();
int Evaluate();
int CountBlank(POS SaveBlank[STEP]);
int MaxMinSearch(int depth);
void SetChess(POS MarkPos);
void RemoveChess(POS MarkPos);
void InitBoard();   //初始化边界
void WhoPlayFirst();
void ManPlay();
void ComPlay();
void DrawBoard();
POS BestPosMark;
int main()
{
    int step = 0;
    CurrentDepth = STEP-1;
    InitBoard();
    WhoPlayFirst();
    if (player == MANAGER)
    {
        for (step = 1;step <= STEP;)
        {
            ManPlay();
            DrawBoard();
            if (isEnd()==MANAGER)
            {
                printf("\n电脑1战胜电脑2！\n");
                system("pause");
                return 0;
            }
            step++;
            CurrentDepth--;
            if (CurrentDepth == 0)
            {
                printf("\n平局了！\n");
                system("pause");
                return 0;
            }
            player = (player == COMPUTER) ? MANAGER : COMPUTER;
            ComPlay();
            DrawBoard();
            if(isEnd()==COMPUTER)
            {
                printf("\n电脑2战胜了电脑1！\n");
                system("pause");
                return 0;
            }
            step++;
            CurrentDepth--;
            if (CurrentDepth == 0)
            {
                printf("\n平局了！\n");
                system("pause");
                return 0;
            }
            player = (player == COMPUTER) ? MANAGER : COMPUTER;
        }
    }
    if (player == COMPUTER)
    {
        for (step = 1;step <= STEP;)
        {
            ComPlay();
            DrawBoard();
            if (isEnd()==COMPUTER)
            {
                printf("\n电脑2战胜了电脑1！\n");
                system("pause");
                return 0;
            }
            step++;
            CurrentDepth--;
            if (CurrentDepth == 0)
            {
                printf("\n平局了！\n");
                system("pause");
                return 0;
            }
            player = (player == COMPUTER) ? MANAGER : COMPUTER;
            ManPlay();
            DrawBoard();
            if(isEnd()==MANAGER)
            {
                printf("\n电脑1战胜电脑2！\n");
                system("pause");
                return 0;
            }
            step++;
            CurrentDepth--;
            if (CurrentDepth == 0)
            {
                printf("\n平局了！\n");
                return 0;
            }
            player = (player == COMPUTER) ? MANAGER : COMPUTER;
        }
    }
    return 0;
}
void DrawBoard()
{
    int i, j;
    for (i = 0;i < N;i++)
    {
        printf("-------------\n");
        for (j = 0;j < N;j++)
        {
            if (chess[i][j] == COMPUTER)
                printf("| X ");
            else if (chess[i][j] == MANAGER)
                printf("| O ");
            else
                printf("|   ");
        }
        printf("|\n");
    }
    printf("-------------\n");
}
int isEnd()
{
    int i, j;
    int count = 0;
    for (i = 0;i < N;i++)   //行
    {
        count = 0;
        for (j = 0;j < N;j++)
            count += chess[i][j];
        if (count == 3 || count == -3)
            return count / 3;
    }
    for (j = 0;j < N;j++)   //列
    {
        count = 0;
        for (i = 0;i < N;i++)
            count += chess[i][j];
        if (count == 3 || count == -3)
            return count / 3;
    }
    count = 0;
    count = chess[0][0] + chess[1][1] + chess[2][2];
    if (count == 3 || count == -3)
        return count / 3;
    count = chess[0][2] + chess[1][1] + chess[2][0];
    if (count == 3 || count == -3)
        return count / 3;
    return 0;
}
int CountBlank(POS SaveBlank[STEP])
{
    int i, j;
    int count = 0;
    for (i = 0;i < N;i++)
    {
        for (j = 0;j < N;j++)
        {
            if (chess[i][j] == 0)   //若未被占
            {
                SaveBlank[count].x = i;
                SaveBlank[count].y = j;
                count++;
            }
        }
    }
    return count;
}
int Evaluate()
{
    int flag = 1;
    int i, j;
    int count = 0;
    if (isEnd() == COMPUTER)    //将自己的优势设置为无限大
        return INT_MAX;
    if (isEnd() == MANAGER)     //将自己的劣势设置为无限大
        return -INT_MAX;
    for (i = 0;i < N;i++)
    {
        for (j = 0;j < N;j++)
        {
            if (chess[i][j] == 0)
                TempChess[i][j] = COMPUTER; //将剩余的地方全放上电脑棋子
            else
                TempChess[i][j] = chess[i][j];
        }
    }
    //以下为电脑,记录若放满棋子后连成三个棋子的数量，越多则代表位置越重要
    for (i = 0;i < N;i++)
    {
        for (j = 0;j < N;j++)
            count += chess[i][j];
        count /= 3;
    }
    for (j = 0;j < N;j++)
    {
        for (i = 0;i < N;i++)
            count += chess[i][j];
        count /= 3;
    }
    count += (TempChess[0][0] + TempChess[1][1] + TempChess[2][2]) / 3;
    count += (TempChess[0][2] + TempChess[1][1] + TempChess[2][0]) / 3;

    //以下为玩家
    for (i = 0;i < N;i++)
    {
        for (j = 0;j < N;j++)
        {
            if (chess[i][j] == 0)
                TempChess[i][j] = MANAGER;  //将剩余的地方全放上电脑棋子
            else
                TempChess[i][j] = chess[i][j];
        }
    }
    for (i = 0;i < N;i++)
    {
        for (j = 0;j < N;j++)
            count += chess[i][j];
        count /= 3;
    }
    for (j = 0;j < N;j++)
    {
        for (i = 0;i < N;i++)
            count += chess[i][j];
        count /= 3;
    }
    count += (TempChess[0][0] + TempChess[1][1] + TempChess[2][2]) / 3;
    count += (TempChess[0][2] + TempChess[1][1] + TempChess[2][0]) / 3;

    return count;   //count是根据对电脑的优势和对玩家的优势相减综合算出的
}
void RemoveChess(POS MarkPos)
{
    chess[MarkPos.x][MarkPos.y] = 0;
    player = (player == COMPUTER) ? MANAGER : COMPUTER;
}
void SetChess(POS MarkPos)
{
    chess[MarkPos.x][MarkPos.y] = player;
    player = (player == COMPUTER) ? MANAGER : COMPUTER;
}
int MaxMinSearch(int depth)
{
    int BestValue = 0;
    int Value = 0;
    int i, count = 0;
    POS SaveBlank[STEP];
    if (COMPUTER == isEnd() || MANAGER == isEnd())
        return Evaluate();
    if (depth == 0)
        return Evaluate();
    if (player == COMPUTER)
        BestValue = -INT_MAX;
    if (player == MANAGER)
        BestValue = INT_MAX;
    count = CountBlank(SaveBlank);
    for (i = 0;i < count;i++)
    {
        POS MarkPos = SaveBlank[i];
        SetChess(MarkPos);
        Value = MaxMinSearch(depth - 1);
        RemoveChess(MarkPos);
        if (player == MANAGER)
        {
            if (Value < BestValue)
            {
                BestValue = Value;
                if (depth == CurrentDepth)
                {
                    BestPosMark = MarkPos;
                }
            }
        }
        else if (player == COMPUTER)
        {
            if (Value > BestValue)
            {
                BestValue = Value;
                if (depth == CurrentDepth)
                {
                    BestPosMark = MarkPos;
                }
            }
        }
    }
    return BestValue;
}
void ComPlay()
{
    MaxMinSearch(CurrentDepth);
    printf("\n电脑2落子的位置为：(%d,%d)\n", BestPosMark.x + 1, BestPosMark.y + 1);
    chess[BestPosMark.x][BestPosMark.y] = COMPUTER;
}
void ManPlay()
{
	MaxMinSearch(CurrentDepth);
    printf("\n电脑1落子的位置为：(%d,%d)\n", BestPosMark.x + 1, BestPosMark.y + 1);
    chess[BestPosMark.x][BestPosMark.y] = MANAGER;
}
void InitBoard()
{
    int i, j;
    for (i = 0;i < N;i++)
        for (j = 0;j < N;j++)
            TempChess[i][j] = chess[i][j] = 0;
}
void WhoPlayFirst()
{
    char ch;
    printf("欢迎试玩AI井字棋，请选择电脑落子先后：1---电脑1先手 2---电脑2先手\n");
    ch = getchar();
    player = (ch == '1') ? MANAGER : COMPUTER;
}