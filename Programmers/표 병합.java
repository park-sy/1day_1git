// 220218 / 표병합
import java.util.*;
class Solution {
    static int[] parent;

    public String[] solution(String[] commands) {
        
        List<String> answer = new ArrayList<>();
        parent = new int[2551];
        String[] word = new String[2551];
        for(int i = 0; i < 2551; i++) {
            parent[i] = i;
        }
        
        for(String command : commands){
            String[] cmd = command.split(" ");
            if(cmd[0].equals("UPDATE"))
            {
                if(cmd.length == 4)
                {
                    int r = Integer.parseInt(cmd[1]);
                    int c = Integer.parseInt(cmd[2]);
                    int root = find(r*50+c);
                    word[root] = cmd[3]; 
                }
                else
                {
                    for(int i = 0; i < 2551; i++){
                        if(word[i] == null) continue;
                        if(find(i) != i) continue;
                        if(word[i].equals(cmd[1])) word[i] = cmd[2];
                    }
                }
                
            }
            else if(cmd[0].equals("MERGE"))
            {
                int r1 = Integer.parseInt(cmd[1]);
                int c1 = Integer.parseInt(cmd[2]);
                int r2 = Integer.parseInt(cmd[3]);
                int c2 = Integer.parseInt(cmd[4]);
                if(r1 == r2 && c1 == c2) continue;
                int p = find(r1*50+c1);
                if(word[p] != null) union(r1*50+c1, r2*50+c2);
                else union(r2*50+c2,r1*50+c1);
                
            }
            else if(cmd[0].equals("UNMERGE"))
            {
                int r = Integer.parseInt(cmd[1]);
                int c = Integer.parseInt(cmd[2]);
                int root = find(50*r + c);
                String temp = word[root];
                for(int i = 0; i < 2551; i++){
                    if(find(i) == root) {
                        word[i] = null;
                        parent[i] = i;
                    }
                }
                word[r*50+c] = temp;
            }
            else
            {   
                int r = Integer.parseInt(cmd[1]);
                int c = Integer.parseInt(cmd[2]);
                int root = find(50*r + c);
                if(word[root] == null) answer.add("EMPTY");
                else answer.add(word[root]);
            }
        }
        
        return answer.toArray(new String[answer.size()]);
    }
    
    public static int find(int x){
        if(x != parent[x]) parent[x] = find(parent[x]);
        return parent[x];
    }
    
    
    public static void union(int p, int c){
        p = find(p);
        c = find(c);
        parent[c] = p;
    }
}