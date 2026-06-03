import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        Map<String, Integer> clothes_lst = new HashMap<>();
        for (String[] cloth: clothes) {
            clothes_lst.put(cloth[1], clothes_lst.getOrDefault(cloth[1], 0)+1);
        }
        
        System.out.println(clothes_lst);
        
        for (String key: clothes_lst.keySet()) {
            int cnt = clothes_lst.getOrDefault(key, 0);
            answer*=cnt+1;
        }
        
        return answer-1;
    }
}