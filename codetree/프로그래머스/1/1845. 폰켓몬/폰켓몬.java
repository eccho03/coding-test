import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        HashSet<Integer> hashNums = new HashSet<Integer>();
        for (int n: nums) {
            hashNums.add(n);
        }
        
        // for (int num: hashNums) {
        //     System.out.println(num);
        // }
        
        answer = Math.min(nums.length/2, hashNums.size());
        return answer;
    }
}