import java.util.*;

class Solution {
    static List<String> dictionary = new ArrayList<>();
    static String[] vowel = {"A", "E", "I", "O", "U"};
    
    static void dfs(String word, int depth) {
        if (depth>5) return;
        if (!word.equals("")) dictionary.add(word);
        
        for (int i=0; i<5; i++) {
            dfs(word+vowel[i], depth+1);
        }
    }
    
    public int solution(String word) {
        int answer = 0;
        dfs("", 0);
        // System.out.println(dictionary);
        Collections.sort(dictionary);
        
        for (int i=0; i<dictionary.size(); i++) {
            if (dictionary.get(i).equals(word)) return i+1;
        }
        
        return -1;
    }
}