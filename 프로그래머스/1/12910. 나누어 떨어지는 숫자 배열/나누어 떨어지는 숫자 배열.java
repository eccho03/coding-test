import java.util.*;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> answer = new ArrayList<>();
        
        for (int num: arr) {
            if (num%divisor==0) answer.add(num);
        }
        
        if (answer.size()==0) answer.add(-1);
        
        Collections.sort(answer);
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}