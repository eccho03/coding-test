import java.util.*;
class Solution {
    public String solution(String X, String Y) {
        StringBuilder answer = new StringBuilder();
        Map<Character, Integer> x_map = new HashMap<>();
        Map<Character, Integer> y_map = new HashMap<>();
        Map<Character, Integer> common_map = new HashMap<>();
        
        for (char c: X.toCharArray()) {
            x_map.put(c, x_map.getOrDefault(c, 0)+1);
        }
        
        for (char c: Y.toCharArray()) {
            y_map.put(c, y_map.getOrDefault(c, 0)+1);
        }
        
        for (char key: x_map.keySet()) {
            if (y_map.containsKey(key)) {
                int cnt = Math.min(x_map.get(key), y_map.get(key));
                common_map.put(key, cnt);
            }
        }
        
        List<Character> keys = new ArrayList<>(common_map.keySet());
        keys.sort(Collections.reverseOrder());
        
        for (char key: keys) {
            int cnt = common_map.get(key);
            for (int i=0; i<cnt; i++) {
                answer.append(key);
            }
        }
        
        String result = answer.toString();
        
        if (result.equals("")) return "-1";
        if (result.replace("0","").equals("")) return "0";
        
        return result.toString();
    }
}