// 230102 타겟넘버
class Solution {
    static int answer;
    public int solution(int[] numbers, int target) {
        answer = 0;
        
        dfs(numbers, numbers.length, 0, target, 0);
        return answer;
    }
    
    public void dfs(int[] numbers, int num, int res, int target, int idx){
        if(num == idx){
            if(target == res) answer++;
            return;
        }
        dfs(numbers, num, res+numbers[idx], target, idx+1);
        dfs(numbers, num, res-numbers[idx], target, idx+1);
    }
}