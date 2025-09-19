class Solution {
    public String solution(String[] seoul) {
        StringBuilder answer = new StringBuilder();
        int idx = 0;
        for (int i=0; i<seoul.length; i++) {
            if (seoul[i].equals("Kim")) idx=i;
        }
        answer.append("김서방은 ");
        answer.append(idx);
        answer.append("에 있다");
        return answer.toString();
    }
}