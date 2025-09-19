class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        int idx=0;
        for (int i=0; i<s.length(); i++) {
            Character ch = s.charAt(i);
            if (ch==' ') {
                answer.append(' ');
                idx=0;
            }
            else {
                if (idx%2==0) {
                    answer.append(Character.toUpperCase(ch));
                }
                else {
                    answer.append(Character.toLowerCase(ch));
                }
                idx++;
            }
        }
        
        
        return answer.toString();
    }
}