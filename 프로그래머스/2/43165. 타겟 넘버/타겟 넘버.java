class Solution {
    static int answer = 0;
    static int dfs(int val, int idx, int[] numbers, int target) {
        if (idx==numbers.length-1) {
            // System.out.println(val);
            if (val==target) {
                answer++;
            }
            return val;
        }
        
        dfs(val+numbers[idx+1], idx+1, numbers, target);
        dfs(val-numbers[idx+1], idx+1, numbers, target);
        
        return val;
    }
    
    public int solution(int[] numbers, int target) {
        
        dfs(numbers[0], 0, numbers, target);
        dfs(-numbers[0], 0, numbers, target);
        
        return answer;
    }
}