/**
 * Created by zhangyilin on 2019/3/24.
 */
import java.util.*;

public class CAndC {

    static   final char x ='x';
    static   final char o ='o';
    static   final char empty = '\0';
    static   final   int   INFINITY = 100 ;   // 表示无穷的值
    static   final   int   WIN = +INFINITY ;   // MAX的最大利益为正无穷
    static   final   int   LOSE = -INFINITY ;   // MAX的最小得益（即MIN的最大得益）为负无穷
    static   final   int   DOUBLE_LINK = INFINITY / 2 ;   // 如果同一行、列或对角上连续有两个，赛点
    static   final   int   INPROGRESS = 1 ;   // 仍可继续下（没有胜出或和局）
    static   final   int   DRAW = 0 ;   // 和局
    static   final   int [][] WIN_STATUS =   {
            { 0, 1, 2 },
            { 3, 4, 5 },
            { 6, 7, 8 },
            { 0, 3, 6 },
            { 1, 4, 7 },
            { 2, 5, 8 },
            { 0, 4, 8 },
            { 2, 4, 6 }
    };

    public static void main(String[] args) {

        int v,xwin=0,xlose=0,xdraw=0;
        for (int i = 0; i < 50; i++) {
            char[] array=new char[9];
            int state = INPROGRESS;
            //int step = 0;

            while (state != WIN && state != LOSE && state != DRAW) {
//                step++;
                v = minimaxX(array,3);
                array[v]=x;

                state = gameState(array);
                System.out.println("我选择下在 "+v);
                PrintBoard(array);
                if (state == WIN){
                    System.out.println("X机器玩家赢了");
                    break;
                }
                if (state == LOSE){
                    System.out.println("O机器玩家赢了");
                    break;
                }
                if (state == DRAW){
                    System.out.println("平局");
                    break;
                }

//                step++;
                v = minimaxO(array,2);
                array[v]=o;
                state = gameState(array);
                System.out.println("我选择下在 "+v);
                PrintBoard(array);

                if (state == WIN){
                    System.out.println("X机器玩家赢了");
                    break;
                }
                if (state == LOSE){
                    System.out.println("O机器玩家赢了");
                    break;
                }
                if (state == DRAW){
                    System.out.println("平局");
                    break;
                }

            }
            switch (state) {
                case WIN:
                    xwin++;
                    break;
                case LOSE:
                    xlose++;
                    break;
                case DRAW:
                    xdraw++;
                    break;
                default:
                    break;
            }
        }
        System.out.println("平局次数: "+xdraw+"   X机器玩家赢得次数: "+xwin+"   X机器玩家输的次数: "+xlose);
    }


//
//    public static void PrintBoard(char array[])
//    {
//        for (int i = 0; i <3 ; i++) {
//            for (int j = 0; j < 3; j++) {
//                System.out.print(array[i * 3 + j]+" ");
//            }
//            System.out.println();
//        }
//    }


    public static void PrintBoard(char array[]){
        char chess;
        for (int i = 0; i < 3; ++i)
        {
            for (int j = 0; j < 3; ++j)
            {
                chess = array[i * 3 + j];
                if (chess=='o'||chess=='x')
                    System.out.print(chess+" ");
                else
                    System.out.print("- ");
            }
            System.out.println();
        }
    }

    public  static int   gameState( char []   board )   {
        int   result = INPROGRESS;
        boolean   isFull =   true ;

        // is game over?
        for   ( int   pos = 0; pos < 9; pos++) {
            char   chess = board[pos];
            if   ( empty   == chess) {
                isFull =   false ;
                break ;
            }
        }
        // is Max win/lose?
        for   ( int [] status : WIN_STATUS) {
            char   chess = board[status[0]];
            if   (chess ==   empty ) {
                continue;
            }
            int   i = 1;
            for   (; i < status.length; i++) {
                if   (board[status[i]] != chess) {
                    break ;
                }
            }
            if   (i == status.length) {
                result = chess ==   x   ? WIN : LOSE;
                break ;
            }
        }
        if   (result != WIN & result != LOSE) {
            if   (isFull) {
                // is draw
                result = DRAW;
            }   else   {
                // check double link
                // finds[0]->'x', finds[1]->'o'
                int [] finds =   new   int [2];
                for   ( int [] status : WIN_STATUS) {
                    char   chess =   empty ;
                    boolean   hasEmpty =   false ;
                    int   count = 0;
                    for   ( int   i = 0; i < status.length; i++) {
                        if   (board[status[i]] ==   empty ) {
                            hasEmpty =   true ;
                        }   else   {
                            if   (chess ==   empty ) {
                                chess = board[status[i]];
                            }
                            if   (board[status[i]] == chess) {
                                count++;
                            }
                        }
                    }
                    if   (hasEmpty && count > 1) {
                        if   (chess ==   x ) {
                            finds[0]++;
                        }   else   {
                            finds[1]++;
                        }
                    }
                }
                // check if two in one line
                if   (finds[1] > 0) {
                    result = -DOUBLE_LINK;
                }   else   if   (finds[0] > 0) {
                    result = DOUBLE_LINK;
                }
            }
        }
        return   result;
    }

    /**
     * 以'x'的角度来考虑的极小极大算法
     */

    public  static int   minimaxX( char [] board,   int   depth){
        int [] bestMoves =   new   int [9];
        int   index = 0;
        int state = INPROGRESS;
        int   bestValue = - INFINITY ;

        System.out.println("开始思考");
        for ( int  pos=0; pos<9; pos++){
            if (board[pos]== empty ) {
                board[pos] = x;
                state = gameState(board);
                if (state == WIN) {
                    System.out.println("我如果下在 " + pos + ",将导致 胜利 ");
                }
                else if (state == DRAW) {
                    System.out.println("我如果下在 " + pos + ",将导致 平局 ");
                }
                else {
                    board[pos] = o;
                    state = gameState(board);
                    if (state == LOSE) {
                        System.out.println("我如果下在 " + pos + ",将导致 平局 ");
                    }
                    else {
                        if(state == -50)
                            System.out.println("我如果下在 " + pos + ",将导致 失败");
                        else
                            System.out.println("我如果下在 " + pos + ",将导致 平局");

                    }

                }
                board[pos] = x;
                int   value = min(board, depth);
                if (value > bestValue){
                    bestValue = value;
                    index = 0;
                    bestMoves[index] = pos;

                }
                else if (value == bestValue){
                    index++;
                    bestMoves[index] = pos;

                }

                board[pos] =   empty ;

            }

        }

        if (index>=1){
            index = ( new   Random (System. currentTimeMillis ()).nextInt()>>>1)%index;
        }
        return   bestMoves[index];

    }

    public  static int   minimaxO( char [] board,   int   depth){
        int [] bestMoves =   new   int [9];
        int   index = 0;
        int state = INPROGRESS;
        int   bestValue = + INFINITY ;
        System.out.println("开始思考");

        for ( int  pos=0; pos<9; pos++){

            if (board[pos]== empty ){
                board[pos] = o;
                state = gameState(board);
                if(state == LOSE)
                {
                    System.out.println("我如果下在 " + pos + ",将导致 胜利 ");
                }
                else{
                    board[pos] = x;
                    state = gameState(board);
                    if (state == WIN){
                        System.out.println("我如果下在 " + pos + ",将导致 平局 ");
                    }
                    else {
                        if (state == 50)
                            System.out.println("我如果下在 " + pos + ",将导致 平局");
                        else {
                            System.out.println("我如果下在 " + pos + ",将导致 失败");
                        }
                    }
                }
//                else if (state==DRAW){
//                    System.out.println("我如果下在 " + pos + ",将导致 平局 ");
//                }
//                else if(state == WIN){
//                    System.out.println("我如果下在 " + pos + ",将导致 失败");
//                }
//                else {
//                    System.out.println("我如果下在 " + pos + ",将导致 平局 ");
//                }
                board[pos] = o;
                int   value = max(board, depth);
                if (value<bestValue){
                    bestValue = value;
                    index = 0;
                    bestMoves[index] = pos;

                } else
                if (value==bestValue){
                    index++;
                    bestMoves[index] = pos;

                }

                board[pos] =   empty ;
            }

        }

        if (index>1){
            index = ( new   Random (System. currentTimeMillis ()).nextInt()>>>1)%index;

        }
        return   bestMoves[index];

    }



    /**
     * 对于'x'，估值越大对其越有利
     */
    public  static  int   max( char [] board,   int   depth){

        int   evalValue =   gameState (board);

        boolean   isGameOver = (evalValue== WIN   || evalValue== LOSE   || evalValue== DRAW );
        if (depth==0 || isGameOver){
            return   evalValue;
        }

        int   bestValue = - INFINITY ;
        for ( int   pos=0; pos<9; pos++){

            if (board[pos]== empty ){
                // try
                board[pos] =   x ;

                //   maximixing
                bestValue = Math. max (bestValue, min(board, depth-1));

                // reset
                board[pos] =   empty ;
            }

        }

        return   evalValue;

    }
    /**
     * 对于'o'，估值越小对其越有利
     */
    public  static int   min( char [] board,   int   depth){

        int   evalValue =   gameState (board);

        boolean   isGameOver = (evalValue== WIN   || evalValue== LOSE   || evalValue== DRAW );
        if (depth==0 || isGameOver){
            return   evalValue;
        }

        int   bestValue = + INFINITY ;
        for ( int   pos=0; pos<9; pos++){

            if (board[pos]== empty ){
                // try
                board[pos] =   o ;

                //   minimixing
                bestValue = Math.min(bestValue, max(board, depth-1));

                // reset
                board[pos] =   empty ;
            }

        }

        return   evalValue;

    }


}
