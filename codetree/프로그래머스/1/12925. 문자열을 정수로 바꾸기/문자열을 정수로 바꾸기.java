class Solution {
    public int solution(String s) {
        String answer = "";
        
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(0)=='0')   continue;
            answer += s.charAt(i);
        }
        int num = Integer.parseInt(answer);
        return num;
    }
}