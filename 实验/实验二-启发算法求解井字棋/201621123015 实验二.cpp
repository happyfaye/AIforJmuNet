#include <stdio.h>
#include <string.h>
#include <stdlib.h>
 
int main(int argc,char** argv)
{
	int player = 0;
	int winner = 0;
	int choice = 0;
	int row = 0;
	int column = 0;
	int line = 0;
 
	char board[3][3] = {
		{'1','2','3'},
		{'4','5','6'},
		{'7','8','9'}
	};
 
	int i;
	for(i = 0;i<9 && winner==0;i++){
		printf("\n\n");
		printf(" %c | %c | %c\n",board[0][0],board[0][1],board[0][2]);
		printf("---+---+---\n");
		printf(" %c | %c | %c\n",board[1][0],board[1][1],board[1][2]);
		printf("---+---+---\n");
		printf(" %c | %c | %c\n",board[2][0],board[2][1],board[2][2]);
 
		player = i%2+1;
		//Get valid player square selection
		do{
			printf("\nPlayer %d, please enter the number of the square "
				"where you want to place your %c: ",
				player,(player == 1)?'X':'O');
			scanf("%d",&choice);
 
			row = --choice/3;
			column = choice%3;
		}while(choice<0 || choice>9 || board[row][column]>'9');
		//insert player symbol
		board[row][column] = (player == 1)?'X':'O';
		//Check for a winning line--diagonals first
		if((board[0][0]==board[1][1] && board[0][0]==board[2][2]) ||
			(board[0][2]==board[1][1] && board[0][2]==board[2][0]))
			winner = player;
		else
			//Check rows and columns for a winning line
			for(line = 0;line <= 2;line++)
				if((board[line][0]==board[line][1] &&
					board[line][0]==board[line][2]) ||
					(board[0][line]==board[1][line] &&
					board[0][line]==board[2][line]))
					winner = player;
	}
	//Game is over so display the final board
	printf("\n\n");
	printf(" %c | %c | %c\n",board[0][0],board[0][1],board[0][2]);
	printf("---+---+---\n");
	printf(" %c | %c | %c\n",board[1][0],board[1][1],board[1][2]);
	printf("---+---+---\n");
	printf(" %c | %c | %c\n",board[2][0],board[2][1],board[2][2]);
	//Dispay result message
	if(winner == 0)
		printf("\n201621123015与对手打成平局\n");
	else if(winner == 1)
		printf("\n201621123015胜利\n");
	else
		printf("\n201621123015失败\n");
	return 0;
}
