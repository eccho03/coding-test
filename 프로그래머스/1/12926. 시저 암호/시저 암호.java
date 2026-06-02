import java.util.*;

class Solution {
    public String solution(String s, int n) {
        StringBuilder answer = new StringBuilder();
        
        for (int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            
            if (Character.isUpperCase(ch)) {
                int idx = ch-'A';
                idx = (idx+n)%26;
                char new_char = (char)(idx+'A');      
                answer.append(new_char);
            }
            else if (Character.isLowerCase(ch)) {
                int idx = ch-'a';
                idx = (idx+n)%26;
                char new_char = (char)(idx+'a');      
                answer.append(new_char);
            }
            else {
                answer.append(" ");
            }
        }
        
        return answer.toString();
    }
}