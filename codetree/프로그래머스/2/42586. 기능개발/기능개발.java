import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        int cnt = 1;
        int lastDay = (int) Math.ceil((100.0-progresses[0])/speeds[0]);
        
        
        for (int i=1; i<progresses.length; i++) {
            int curDay = (int) Math.ceil((100.0-progresses[i])/speeds[i]);
            
            if (lastDay>=curDay) {
                cnt++;
                
            }
            else {
                answer.add(cnt);
                lastDay=curDay;
                cnt=1;
            }
        }
        
        answer.add(cnt);
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}