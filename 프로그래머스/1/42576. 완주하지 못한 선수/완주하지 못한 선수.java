import java.util.Arrays;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        // for (String part: participant) {
        //     System.out.println(part);
        // }
        // System.out.println("---");
        // for (String com: completion) {
        //     System.out.println(com);
        // }
        
        for (int i=0; i<completion.length; i++) {
            // System.out.println(completion[i] +" ," + participant[i]);
            if (!completion[i].equals(participant[i])) {
                answer = participant[i];
                break;
            }
        }
        if (answer=="") answer=participant[participant.length-1];
        
        return answer;
    }
}