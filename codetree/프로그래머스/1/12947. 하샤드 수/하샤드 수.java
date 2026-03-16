class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        int sum = 0;
        for (char c: String.valueOf(x).toCharArray()) {
            sum += c-'0';
        }
        answer = (x%sum ==0)?true:false;
        
        return answer;
    }
}