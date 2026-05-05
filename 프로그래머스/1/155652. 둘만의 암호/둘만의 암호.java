import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {
        StringBuilder answer = new StringBuilder();
        
        Set<Character> skip_set = new HashSet<>();
        
        for (char ch: skip.toCharArray()) {
            skip_set.add(ch);
        }
        
        for (char ch: s.toCharArray()) {
            int cnt = 0;
            char target = ch;
            while (cnt<index) {
                target = (char)(((target-'a')+1)%26 + 'a');
                
                if (!skip_set.contains(target)) cnt++;
            }
            answer.append(target);
        }
        
        return answer.toString();
    }
}