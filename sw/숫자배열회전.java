//230103 숫자배열회전
import java.util.*;
public class Solution {
    static int[][] g;
    static int n;
    static String[][] ans;
    static public void main(String[] argv) throws Exception{
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int t = 1; t < T+1; t++) {
            System.out.println("#"+t);
            n = sc.nextInt();
            g = new int[n][n];
            ans = new String[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    g[i][j] = sc.nextInt();
                }
            }
            calculation();

        }
    }

    static public void calculation(){
        StringBuffer[] temp;
        for (int i = 0; i < n; i++) {
            temp = new StringBuffer[3];
            for (int j = 0; j < 3; j++) {
                temp[j] = new StringBuffer();
            }
            for (int j = 0; j < n; j++) {
                temp[0].append(g[n-j-1][i]);
                temp[1].append(g[n-i-1][n-j-1]);
                temp[2].append(g[j][n-i-1]);
            }
            System.out.print(temp[0]+" ");
            System.out.print(temp[1]+" ");
            System.out.println(temp[2]);
        }
    }
}
