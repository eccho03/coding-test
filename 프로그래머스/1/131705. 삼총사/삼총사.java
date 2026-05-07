import java.util.*;

class Solution {
    
    static int answer=0;
    
    static void dfs(int[] number, int[] three, int start, int depth) {
        if (depth==3) {
            if (three[0]+three[1]+three[2]==0) answer++;
            return;
        }
        
        for (int i=start; i<number.length; i++) {
            three[depth] = number[i];
            dfs(number, three, i+1, depth+1);
        }
    }
    
    public int solution(int[] number) {
        int N = number.length;
        int[] three = new int[3];
        
        dfs(number, three, 0, 0);
        
        return answer;
    }
}