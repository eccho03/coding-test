import java.util.*;
class Solution {
    public int[] solution(int[] answers) {        
        int[] stud_1 = {1,2,3,4,5};
        int[] stud_2 = {2,1,2,3,2,4,2,5};
        int[] stud_3 = {3,3,1,1,2,2,4,4,5,5};
        int solved_1 = 0;
        int solved_2 = 0;
        int solved_3 = 0;
        
        for (int i=0; i<answers.length; i++) {
            if (answers[i]==stud_1[i%stud_1.length]) {
                solved_1++;
            }
            if (answers[i]==stud_2[i%stud_2.length]) {
                solved_2++;
            }
            if (answers[i]==stud_3[i%stud_3.length]) {
                solved_3++;
            }
        }
        
        int mxScore = Math.max(solved_1, Math.max(solved_2, solved_3));
        //System.out.println(mxScore);
        List<Integer> answer = new ArrayList<>();
        
        if (solved_1==mxScore) {
            answer.add(1);
        }
        if (solved_2==mxScore) {
            answer.add(2);
        }
        if (solved_3==mxScore) {
            answer.add(3);
        }
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}