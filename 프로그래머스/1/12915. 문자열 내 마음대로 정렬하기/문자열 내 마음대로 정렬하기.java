import java.util.*;
class Solution {
    public String[] solution(String[] strings, int n) {
        List<String> answer = new ArrayList<>();
        
        Arrays.sort(strings, (s1, s2) -> {
            if (s1.charAt(n)==s2.charAt(n)) return s1.compareTo(s2);
            else {
                return s1.charAt(n)-s2.charAt(n);
            }
        });
        
        for (String st: strings) {
            answer.add(st);
        }
        return answer.toArray(new String[0]);
    }
}