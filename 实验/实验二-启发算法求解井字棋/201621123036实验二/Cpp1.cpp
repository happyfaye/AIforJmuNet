#include "algorithm"
#include "windows.h"
#include "iostream"
#include "stdlib.h"
#include "string.h"
#include "stdio.h"
#include "vector"
#include "math.h"
#include "time.h"
#include "string"
#include "map" 
 
using namespace std;
 
//	判断所选位置是否可下 不可下返回-1 可以下返回0 
int IsNULL ( int array[3][3], int x, int y )
{
	if ( array[x][y] == 0 ) return 0;
	return -1;
}
 
//	打印棋盘 
void Print ( int array[3][3] )
{
	system( "cls" );
	int i, j;
	printf ( "\n\n\t井 字 棋\n" );
	for ( i = 0; i < 3; i ++ )
	{				  
		printf ( "\n\t+-+-+-+\n\t|" );
		for ( j = 0; j < 3; j ++ )
		{
			if ( array[i][j] == 0 ) printf( " " );
			if ( array[i][j] == 1 ) printf( "X" );
			if ( array[i][j] == -1 ) printf( "O" );
			printf( "|" );
		}
	}
	printf ( "\n\t+-+-+-+\n\n" );
}
 
//	电脑下子 
int GO ( int array[3][3] )
{
	int i, t;
	int k;
	for ( i = 0; i < 3; i ++ )
	{
		t = array[i][0] + array[i][1] + array[i][2];
		if ( t == -2 )
		{
			for ( k = 0; k < 3; k ++ )
			{
				if ( array[i][k] == 0 )
				{
					array[i][k] = -1;
					return 0;
				} 
				
			}
		} 
	}
	for ( i = 0; i < 3; i ++ )
	{
		t = array[0][i] + array[1][i] + array[2][i];
		if ( t == -2 )
		{
			for ( k = 0; k < 3; k ++ )
			{
				if ( array[k][i] == 0 )
				{
					array[k][i] = -1;
					return 0;
				}
			}
		} 
	}
	int j = 0; t = 0;
	for ( i = 0; i < 3; i ++ )
	{
		j += array[i][i];
		t += array[i][2-i];
	}
	if ( t == -2 )
	{
		for ( k = 0; k < 3; k ++ )
		{
			if ( array[k][2-k] == 0 )
			{
				array[k][2-k] = -1;
				return 0;
			} 
		}
	}
	if ( j == -2 )
	{
		for ( k = 0; k < 3; k ++ )
		{
			if ( array[k][k] == 0 ) 
			{
				array[k][k] = -1;
				return 0;
			}
		}
	}
	
	
	
	for ( i = 0; i < 3; i ++ )
	{
		t = array[i][0] + array[i][1] + array[i][2];
		if ( t == 2 )
		{
			for ( k = 0; k < 3; k ++ )
			{
				if ( array[i][k] == 0 )
				{
					array[i][k] = -1;
					return 0;
				} 
				
			}
		} 
	}
	for ( i = 0; i < 3; i ++ )
	{
		t = array[0][i] + array[1][i] + array[2][i];
		if ( t == 2 )
		{
			for ( k = 0; k < 3; k ++ )
			{
				if ( array[k][i] == 0 )
				{
					array[k][i] = -1;
					return 0;
				}
			}
		} 
	}
	j = 0; t = 0;
	for ( i = 0; i < 3; i ++ )
	{
		j += array[i][i];
		t += array[i][2-i];
	}
	if ( t == 2 )
	{
		for ( k = 0; k < 3; k ++ )
		{
			if ( array[k][2-k] == 0 )
			{
				array[k][2-k] = -1;
				return 0;
			} 
		}
	}
	if ( j == 2 )
	{
		for ( k = 0; k < 3; k ++ )
		{
			if ( array[k][k] == 0 ) 
			{
				array[k][k] = -1;
				return 0;
			}
		}
	}
	
	
	while ( 1 )
	{
		srand ( time ( 0 ) );
		i = rand ( ) % 3;
		j = rand ( ) % 3;
		if ( IsNULL ( array, i, j ) == 0 )
		{
			array[i][j] = -1;
			break;
		}
	}
	return 0;
}
 
//	平局返回0;正方胜返回1;负反胜利返回-1;否则返回6; 
int Check ( int array[3][3] )
{
	int i, t;
	for ( i = 0; i < 3; i ++ )
	{
		t = array[i][0] + array[i][1] + array[i][2];
		if ( t == -3 ) return -1;
		if ( t == 3 ) return 1;
	}
	for ( i = 0; i < 3; i ++ )
	{
		t = array[0][i] + array[1][i] + array[2][i];
		if ( t == -3 ) return -1;
		if ( t == 3 ) return 1;
	}
	int j = 0; t = 0;
	for ( i = 0; i < 3; i ++ )
	{
		j += array[i][i];
		t += array[i][2-i];
	}
	if ( t == -3 || j == -3 ) return -1;
	if ( t == 3 || j == 3 ) return 1;
	for ( i = 0; i < 3; i ++ )
	{
		for ( j = 0; j < 3; j ++ )
		{
			if ( array[i][j] == 0 ) return 6;
		}
	}
	return 0;
}
 
 
int CP ( int array[3][3] )
{
	int t = Check ( array );
	Print ( array );
	if ( t == 0 )
	{
		printf ( "\t 平局！");
		system ( "pause" );
		return 0; 
	}
	if ( t == 1 )
	{
		printf ( "\t 恭喜你 赢了！ ");
		system ( "pause" );
		return 0; 
	}
	if ( t == -1 )
	{
		printf ( "\t 很抱歉 输了！ ");
		system ( "pause" );
		return 0; 
	}
	return -1;
} 
 
int main ( )
{
	system ( "井字棋小游戏" ); 
	int array[3][3];
	memset ( array, 0, sizeof ( array ) );
	Print ( array );
	int x, y, t;
	while ( 1 )
	{
		scanf ( "%d %d", &x, &y );
		x --;
		y --;
		if ( x > 2 || y > 2 || x < 0 || y < 0 )
		{
			printf( "\t输入范围: 1-3！ " );
			continue;
		}
		if ( IsNULL ( array, x, y ) == -1 )
		{
			printf ( "所选位置已存在！ " );
			continue; 
		}
		array[x][y] = 1;
		t = CP ( array );
		if ( t == 0 ) return 0;
		GO ( array );
		t = CP ( array );
		if ( t == 0 ) return 0;
	}
	return 0;
} 