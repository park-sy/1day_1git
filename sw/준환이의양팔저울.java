//230103 준환이의 양팔저울
import java.util.*;
import java.io.*;
public class Solution {
    static int ans;
    static public void main(String[] argv) throws Exception{
        Scanner sc = new Scanner(System.in);
        int[] g;
        boolean[] visit;
        int n;
        int T = sc.nextInt();
        for (int t = 1; t < T+1; t++) {

            n = sc.nextInt();
            visit = new boolean[n];
            g = new int[n];
            Arrays.fill(visit, false);

            for (int i = 0; i < n; i++) {
                g[i] = sc.nextInt();
            }
            ans = 0;
            cal(g,visit,n,0,0,0);

            System.out.println("#"+t + " "+ans);
        }
    }

    static public void cal(int[] g, boolean[] visit, int n, int cnt, int left, int right){
        if(cnt == n) {
            ans += 1;
            return;
        }

        for (int i = 0; i < n; i++) {
            if(!visit[i]){
                if(left >= right + g[i]){
                    visit[i] = true;
                    cal(g,visit,n,cnt+1, left, right+g[i]);
                    visit[i] = false;
                }
                if(left + g[i] >= right){
                    visit[i] = true;
                    cal(g,visit,n,cnt+1, left+g[i], right);
                    visit[i] = false;
                }

            }
        }
    }
}
