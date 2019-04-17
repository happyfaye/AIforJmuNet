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


import java.util.Arrays;
import java.util.Scanner;

public class Tictactoe {

	char[] chess = new char[9];
	private Algorithm al = new Algorithm();
	
	
	public char[] getChess() {
		return chess;
	}

	public void setChess(char[] chess) {
		this.chess = chess;
	}
        
        public Tictactoe(){
            initBroad();
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
	 * 人类回合
	 */
	public void humanPlace(int pos) {
		
		chess[pos] = 'O';
	}
	/**
	 * 电脑回合
	 */
	public int comPlace(int difficult) {
            int pos=al.getNextMove1(chess,difficult);
	    chess[pos] = 'X';
            return pos;
	}
	
	/**
	 * 电脑1回合
	 */
	public int com1Place() {
		int pos = al.getNextMove3(chess);
		chess[pos] = 'O';
		return pos;
	}
	
	/**
	 * 电脑2回合
	 */
	public int com2Place() {
            int pos = al.getNextMove2(chess);
		chess[pos] = 'X';
		return pos;
	}

	
}

