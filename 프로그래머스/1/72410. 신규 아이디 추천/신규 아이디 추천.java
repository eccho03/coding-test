import java.util.*;

class Solution {
    public String solution(String new_id) {
        StringBuilder answer = new StringBuilder();
        
        for (int i=0; i<new_id.length(); i++) {
            char ch = new_id.charAt(i);
            if (Character.isUpperCase(ch)) {
                answer.append(Character.toLowerCase(ch));
            }
            else if (Character.isLowerCase(ch)||Character.isDigit(ch)||ch=='-'||ch=='_'||ch=='.') {
                answer.append(ch);
            }                  
        }
        
        String result = answer.toString();
        
        while (result.contains("..")) {
            result = result.replace("..",".");
        }
        
        if (result.startsWith(".")) result = result.substring(1);
        if (result.endsWith(".")) result = result.substring(0, result.length()-1);
        if (result.length()==0) result += 'a';
        if (result.length()>=16) result = result.substring(0, 15);
        if (result.endsWith(".")) result = result.substring(0, result.length()-1);
        if (result.length()<=2) {
            while (true) {
                result+=result.substring(result.length()-1);
                if (result.length()==3) break;
            }
        }
        
        return result;
    }
}