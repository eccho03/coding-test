import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Set<String> new_report = new HashSet<>();
        Map<String, Integer> get_report = new HashMap<>();
        Map<String, Integer> make_report = new HashMap<>();
        Set<String> forbidden_id = new HashSet<>();
        
        for (String cur_report: report) {
            new_report.add(cur_report);
        }
        
        for (String cur_report: new_report) {
            String[] token = cur_report.split(" ");
            get_report.put(token[1], get_report.getOrDefault(token[1], 0)+1);
        }
        
        for (String key: get_report.keySet()) {
            if (get_report.get(key)>=k) forbidden_id.add(key);
        }
        
        // System.out.println(forbidden_id);
        
        for (String cur_report: new_report) {
            String[] token = cur_report.split(" ");
            if (forbidden_id.contains(token[1])) make_report.put(token[0], make_report.getOrDefault(token[0], 0)+1);
        }
        
        // System.out.println(make_report);
        
        for (int i=0; i<id_list.length; i++) {
            String id = id_list[i];
            answer[i] = make_report.keySet().contains(id) ? make_report.get(id):0;
        }
        
        return answer;
    }
}