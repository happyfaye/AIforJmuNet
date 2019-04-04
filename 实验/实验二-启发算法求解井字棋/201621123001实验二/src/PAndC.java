import java.util.Scanner;

/**
 * Created by zhangyilin on 2019/3/20.
 */
public class PAndC {
    public static void main(String[] args) {
        char[][] array=new char[3][3];
        showMap(array);
        int step=0;
        int row,column;
        String locate;
        Scanner input = new Scanner(System.in);
        while(step<5||isWin(array)==false&&step<9)
        {
            if(step%2==0)  //用奇偶来区别XO输入
            {
                row=(int)(Math.random()*3);
//                System.out.print("Enter a column(0, 1, or 2) for player X:");
                column=(int)(Math.random()*3);
                if(array[row][column]=='\0')
                {
                    array[row][column]='X';
                    System.out.println("AI进入垃圾时间...");
                    showMap(array);
                }
                else {
                    step--;
                }
            }
            else
            {
                System.out.print("请输入落子坐标(以逗号分开，介于[0~2],[0~2]之间):");
                locate = input.next();
                String[] ss = locate.split(",");
                row = Integer.parseInt(ss[0]);
                column = Integer.parseInt(ss[1]);
//                System.out.println("AI进入垃圾时间...");
                if(array[row][column]=='\0')
                {
                    array[row][column]='O';
                }
                else{
                    System.out.println("输入的坐标已有棋子，请重新输入");
                    step--;
                }

                showMap(array);
            }
            step++;
        }
        if(step==9&&isWin(array)==false)  //平局
            System.out.println("棋逢对手！201621123001与AI双方平局");

    }
    public static void showMap(char[][] map) {
//        System.out.println("请输入落子坐标(以逗号分开，介于[0~2],[0~2]之间):");
        System.out.println("-----------------");

        for (int i = 0; i < 4; i++) {

            if (i==0){
                System.out.print("| ");
                System.out.print("*");
            }
            else {
                System.out.print(i-1);
            }
            System.out.print(" | ");
        }
        System.out.println();
        System.out.println("-----------------");
        for (int i = 0; i < 3; i++) {
            System.out.print("| ");
            System.out.print(i);
            System.out.print(" |");
            for (int j = 0; j < 3; j++) {
                if (map[i][j] != '\u0000')
                    System.out.print(" " + map[i][j] + " |");
                else
                    System.out.print("   |");
            }
            System.out.println();
            System.out.println("-----------------");

        }
    }


    public static boolean isWin(char[][] chess)
    {
        for(int i=0;i<3;i++)//横着判断
        {
            boolean row=true;
            if(chess[i][0]=='\u0000')
                continue;
            for(int j=1;j<3;j++)
            {
                if(chess[i][j]!=chess[i][0]||chess[i][j]=='\u0000')
                {
                    row=false;
                    break;
                }
            }
            if(row)
            {
                if (chess[i][0]=='X')
                    System.out.println("机器赢了！你输了 ");
                else if (chess[i][0]=='O')
                    System.out.println("恭喜你201621123001赢了！ ");
                else
                    System.out.println("相逢对手！201621123001与AI双方平局！");
                return true;
            }
        }

        for(int i=0;i<3;i++)//竖着判断
        {
            boolean column=true;
            if(chess[0][i]=='\u0000')
                continue;
            for(int j=1;j<3;j++)
            {
                if(chess[j][i]!=chess[0][i]||chess[j][i]=='\u0000')
                {
                    column=false;
                    break;
                }
            }
            if(column)
            {
                if (chess[0][i]=='X')
                    System.out.println("机器赢了！你输了 ");
                else if (chess[0][i]=='O')
                    System.out.println("恭喜你201621123001赢了！ ");
                else
                    System.out.println("相逢对手！201621123001与AI双方平局！");
//                System.out.println(chess[0][i]+" player won");
                return true;
            }
        }

        boolean mainDiagonal=true;
        boolean deputyDiagonal=true;
        for(int i=0;i<3;i++)//对角线判断
        {
            for(int j=0;j<3;j++)
            {
                if(mainDiagonal&&i==j)
                {
                    if(chess[i][j]=='\u0000'||chess[i][j]!=chess[0][0])
                        mainDiagonal=false;
                }
                if(deputyDiagonal&&i==2-j)
                {
                    if(chess[i][j]=='\u0000'||chess[i][j]!=chess[0][2])
                        deputyDiagonal=false;
                }
            }
        }
        if(mainDiagonal)
        {
            if (chess[0][0]=='X')
                System.out.println("机器赢了！你输了 ");
            else if (chess[0][0]=='O')
                System.out.println("恭喜你201621123001赢了！ ");
            else
                System.out.println("相逢对手！201621123001与AI双方平局！");
//            System.out.println(chess[0][0]+" player won");
            return true;
        }
        if(deputyDiagonal)
        {
            if (chess[0][2]=='X')
                System.out.println("机器赢了！你输了 ");
            else if (chess[0][2]=='O')
                System.out.println("恭喜你201621123001赢了！ ");
            else
                System.out.println("相逢对手！201621123001与AI双方平局！");
//            System.out.println(chess[0][2]+" player won");
            return true;
        }
        return false;
    }

}
