import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        
        boolean word_start = true;
        
        for (int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            if (word_start) {
                if (Character.isAlphabetic(ch)) 
                    answer.append(Character.toUpperCase(ch));
                else
                    answer.append(ch);
                word_start = false;
            }
            
            else {
                if (ch==' ') {  
                    if (i<s.length()-1 && s.charAt(i+1)!=' ') word_start = true;
                    answer.append(' ');
                }
                else answer.append(Character.toLowerCase(ch));
            }        
            
        }
              
        return answer.toString();
    }
}