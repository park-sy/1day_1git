//230103 스도쿠검증
import java.util.*;
public class 스도쿠검증 {
    static int[][] g;
    static public void main(String[] argv) throws Exception{
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        g = new int[9][9];
        for (int t = 1; t < T+1; t++) {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    g[i][j] = sc.nextInt();
                }
            }
            if(check()) System.out.println("#"+t+" 1");
            else System.out.println("#"+t+" 0");


        }
    }

    static public boolean check(){
        boolean[] visitBox, visitCal, visitRow;

        for (int k = 0; k < 9; k++) {
            visitBox = new boolean[10];
            Arrays.fill(visitBox, false);
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if(visitBox[g[i+k/3*3][j+(k%3)*3]]) return false;
                    visitBox[g[i+k/3*3][j+(k%3)*3]] = true;
                }
            }
            visitCal = new boolean[10];
            Arrays.fill(visitCal, false);
            for (int i = 0; i < 9; i++) {
                if(visitCal[g[k][i]]) return false;
                visitCal[g[k][i]] = true;
            }
            visitRow = new boolean[10];
            Arrays.fill(visitRow, false);
            for (int i = 0; i < 9; i++) {
                if(visitRow[g[i][k]]) return false;
                visitRow[g[i][k]] = true;
            }
        }
        return true;
    }
}
