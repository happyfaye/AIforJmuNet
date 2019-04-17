/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tictactoe;

/**
 *
 * @author 一只水饺
 */
import java.util.Random;

public class Algorithm {
	public static   final   char  empty = ' ';
	public static   final   char  x = 'X';
	public static   final   char  o = 'O';
	public static   final   int   INFINITY = 100 ;   // 表示无穷的值   
	public static   final   int   WIN = +INFINITY ;   // MAX的最大利益为正无穷   
	public static   final   int   LOSE = -INFINITY ;   // MAX的最小得益（即MIN的最大得益）为负无穷   
	public static   final   int   DOUBLE_LINK = INFINITY / 2 ;   // 如果同一行、列或对角上连续有两个，赛点   
	public static   final   int   INPROGRESS = 1 ;   // 仍可继续下（没有胜出或和局）   
	public static   final   int   DRAW = 0 ;   // 和局   
	public static   final   int [][] WIN_STATUS =   {   
	      {   0, 1, 2 },   
	      { 3, 4, 5 },   
	      { 6, 7, 8 },   
	      { 0, 3, 6 },   
	      { 1, 4, 7 },   
	      { 2, 5, 8 },   
	      { 0, 4, 8 },   
	      { 2, 4, 6 }   
	};   
	
	
	//开局时，每个位置的估值   
	static   final   int []   INITIAL_POS_VALUE   = {   
	      3, 2, 3,   
	      2, 4, 2,   
	      3, 2, 3  
	};   
	/**  
	 * 估值函数，提供一个启发式的值，决定了游戏AI的高低  
	 */  
	public   int   gameState ( char []   board ) {   
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
	                  // break ; 
                          continue;
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
	public   int   minimax( char [] board,   int   depth){   
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
	 * 以'O'的角度来考虑的极小极大算法  
	 */  
	public   int   maximin( char [] board,   int   depth){   
	       int [] bestMoves =   new   int [9];   
	       int   index = 0;   
	         
	       int   bestValue =  INFINITY ;   
	       for ( int   pos=0; pos<9; pos++){   
	               
	             if (board[pos]== empty ){   
	                  board[pos] =   o ;   
	                     
	                   int   value = max(board, depth, - INFINITY , + INFINITY );   
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
	public   int   max( char [] board,   int   depth,   int   alpha,   int   beta){   
	         
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
	public   int   min( char [] board,   int   depth,   int   alpha,   int   beta){   
	         
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
	
	/**
	 * 获取电脑方的最佳走法
	 * @param board	棋盘状态
	 * @return
	 */
	public int getNextMove1(char [] board,int depth) {
		
		return minimax(board,depth);
	}
	
	public int getNextMove2(char [] board) {
		
		return minimax(board,3);
	}
	public int getNextMove3(char [] board) {
	
	return maximin(board,2);
}
}

