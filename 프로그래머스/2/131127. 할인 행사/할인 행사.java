import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        int DAYS = 10;
        
        Map<String, Integer> cur_window = new HashMap<>();
        Map<String, Integer> want_map = new HashMap<>();
        
        for (int i=0; i<want.length; i++) {
            want_map.put(want[i], number[i]);
        }
        
        //System.out.println(want_map);
        
        
        for (int i=0; i<DAYS; i++) {
            cur_window.put(
                discount[i], 
                cur_window.getOrDefault(discount[i], 0)+1
            );
        }
        
        if (cur_window.equals(want_map)) answer++;
        
        for (int i=DAYS; i<discount.length; i++) {
            cur_window.put(
                discount[i-DAYS], 
                cur_window.getOrDefault(discount[i-DAYS], 0)-1
            );
            // System.out.println(cur_window);
            
            if (cur_window.get(discount[i-DAYS])==0) cur_window.remove(discount[i-DAYS]);
                
            cur_window.put(
                discount[i], 
                cur_window.getOrDefault(discount[i], 0)+1
            );
            
            if (cur_window.equals(want_map)) answer++;
        }
        
        //System.out.println(cur_window);
        
        
        return answer;
    }
}