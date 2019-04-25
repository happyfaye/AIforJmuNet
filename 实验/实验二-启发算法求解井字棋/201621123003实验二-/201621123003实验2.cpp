#include <stdio.h>
#include <ctype.h>
#include <conio.h>
#include <stdlib.h>
#define MAX 1000  /*定义最大值为1000*/
#define MIN -1000  /*定义最小值为-1000*/
#define NONE 0     /* 如果搜索不到结果，结果为NONE*/
#define DRAW 1     /* 如定义平局DRAW 为1*/
#define C_WIN 2    /*电脑赢为2*/
#define M_WIN 3    /*人赢为3*/
#define QUIT 4     /*放弃为4*/
#define MAN -1     /*人用-1表示*/
#define COM 1      /*电脑用1表示*/
#define TRUE 1

/*定义b[10]用来存储棋盘（board）,step表示可以下的步数，
r表示结果，初始值为NONE；w表示可以赢的位置*/
int b[10]={0},step=9,r=NONE,w=0;

/*checkWin函数用来判断胜负，如果有胜负，返回胜方，否则返回NONE*/
int checkWin(int t[], int p){
	if(t[1]==p && t[1]==t[2] && t[2]==t[3]) return(p);
	if(t[4]==p && t[4]==t[5] && t[5]==t[6]) return(p);
	if(t[7]==p && t[7]==t[8] && t[8]==t[9]) return(p);
	if(t[1]==p && t[1]==t[4] && t[4]==t[7]) return(p);
	if(t[2]==p && t[2]==t[5] && t[5]==t[8]) return(p);
	if(t[3]==p && t[3]==t[6] && t[6]==t[9]) return(p);
	if(t[1]==p && t[1]==t[5] && t[5]==t[9]) return(p);
	if(t[3]==p && t[3]==t[5] && t[5]==t[7]) return(p);
	return(NONE);
} 
 
 /*search函数，搜索计算机和人可以羸的机会，用来计算评价值，*/
 int search(int t[]){
 	
 	int f=0,k=0;
 	k=checkWin(t,MAN);
	if(k==MAN)/*先判断人是否可以赢*/
		return MIN;/*如果可以返回一个最小值*/
	if(t[1]>=0 && t[2]>=0 && t[3]>=0) f++;
	if(t[4]>=0 && t[5]>=0 && t[6]>=0) f++;
	if(t[7]>=0 && t[8]>=0 && t[9]>=0) f++;
	if(t[1]>=0 && t[4]>=0 && t[7]>=0) f++;
	if(t[2]>=0 && t[5]>=0 && t[8]>=0) f++;
	if(t[3]>=0 && t[6]>=0 && t[9]>=0) f++;
	if(t[1]>=0 && t[5]>=0 && t[9]>=0) f++;
	if(t[3]>=0 && t[5]>=0 && t[7]>=0) f++;

	if(t[1]<=0 && t[2]<=0 && t[3]<=0) f--;
	if(t[4]<=0 && t[5]<=0 && t[6]<=0) f--;
	if(t[7]<=0 && t[8]<=0 && t[9]<=0) f--;
	if(t[1]<=0 && t[4]<=0 && t[7]<=0) f--;
	if(t[2]<=0 && t[5]<=0 && t[8]<=0) f--;
	if(t[3]<=0 && t[6]<=0 && t[9]<=0) f--;
	if(t[1]<=0 && t[5]<=0 && t[9]<=0) f--;
	if(t[3]<=0 && t[5]<=0 && t[7]<=0) f--;
		return f;/*计算评价值，并返回评价值*/	
 }
 
 
 int checkWinning(int p,int t[]){
	int i,k=10;
	for(i=1;i<10;i++){
		if(t[i]==0){
			t[i]=p;
			if(checkWin(t,p)==p){
				t[i]=0;
				k=i;
				w++;
			}
			t[i]=0;
		}
	}	
 	return k;
 } 
 
 
 /*display函数用来显示棋盘，并显示结果*/
 void display(int type){
//	printf("姓名：\n");
	printf("学号：201621123003\n");

	char dis[10]={""};
	int i;
	for(i=1;i<10;i++){
		if(b[i]<0)
	 		dis[i]='X';
		if(b[i]>0)
			 dis[i]='O'; 		
	}
 	printf("\n%c|%c|%c\n",dis[1],dis[2],dis[3]);
 	printf("-----\n");
 	printf("%c|%c|%c\n",dis[4],dis[5],dis[6]);
 	printf("-----\n");
 	printf("%c|%c|%c\n",dis[7],dis[8],dis[9]);
 
	if(type==NONE) printf("请继续");
	
	if(type==DRAW) printf("平局");
 
 	if(type==C_WIN) printf("您输了");
 
 	if(type==M_WIN) printf("恭喜您赢了");
 
 	if(type==QUIT) printf("您停止了游戏");
 }
 
/*人下的时候执行man函数*/
int man(){
	int c;
	/*提示信息*/
	printf("\n请输入您想下的位置，输入0结束（输入1-9分别代表9宫格所在的位置）\n");
	for(c=getche();;printf("\n",c=getche())) 
	if(isdigit(c) && b[c-48]==0){
		
		/*如果用户输入的是"0"，就结束程序*/
		if(c=='0'){
		r=QUIT;return 0;	
		} 
	
	/*下再用户输入的位置，步数减1*/
	step--;
	b[c-48]=MAN;
	 
	/*如果步数为0，结果为平局*/
	if(step==0) 
		r=DRAW;
	
	/*人赢了，结果为M_WIN*/
	if(checkWin(b,MAN)==MAN)
		r=M_WIN;
	
	return 0;
	}	
} 
 
 
int com(){
	int i,j,t[10];
	int temp,max=MIN-1,f=0,best=1,k,flag;
	system("cls");
	
	/*如果电脑可以赢下在该位置*/
	flag=checkWinning(COM,b);
	if(flag<10){
		b[flag]=COM;
		r=C_WIN;
		step--;
		return 0;
	} 
	
	/*如果人可以赢，也下在相应的位置*/
	flag=checkWinning(MAN,b);
	if(flag<10){
		b[flag]=COM;
		step--;
		return 0;	
	} 

    /*用t暂时存储棋盘*/
    for(i=1;i<10;i++){
    	t[i]=b[i];
	} 
    for(i=1;i<10;i++){
		if(t[i]==0){
			t[i]=COM;
			f=MAX;
			k=checkWinning(COM,t);/*如果搜索到下了第i格后人可以赢*/
								  /*就对算法进行剪支，只返回k位置的评价值*/
		    for(j=1;j<10;j++){
		    	if(k<10){
		    		t[k]=MAN;
		    	    f=search(t);
		    	    t[k]=0;
		    	    break;
				}
			
			/*否则算出每个生成的结点的评价值*/
			if(t[j]==0){
				t[j]=MAN;
				temp=search(t); 
				if(temp<f){    /*每次都返回最小评价值给最大层 */
					f=temp;
				}
				t[j]=0;
				if(f==MIN)
				    break;
			} 
			}
			t[i]=0;
			if(f>max){/* 在最大层中选择最大的评价值*/ 
				best=i;
				max=f; 
			}
		} 
	} 
	b[best]=COM;/*并下在最大层中评价值最大的位置*/
	step--;
	if(step==0) 
		r=DRAW;
}
 
 
main(){
char c;
int i;
system("cls");
printf("玩家201621123003你好\n"); 
for(i=0;i<20;i++)
printf("*");
//printf("\n 是否想先下（自己先下输入1）\n");
for(c=getche();c!='1' && c!='2';c=getche());
if(c=='1'){
	man();
	if(step<=0||r!=NONE){
		system("cls");
		display(r);
		getch();
		return 0;
	}
}
/*人与电脑轮流下*/
while(TRUE){
	com();
	display(r);
	if(step<=0||r!=NONE)
			break;
	man();
	if(step<=0|| r!=NONE)
	{
		system("cls");
		display(r);
		break;
	 } 
}
getch();
}	