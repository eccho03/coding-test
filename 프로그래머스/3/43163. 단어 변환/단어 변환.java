import java.util.*;

class Solution {
    static class Point {
        String word;
        int cnt;
        
        Point(String word, int cnt) {
            this.word = word;
            this.cnt = cnt;
        }
    }
    
    static int bfs(String begin, String target, String[] words) {
        Queue<Point> q = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        
        q.offer(new Point(begin, 0));
        visited.add(begin);
        
        while (!q.isEmpty()) {
            Point cur = q.poll();
            if (cur.word.equals(target)) return cur.cnt;
            
            for (String nxt: words) {
                if (visited.contains(nxt)) continue;
                int num = 0;
                for (int i=0; i<cur.word.length(); i++) {
                    if (cur.word.charAt(i)!=nxt.charAt(i)) num++;
                }
                if (num!=1) continue;
                q.offer(new Point(nxt, cur.cnt+1));
                visited.add(nxt);
            }
        }
        
        
        return -1;
        
    }
    
    public int solution(String begin, String target, String[] words) {
        if (!Arrays.asList(words).contains(target)) return 0;
        
        int answer = bfs(begin, target, words);
        return answer;
    }
}