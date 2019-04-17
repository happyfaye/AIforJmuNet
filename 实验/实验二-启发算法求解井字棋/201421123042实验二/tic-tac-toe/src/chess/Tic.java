package chess;

import java.util.Scanner;

public class Tic {
	
	Scanner sc = new Scanner(System.in);
	private char[] chess = new char[9];
	private Algorithm al = new Algorithm();
	
	
	public char[] getChess() {
		return chess;
	}

	public void setChess(char[] chess) {
		this.chess = chess;
	}

	/**
	 * 初始化棋盘
	 */
	public void initBroad() {
		for(int i=0;i<chess.length;i++) {
			chess[i] = ' ';
		}
		
		
	}
	
	/**
	 * 打印棋盘
	 */
	public void printBroad() {
		
		System.out.println("-------------------------");
		System.out.println("|       |       |       |");
		for(int i=0;i<chess.length;i++) {
			if(i%3==0&&i!=0) {
				System.out.println("|");
				System.out.println("|       |       |       |");
				System.out.println("-------------------------");
				System.out.println("|       |       |       |");
			}
			
			System.out.print("|   "+chess[i]+"   ");
			
			
		}
		System.out.println("|");
		System.out.println("|       |       |       |");
		System.out.println("-------------------------");
		
		
	}
	
	/**
	 * 判断该位置是否有棋子
	 * @param i	棋子位置
	 * @return	
	 */
	public boolean isEmpty(int i) {
		
		return chess[i] == ' ';
		
	}
	
	
	/**
	 * 获取玩家输入坐标
	 * @return
	 */
	public int getPos() {
		boolean flag = true;
		int pos = 0;
		System.out.println("轮到你的回合……");
		while(flag) {
			System.out.println("请输入你的选择，数字之间以空格分开，例如：2 2：");
			int m = sc.nextInt();
			int n = sc.nextInt();
			if(m<0||m>3||n<0||n>3) {
				System.out.println("输入有误，请重新输入！");
			}else {
				pos = (m-1)*3+n-1;
				if(isEmpty(pos)==true) {
					flag=false;
				}else {
					
					System.out.println("该格已经有棋子，请重新输入");
				}
				
			}
			
		}
		
		return pos;
		
	}
	
	/**
	 * 选择先手顺序
	 * @return
	 */
	public int chooseFirstPlace() {
		boolean flag=true;
		
		System.out.println("请选择先手顺序（1：玩家先手，2：电脑先手）：");
		int choose = sc.nextInt();
		while(flag) {
			if(choose==1||choose==2) {
				flag = false;
			}else {
				System.out.println("请输入正确数字！");
			}
		}
		
		return choose;
		
	}
	
	/**
	 * 人类回合
	 */
	public void humanPlace() {
		int pos = getPos();
		chess[pos] = 'O';
		System.out.println("落子完毕");
		printBroad();
	}
	
	

	/**
	 * 电脑回合
	 */
	public void comPlace() {
		int pos = al.getNextMove(chess);
		//pos = (m-1)*3+n-1;
		System.out.println("轮到电脑回合，电脑的选择是:"+(pos/3+1)+" "+(pos%3+1));
		chess[pos] = 'X';
		System.out.println("落子完毕");
		printBroad();
	}
	
	/**
	 * 电脑1回合
	 */
	public void com1Place() {
		int pos = al.comp1GetNextMove(chess);
		System.out.println("轮到三层深度机器玩家回合，电脑的选择是:"+(pos/3+1)+" "+(pos%3+1));
		chess[pos] = 'X';
		System.out.println("落子完毕");
		
	}
	
	/**
	 * 电脑2回合
	 */
	public void com2Place() {
		int pos = al.comp2GetNextMove(chess);
		System.out.println("轮到二层深度机器玩家回合，电脑的选择是:"+(pos/3+1)+" "+(pos%3+1));
		chess[pos] = 'O';
		System.out.println("落子完毕");
		
	}
	
	
	
	
	
	
	
	
	
}
