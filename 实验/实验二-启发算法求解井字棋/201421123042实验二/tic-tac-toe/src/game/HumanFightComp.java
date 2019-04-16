package game;
import java.util.*;
import chess.*;


public class HumanFightComp {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String newGame;
		int choose;
		Algorithm al = new Algorithm();
		Tic tic = new Tic();
		
		boolean flag=true;
		while(flag) {
			tic.initBroad();
			choose = tic.chooseFirstPlace();
			if(choose==2) {
				tic.comPlace();
			}
			while(true) {
				tic.humanPlace();
				if(al.gameState(tic.getChess())==al.WIN || al.gameState(tic.getChess())==al.LOSE || al.gameState(tic.getChess())==al.DRAW) {
					break;
				}
				tic.comPlace();
				//System.out.println(al.gameState(tic.getChess()));
				if(al.gameState(tic.getChess())==al.WIN || al.gameState(tic.getChess())==al.LOSE || al.gameState(tic.getChess())==al.DRAW) {
					break;
				}
			}
			if(al.gameState(tic.getChess())==al.WIN) {
				System.out.println("很遗憾，你输了，请再接再厉~");
			}else if(al.gameState(tic.getChess())==al.LOSE) {
				System.out.println("恭喜你战胜了电脑！");
			}else {
				System.out.println("恭喜你与电脑打成平手！");
			}
			System.out.println("是否开始一局新游戏（y:是，n:否）？");
			newGame = sc.next();
			if(newGame.equalsIgnoreCase("n")) {
				flag=false;
			}
		}
		

	}

}
