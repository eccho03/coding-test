class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "";
        
        int length_1 = cards1.length;
        int length_2 = cards2.length;
        int idx_1 = 0;
        int idx_2 = 0;
        
        for (int i=0; i<goal.length; i++) {
            if (idx_1<length_1 && goal[i].equals(cards1[idx_1])) {
                idx_1++;
            }
            else if (idx_2<length_2 && goal[i].equals(cards2[idx_2])) {
                idx_2++;
            }
            else {
                return "No";
            }
        }
        
        
        return "Yes";
    }
}