import java.util.*;

class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        
        int length = p.length();
        
        // i ~ i+3
        
        for (int i=0; i<t.length(); i++) {
            String tmp = "";
            for (int j=i;j<i+length; j++) {
                if (t.length()-i<length) break;
                tmp += t.charAt(j);
            }
            if (tmp!="") {
                if (Long.parseLong(tmp) <= Long.parseLong(p)) {
                // System.out.println(Integer.parseInt(tmp));
                    answer++;
            }
            
        }
        }
        
        return answer;
    }
}