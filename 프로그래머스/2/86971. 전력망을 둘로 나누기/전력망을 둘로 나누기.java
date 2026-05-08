import java.util.*;

class Solution {
    static List<List<Integer>> graph = new ArrayList<>();
    static boolean[] visited;
    static int mn_diff = Integer.MAX_VALUE;
    
    static int bfs(int num, int[][] wires) {
        Queue<Integer> q = new LinkedList<>();
        int cnt = 0;
        
        q.offer(num);
        visited[num]=true;
        cnt++;
        
        while (!q.isEmpty()) {
            int cur = q.poll();
            
            for (int nxt: graph.get(cur)) {
                if (!visited[nxt]) {
                    q.offer(nxt);
                    visited[nxt]=true;
                    cnt++;
                }
            }
        }
        
        return cnt;
    }
    
    public int solution(int n, int[][] wires) {
        int answer = -1;
        
        for (int i=0; i<=n; i++) {
            graph.add(new ArrayList());
        }
        
        for (int[] wire: wires) {
            graph.get(wire[0]).add(wire[1]);
            graph.get(wire[1]).add(wire[0]);
        }
        
        for (int i=0; i<wires.length; i++) {
            int[] wire = wires[i];
            
            graph.get(wire[0]).remove(Integer.valueOf(wire[1]));
            graph.get(wire[1]).remove(Integer.valueOf(wire[0]));
            
            visited = new boolean[n+1];
            int left = bfs(1, wires);
            int right = n-left;
            
            //System.out.println(Math.abs(left-right));
            mn_diff = Math.min(mn_diff, Math.abs(left-right));
            
            graph.get(wire[0]).add(wire[1]);
            graph.get(wire[1]).add(wire[0]);
        }
        
        return mn_diff;
    }
}