class Solution {
    public String solution(String phone_number) {
        StringBuilder answer = new StringBuilder();
        int N = phone_number.length();
        for (int i=0; i<N; i++) {
            if ((N-i)>4) {
                answer.append("*");
            }
            else {
                answer.append(phone_number.charAt(i));
            }
        }
        
        return answer.toString();
    }
}