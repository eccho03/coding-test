import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];
        
        Arrays.sort(strings, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                if (s1.charAt(n)-s2.charAt(n)!=0) return s1.charAt(n)-s2.charAt(n);
                else return s1.compareTo(s2);
            }
        });
        
        for (int i=0; i<strings.length; i++) {
            answer[i] = strings[i];
        }
        
        return answer;
    }
}