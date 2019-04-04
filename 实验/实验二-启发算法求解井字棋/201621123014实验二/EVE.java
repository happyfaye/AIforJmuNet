package EVE;

import java.util.Scanner;


public class Main
{
	public static void main(String [] args)
    {
    	System.out.println("输入0开始电脑1VS电脑2");
        
        
        Scanner sc = new Scanner(System.in);
        int flag = sc.nextInt();
        while(true)
        {
            XO game = new XO(flag);
            game.play();
            break;
        }
    }
}
class XO
{
    int[][] num = new int[5][5];
    int[][] cal = new int[5][5];
    public int first;
    public XO(int cur)
    {
        for (int i = 0; i < 5; i++)
            for (int j = 0; j < 5; j++)
                cal[i][j] = num[i][j] = 0;
        first = cur;
    }
 
    boolean win(int [][] A)   //判断胜利条件：横三竖三斜三
    {
        for (int i = 0; i < 3; i++)
            if (A[i][0] == A[i][1] && A[i][1] == A[i][2] && A[i][2] != 0)
                return true;
        for (int i = 0; i < 3; i++)
            if (A[0][i] == A[1][i] && A[1][i] == A[2][i] && A[2][i] != 0)
                return true;
        if (A[0][0] == A[1][1] && A[1][1] == A[2][2] && A[2][2] != 0) return true;
        else if (A[0][2] == A[1][1] && A[1][1] == A[2][0] && A[2][0] != 0) return true;
 
        return false;
    }
 
    int dfs(boolean computer)
    {
        int state = -1,n = 0;
        for (int x = 0; x < 3; x++)
            for (int y = 0; y < 3; y++) if (cal[x][y] != 0)
                    n++;
        if (n == 9) return 0;
        for (int x = 0; x < 3; x++)
            for (int y = 0; y < 3; y++) if(cal[x][y] == 0)
            {
                if (computer) cal[x][y] = 2;
                else cal[x][y] = 1;
 
                if (win(cal))
                {
                    cal[x][y] = 0;
                    return 1;
                }
 
                int cur = dfs(!computer);
 
                if (cur == -1)
                {
                    cal[x][y] = 0;
                    return 1;
                }
                else if (cur == 0) state = 0;
 
                cal[x][y] = 0;
            }
         return state;
    }
    void computer1()
    {
        int ansx = -1,ansy = -1,state;
 
        for (int x = 0; x < 3; x++)for (int y = 0; y < 3; y++)
            {
                if (num[x][y] == 0)
                {
                    ansx = x;
                    ansy = y;
                    num[x][y] = 1;
                    if (win(num))
                    {
                        System.out.println("电脑1下子为 (" + x + "," + y + ")");
                        System.out.println(num[0][0]+" "+num[0][1]+" "+num[0][2]);
                        System.out.println(num[1][0]+" "+num[1][1]+" "+num[1][2]);
                        System.out.println(num[2][0]+" "+num[2][1]+" "+num[2][2]);
                        return;
                    }
                    num[x][y] = 0;
                }
                cal[x][y] = num[x][y];
            }
 
        for (int x = 0; x < 3; x++)for (int y = 0; y < 3; y++)
            {
                if (num[x][y] == 0)
                {
                    num[x][y] = 2;
                    if(win(num))
                    {
                        num[x][y] = 1;
                        System.out.println("电脑1下子为 (" + x + "," + y + ")");
                        System.out.println(num[0][0]+" "+num[0][1]+" "+num[0][2]);
                        System.out.println(num[1][0]+" "+num[1][1]+" "+num[1][2]);
                        System.out.println(num[2][0]+" "+num[2][1]+" "+num[2][2]);
                        return;
                    }
                    num[x][y] = 0;
                }
            }
 
        for (int x = 0; x < 3; x++)
            for (int y = 0; y < 3; y++) if (cal[x][y] == 0)
            {
                cal[x][y] = 1;
                // 2 is computer
                // 1 is people
                if(win(cal))
                {
                    num[x][y] = 2;
                    System.out.println("电脑1下子为 (" + x + "," + y + ")");
                    System.out.println(num[0][0]+" "+num[0][1]+" "+num[0][2]);
                    System.out.println(num[1][0]+" "+num[1][1]+" "+num[1][2]);
                    System.out.println(num[2][0]+" "+num[2][1]+" "+num[2][2]);
                    return;
                }
                state = dfs(false);
               
                //false is people;
                //true is computer
                if(state == 0)
                {
                    ansx = x;
                    ansy = y;
                }
                else if (state == -1)
                {
                    num[x][y] = 1;
                    System.out.println("电脑1下子为 (" + x + "," + y + ")");
                    System.out.println(num[0][0]+" "+num[0][1]+" "+num[0][2]);
                    System.out.println(num[1][0]+" "+num[1][1]+" "+num[1][2]);
                    System.out.println(num[2][0]+" "+num[2][1]+" "+num[2][2]);
                    return;
                }
                cal[x][y] = 0;
            }
        num[ansx][ansy] = 1;
        System.out.println("电脑1下子为(" + ansx + "," + ansy + ")");
        System.out.println(num[0][0]+" "+num[0][1]+" "+num[0][2]);
        System.out.println(num[1][0]+" "+num[1][1]+" "+num[1][2]);
        System.out.println(num[2][0]+" "+num[2][1]+" "+num[2][2]);
    }
 
    void computer()
    {
        int ansx = -1,ansy = -1,state;
 
        for (int x = 0; x < 3; x++)for (int y = 0; y < 3; y++)
            {
                if (num[x][y] == 0)
                {
                    ansx = x;
                    ansy = y;
                    num[x][y] = 2;
                    if (win(num))
                    {
                        System.out.println("电脑2下子为 (" + x + "," + y + ")");
                        System.out.println(num[0][0]+" "+num[0][1]+" "+num[0][2]);
                        System.out.println(num[1][0]+" "+num[1][1]+" "+num[1][2]);
                        System.out.println(num[2][0]+" "+num[2][1]+" "+num[2][2]);
                        return;
                    }
                    num[x][y] = 0;
                }
                cal[x][y] = num[x][y];
            }
 
        for (int x = 0; x < 3; x++)for (int y = 0; y < 3; y++)
            {
                if (num[x][y] == 0)
                {
                    num[x][y] = 1;
                    if(win(num))
                    {
                        num[x][y] = 2;
                        System.out.println("电脑2下子为 (" + x + "," + y + ")");
                        System.out.println(num[0][0]+" "+num[0][1]+" "+num[0][2]);
                        System.out.println(num[1][0]+" "+num[1][1]+" "+num[1][2]);
                        System.out.println(num[2][0]+" "+num[2][1]+" "+num[2][2]);
                        return;
                    }
                    num[x][y] = 0;
                }
            }
 
        for (int x = 0; x < 3; x++)
            for (int y = 0; y < 3; y++) if (cal[x][y] == 0)
            {
                cal[x][y] = 2;
                // 2 is computer
                // 1 is people
                if(win(cal))
                {
                    num[x][y] = 1;
                    System.out.println("电脑2下子为 (" + x + "," + y + ")");
                    System.out.println(num[0][0]+" "+num[0][1]+" "+num[0][2]);
                    System.out.println(num[1][0]+" "+num[1][1]+" "+num[1][2]);
                    System.out.println(num[2][0]+" "+num[2][1]+" "+num[2][2]);
                    return;
                }
                state = dfs(false);
                //false is people;
                //true is computer
                if(state == 0)
                {
                    ansx = x;
                    ansy = y;
                }
                else if (state == -1)
                {
                    num[x][y] = 2;
                    System.out.println("电脑2下子为 (" + x + "," + y + ")");
                    System.out.println(num[0][0]+" "+num[0][1]+" "+num[0][2]);
                    System.out.println(num[1][0]+" "+num[1][1]+" "+num[1][2]);
                    System.out.println(num[2][0]+" "+num[2][1]+" "+num[2][2]);
                    return;
                }
                cal[x][y] = 0;
            }
        num[ansx][ansy] = 2;
        System.out.println("电脑2下子为(" + ansx + "," + ansy + ")");
        System.out.println(num[0][0]+" "+num[0][1]+" "+num[0][2]);
        System.out.println(num[1][0]+" "+num[1][1]+" "+num[1][2]);
        System.out.println(num[2][0]+" "+num[2][1]+" "+num[2][2]);
    }
 
 
    int solve()
    {
        int ans = 0;
        if (first == 0)
        {
            num[1][1] = 2;
            ans++;
            System.out.println("电脑2下子为(1,1)");
            System.out.println(num[0][0]+" "+num[0][1]+" "+num[0][2]);
            System.out.println(num[1][0]+" "+num[1][1]+" "+num[1][2]);
            System.out.println(num[2][0]+" "+num[2][1]+" "+num[2][2]);
        }
        while(!win(num) && ans != 9)
        {
            ans++;
            if ((ans & 1) == first)computer1();
            else computer();
        }
        if(win(num))return (ans & 1); 
        else return -1;
    }
 
    public void play()
    {
        int state = solve();
        
        System.out.println("----------------------------------------------------------------------");
        System.out.println("结果是：");
        if (state == 1) System.out.println("电脑1获胜");
        else if (state == 0) System.out.println("电脑2获胜");
        else System.out.println("电脑1与电脑2平局");
        System.out.println("----------------------------------------------------------------------");   
    }
}

