import java.util.*;

class Solution {
    public int solution(String s) {
        String answer = "";
        String tmp = "";
        Map<String, Integer> map = new HashMap<>();
        
        map.put("zero", 0);
        map.put("one", 1);
        map.put("two", 2);
        map.put("three", 3);
        map.put("four", 4);
        map.put("five", 5);
        map.put("six", 6);
        map.put("seven", 7);
        map.put("eight", 8);
        map.put("nine", 9);
        
        for (int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            if (Character.isDigit(ch)) {
                answer+=ch;
                tmp = "";
                continue;
            }
            
            tmp += ch;
            if (map.containsKey(tmp)) {
                answer += map.get(tmp);
                tmp = "";
            }
        }
        if (answer == "") return 0;
        return Integer.parseInt(answer);
    }
}