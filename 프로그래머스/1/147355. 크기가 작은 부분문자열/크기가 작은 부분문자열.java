class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int N = p.length();
        for (int i=0; i<=t.length()-N; i++) {
            String tmp = t.substring(i,i+N);
            if (Long.parseLong(tmp) <= Long.parseLong(p))
                answer++;
        }
        
        return answer;
    }
}