package xo;

import java.util.Random;
import java.util.Scanner;

public class Main {
	static   final   int   INFINITY = 100 ;   // 表示无穷的值
	static   final   int   WIN = +INFINITY ;   // MAX的最大利益为正无穷
	static   final   int   LOSE = -INFINITY ;   // MAX的最小得益（即MIN的最大得益）为负无穷
	static   final   int   DOUBLE_LINK = INFINITY / 2 ;   // 如果同一行、列或对角上连续有两个，赛点
	static   final   int   INPROGRESS = 1 ;   // 仍可继续下（没有胜出或和局）
	static   final   int   DRAW = 0 ;   // 和局

	static   final   char  empty = '*';  
	static   final   char  x = 'x';  
	static   final   char  o = 'o';  
	static   final   int [][] WIN_STATUS =   {
	      {   0, 1, 2 },
	      { 3, 4, 5 },
	      { 6, 7, 8 },
	      { 0, 3, 6 },
	      { 1, 4, 7 },
	      { 2, 5, 8 },
	      { 0, 4, 8 },
	      { 2, 4, 6   }
	};

	//开局时，每个位置的估值
	static   final   int []   INITIAL_POS_VALUE   = {
	      3, 2, 3,
	      2, 4, 2,
	      3, 2, 3
	};
	
    public static void person(char[] num)
    {
        int x,y;
        do
        {
        	Scanner sc = new Scanner(System.in);
        	System.out.println("请输入落子坐标（以空格分开，介于[0-2] [0-2]之间）：");
            x = sc.nextInt();
            y = sc.nextInt();
            if(num[x*3+y] == empty) {
            	break;
            }else
            	System.out.println("输入的坐标已经有棋子，请重新输入！");
        } while (true);
        System.out.println("你所下子为(" + x + "," + y + ")");
        num[x*3+y] = 'o'; 
        System.out.println(num[0]+" "+num[1]+" "+num[2]);
        System.out.println(num[3]+" "+num[4]+" "+num[5]);
        System.out.println(num[6]+" "+num[7]+" "+num[8]);
    }
    
    public static void computer(char num[])
    {
    	int moves = minimax(num,3);
        num[moves] = 'x'; 
        System.out.println("电脑下子为(" + moves/3 + "," + moves%3 + ")");
        System.out.println(num[0]+" "+num[1]+" "+num[2]);
        System.out.println(num[3]+" "+num[4]+" "+num[5]);
        System.out.println(num[6]+" "+num[7]+" "+num[8]);
    }
    

    public static void computerByO(char num[])
    {
    	int moves = minimax(num,2);
        num[moves] = 'o'; 
        System.out.println("电脑o下子为(" + moves/3 + "," + moves%3 + ")");
        System.out.println(num[0]+" "+num[1]+" "+num[2]);
        System.out.println(num[3]+" "+num[4]+" "+num[5]);
        System.out.println(num[6]+" "+num[7]+" "+num[8]);
    }
	
    public static void PVE(char[] board) {
        while(true)
        {
            computer(board);
    	    int   evalValue =   gameState (board);
        	if(evalValue== WIN   || evalValue== LOSE   || evalValue== DRAW) {
                System.out.println("----------------------------------------------------------------------");
                System.out.println("结果是：");
                if (evalValue== WIN) System.out.println("AI获胜");
                else if (evalValue== LOSE) System.out.println("201621123086获胜");
                else System.out.println("棋逢对手！201621123086与AI双方平局！");
                System.out.println("----------------------------------------------------------------------");
                break;
        	}
            person(board);
    	    evalValue =   gameState (board);
        	if(evalValue== WIN   || evalValue== LOSE   || evalValue== DRAW) {
                System.out.println("----------------------------------------------------------------------");
                System.out.println("结果是：");
                if (evalValue== WIN) System.out.println("AI获胜");
                else if (evalValue== LOSE) System.out.println("201621123086获胜");
                else System.out.println("棋逢对手！201621123086与AI双方平局！");
                System.out.println("----------------------------------------------------------------------");
                break;
        	}
            
        }
    }
    
    public static int PVP(char[] board) {
        while(true)
        {
            computer(board);
    	    int   evalValue =   gameState (board);
        	if(evalValue== WIN   || evalValue== LOSE   || evalValue== DRAW) {
                System.out.println("----------------------------------------------------------------------");
                System.out.println("结果是：");
                if (evalValue== WIN) { System.out.println("AI-x获胜");return 1;}
                else if (evalValue== LOSE) {System.out.println("AI-o获胜");return -1;}
                else {System.out.println("棋逢对手！AI-x与AI-o双方平局！");return 0;}
        	}
        	computerByO(board);
    	    evalValue =   gameState (board);
        	if(evalValue== WIN   || evalValue== LOSE   || evalValue== DRAW) {
                System.out.println("----------------------------------------------------------------------");
                System.out.println("结果是：");
                if (evalValue== WIN) { System.out.println("AI-x获胜");return 1;}
                else if (evalValue== LOSE) {System.out.println("AI-o获胜");return -1;}
                else {System.out.println("棋逢对手！AI-x与AI-o双方平局！");return 0;}
        	}
            
        }
    }
    
	public static void main(String [] args)
    {
		char board[] = {'*','*','*','*','*','*','*','*','*'};
		PVE(board);
		
//    	int x = 0 ;
//    	int o = 0;
//    	int draw = 0;
//    	for(int i = 0 ; i < 50 ; i++ ) {
//        	char board[] = {'*','*','*','*','*','*','*','*','*'};
//        	int j = PVP(board);
//        	if(j == 1) x++;
//        	else if(j == -1) o++;
//        	else if(j == 0) draw++;
//    	}
//    	System.out.println("AI-x获胜:"+x+"，AI-O获胜:"+o+",平:"+draw);
    }
	
	/**
	 * 估值函数，提供一个启发式的值，决定了游戏AI的高低
	 */
	public static   int   gameState ( char []   board ) {
	       int   result =   INPROGRESS ;
	       boolean   isFull =   true ;
	       int   sum = 0;
	       int   index = 0;
	       // is game over?
	       for ( int   pos=0; pos<9; pos++){
	             char   chess = board[pos];
	             if ( empty ==chess){
	                  isFull =   false ;
	            } else {
	                  sum += chess;
	                  index = pos;
	            }
	      }
	      
	       // 如果是初始状态，则使用开局库
	       boolean   isInitial = (sum== x ||sum== o );
	       if (isInitial){
	             return   (sum== x ?1:-1)*INITIAL_POS_VALUE[index];
	      }
	      
	       // is Max win/lose?
	       for ( int [] status :   WIN_STATUS ){
	             char   chess = board[status[0]];
	             if (chess== empty ){
	                   break ;
	            }
	             int   i = 1;
	             for (; i<status.length; i++){
	                   if (board[status[i]]!=chess){
	                         break ;
	                  }
	            }
	             if (i==status.length){
	                  result = chess== x   ?   WIN   :   LOSE ;
	                   break ;
	            }
	      }
	      
	       if (result!= WIN   & result!= LOSE ){
	            
	             if (isFull){
	                   // is draw
	                  result =   DRAW ;
	            } else {
	                   // check double link
	                   // finds[0]->'x', finds[1]->'o'
	                   int [] finds =   new   int [2];
	                   for ( int [] status :   WIN_STATUS ){
	                         char   chess =   empty ;
	                         boolean   hasEmpty =   false ;
	                         int   count = 0;
	                         for ( int   i=0; i<status.length; i++){
	                               if (board[status[i]]== empty ){
	                                    hasEmpty =   true ;
	                              } else {
	                                     if (chess== empty ){
	                                          chess = board[status[i]];
	                                    }
	                                     if (board[status[i]]==chess){
	                                          count++;
	                                    }
	                              }
	                        }
	                         if (hasEmpty && count>1){
	                               if (chess== x ){
	                                    finds[0]++;
	                              } else {
	                                    finds[1]++;
	                              }
	                        }
	                  }
	                  
	                   // check if two in one line
	                   if (finds[1]>0){
	                        result = - DOUBLE_LINK ;
	                  } else
	                   if (finds[0]>0){
	                        result =   DOUBLE_LINK ;
	                  }
	                  
	            }
	            
	      }
	      
	       return   result;
	      
	} 
	/**
	 * 以'x'的角度来考虑的极小极大算法
	 */
	public static   int   minimax( char [] board,   int   depth){
	       int [] bestMoves =   new   int [9];
	       int   index = 0;
	      
	       int   bestValue = - INFINITY ;
	       for ( int   pos=0; pos<9; pos++){
	            
	             if (board[pos]== empty ){
	                  board[pos] =   x ;
	                  
	                   int   value = min(board, depth, - INFINITY , + INFINITY );
	                   if (value>bestValue){
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
	 * 以'o'的角度来考虑的极小极大算法
	 */
	public static   int   minimaxByO( char [] board,   int   depth){
	       int [] bestMoves =   new   int [9];
	       int   index = 0;
	      
	       int   bestValue = + INFINITY ;
	       for ( int   pos=0; pos<9; pos++){
	            
	             if (board[pos]== empty ){
	                  board[pos] =   o ;
	                  
	                   int   value = max(board, depth, - INFINITY , + INFINITY );
	                   if (value<bestValue){
	                        bestValue = value;
	                        index = 0;
	                        bestMoves[index] = pos;
	                        System.out.println("如果我下在"+pos/3+" "+pos%3+"，将导致胜利");
	                  } else
	                   if (value==bestValue){
	                        index++;
	                        bestMoves[index] = pos;
	                        System.out.println("如果我下在"+pos/3+" "+pos%3+"，将导致失败");
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
	public static   int   max( char [] board,   int   depth,   int   alpha,   int   beta){
	      
	       int   evalValue =   gameState (board);
	      
	       boolean   isGameOver = (evalValue== WIN   || evalValue== LOSE   || evalValue== DRAW );
	       if (beta<=alpha){
	             return   evalValue;
	      }
	       if (depth==0 || isGameOver){
	             return   evalValue;
	      }
	      
	       int   bestValue = - INFINITY ;
	       for ( int   pos=0; pos<9; pos++){
	            
	             if (board[pos]== empty ){
	                   // try
	                  board[pos] =   x ;
	                  
	                   //   maximixing
	                  bestValue = Math. max (bestValue, min(board, depth-1, Math. max (bestValue, alpha), beta));
	                  
	                   // reset
	                  board[pos] =   empty ;
	            }
	            
	      }
	      
	       return   evalValue;
	      
	}
	/**
	 * 对于'o'，估值越小对其越有利
	 */
	public static   int   min( char [] board,   int   depth,   int   alpha,   int   beta){
	      
	       int   evalValue =   gameState (board);
	      
	       boolean   isGameOver = (evalValue== WIN   || evalValue== LOSE   || evalValue== DRAW );
	       if (alpha>=beta){
	             return   evalValue;
	      }
	       // try
	       if (depth==0 || isGameOver || alpha>=beta){
	             return   evalValue;
	      }
	      
	       int   bestValue = + INFINITY ;
	       for ( int   pos=0; pos<9; pos++){
	            
	             if (board[pos]== empty ){
	                   // try
	                  board[pos] =   o ;
	                  
	                   //   minimixing
	                  bestValue = Math.min(bestValue, max(board, depth-1, alpha, Math.min(bestValue, beta)));
	                  
	                   // reset
	                  board[pos] =   empty ;
	            }
	            
	      }
	      
	       return   evalValue;
	      
	} 
	
}
