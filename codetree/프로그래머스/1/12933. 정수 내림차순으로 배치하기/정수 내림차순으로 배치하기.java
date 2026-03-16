import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        String nStr = Long.toString(n);
        String[] str = nStr.split("");
        Arrays.sort(str, Collections.reverseOrder());
        
        String tmp = "";
        for (String st: str) {
            tmp+=st;
            // System.out.println(st);
        }
        
        return Long.parseLong(tmp);
    }
}