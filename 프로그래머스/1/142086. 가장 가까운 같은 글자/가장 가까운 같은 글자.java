import java.util.*;

class Solution {
    public int[] solution(String s) {
        List<Integer> answer = new ArrayList<>();
        int[] pos = new int[26];
        
        for (int i=0; i<26; i++) {
            pos[i]=-1;
        }
        
        for (int i=0; i<s.length(); i++) {
            int idx = s.charAt(i) - 'a';
            if (pos[idx]==-1) answer.add(pos[idx]);
            else answer.add(i-pos[idx]);
            pos[idx]=i;
        }
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}