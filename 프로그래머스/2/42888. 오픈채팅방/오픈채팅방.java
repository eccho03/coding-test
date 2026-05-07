import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        ArrayList<String> answer = new ArrayList<>();
        Map<String, String> nickname = new HashMap<>();
        
        for (String cur: record) {
            String[] token = cur.split(" ");
            
            if (token[0].equals("Enter")) {
                nickname.put(token[1], token[2]);
            }
            else if (token[0].equals("Change")) {
                nickname.put(token[1], token[2]);
            }
        }
        //System.out.println(nickname);
        
        for (int i=0; i<record.length; i++) {
            String[] token = record[i].split(" ");
            if (token[0].equals("Enter")) {
                answer.add(nickname.get(token[1]) + "님이 들어왔습니다.");
            }
            else if (token[0].equals("Leave")) {
                answer.add(nickname.get(token[1])+"님이 나갔습니다.");
            }
        }
        
        return answer.toArray(new String[0]);
    }
}