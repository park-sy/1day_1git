// 230101/ 최고의 집합
import java.util.*;
class Solution {
    static int max;
    public int[] solution(int n, int s) {
        int[] answer = new int[n];
        int[] temp = {-1};
        
        int div = s / n;
        if(div == 0) return temp;
        else{
            int idx = 0;
            while(n >= 1){
                div = s / n;
                answer[idx++] = div;
                n -= 1;    
                s -= div;
            }
        }
        return answer;
    }
}