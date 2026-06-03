import java.util.*;

class Solution {  
    public int solution(String str1, String str2) {
        double answer = 0;
        Map<String, Integer> atoms_1 = new HashMap<>();
        Map<String, Integer> atoms_2 = new HashMap<>();
        
        for (int i=0; i<str1.length()-1; i++) {
            char first = str1.charAt(i);
            char second = str1.charAt(i+1);
            
            if (!Character.isAlphabetic(first) || !Character.isAlphabetic(second)) continue;
            
            String atom = String.valueOf(Character.toLowerCase(first)) + String.valueOf(Character.toLowerCase(second));
            // System.out.println(atom);
            atoms_1.put(atom, atoms_1.getOrDefault(atom, 0)+1);
        }
        
        for (int i=0; i<str2.length()-1; i++) {
            char first = str2.charAt(i);
            char second = str2.charAt(i+1);
            
            if (!Character.isAlphabetic(first) || !Character.isAlphabetic(second)) continue;
            
            String atom = String.valueOf(Character.toLowerCase(first)) + String.valueOf(Character.toLowerCase(second));
            // System.out.println(atom);
            atoms_2.put(atom, atoms_2.getOrDefault(atom, 0)+1);
        }
        
        
        //System.out.println(atoms_1);
        //System.out.println(atoms_2);
        
        Set<String> keys = new HashSet<>();
        keys.addAll(atoms_1.keySet());
        keys.addAll(atoms_2.keySet());
        
        //System.out.println(keys);
        
        int inter = 0; //교집합
        int union = 0; //합집합
        
        for (String key: keys) {
            int first = atoms_1.getOrDefault(key, 0);
            int second = atoms_2.getOrDefault(key, 0);
            
            // System.out.println(key + " " + first + " "+ second);
            union += Math.max(first, second);
            inter += Math.min(first, second);
            
        }
        
        //System.out.println(union +" "+ inter);
        
        if (union==0&&inter==0) answer = 1.0f;
        else answer = (double)inter/union;
        // System.out.println(answer);
        
        return (int)(answer*65536);
    }
}