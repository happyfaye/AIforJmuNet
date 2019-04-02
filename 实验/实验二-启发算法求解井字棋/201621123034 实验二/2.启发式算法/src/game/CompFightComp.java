package game;
import chess.*;

public class CompFightComp {

	public static void main(String[] args) {
		int c1 = 0;
		int c2 = 0;
		int pin = 0;
		Algorithm al = new Algorithm();
		Tic tic = new Tic();
		System.out.println("三层深度机器玩家先手情况：");
		for(int i=0;i<25;i++) {
			tic.initBroad();
			while(true) {
				tic.com1Place();
				if(al.gameState(tic.getChess())==al.WIN || al.gameState(tic.getChess())==al.LOSE || al.gameState(tic.getChess())==al.DRAW) {
					break;
				}
				tic.com2Place();
				if(al.gameState(tic.getChess())==al.WIN || al.gameState(tic.getChess())==al.LOSE || al.gameState(tic.getChess())==al.DRAW) {
					break;
				}
				
				
			}
			if(al.gameState(tic.getChess())==al.WIN) {
				System.out.println("获胜者是三层深度的电脑玩家");
				System.out.println("-------------------------");
				c1++;
			}else if(al.gameState(tic.getChess())==al.LOSE) {
				System.out.println("获胜者是二层深度的电脑玩家");
				System.out.println("-------------------------");
				c2++;
			}else {
				System.out.println("两位玩家打平");
				System.out.println("-------------------------");
				pin++;
			}
			
			
		}
		
		
		System.out.println("二层深度机器玩家先手情况：");
		for(int i=0;i<25;i++) {
			tic.initBroad();
			while(true) {
				tic.com2Place();
				if(al.gameState(tic.getChess())==al.WIN || al.gameState(tic.getChess())==al.LOSE || al.gameState(tic.getChess())==al.DRAW) {
					break;
				}
				tic.com1Place();
				if(al.gameState(tic.getChess())==al.WIN || al.gameState(tic.getChess())==al.LOSE || al.gameState(tic.getChess())==al.DRAW) {
					break;
				}
				
				
			}
			if(al.gameState(tic.getChess())==al.WIN) {
				System.out.println("获胜者是三层深度的电脑玩家");
				System.out.println("-------------------------");
				c1++;
			}else if(al.gameState(tic.getChess())==al.LOSE) {
				System.out.println("获胜者是二层深度的电脑玩家");
				System.out.println("-------------------------");
				c2++;
			}else {
				System.out.println("两位玩家打平");
				System.out.println("-------------------------");
				pin++;
			}
			
		}
		
		System.out.println("游戏结果：");
		System.out.println("三层深度的电脑玩家获胜次数为"+c1);
		System.out.println("二层深度的电脑玩家获胜次数为"+c2);
		System.out.println("两个机器打平的次数为"+pin);

		
		
	}

}
