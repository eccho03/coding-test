import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        
        for (char ch: arr) {
            answer+=ch;
        }
        
        return new StringBuilder(answer).reverse().toString();
    }
}