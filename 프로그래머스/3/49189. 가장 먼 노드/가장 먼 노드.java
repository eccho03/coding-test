import java.util.*;

class Solution {
    
    static int[] bfs(List<List<Integer>> graph, int n) {
        Queue<Integer> q = new LinkedList<>();
        int[] dist = new int[n+1];
        
        for (int i=0; i<=n; i++) {
            dist[i]=0; // 초기화
        }
        
        q.add(1);
        dist[1] = 1;
        
        while (!q.isEmpty()) {
            int cur = q.poll();
            
            for (int nxt: graph.get(cur)) {
                if (dist[nxt]==0) {
                    q.add(nxt);
                    dist[nxt] = dist[cur]+1;
                }
            }
            
        }
        
        return dist;
    }
    
    
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        List<List<Integer>> graph = new ArrayList<>();
        
        for (int i=0; i<=n; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int i=0; i<edge.length; i++) {
            int start = edge[i][0];
            int end = edge[i][1];
            graph.get(start).add(end);
            graph.get(end).add(start);
        }
        int[] dist = bfs(graph, n);
        int mx_dist = 0;
        for (int i=1; i<=n; i++) {
            mx_dist = Math.max(mx_dist, dist[i]);
        }
        
        for (int i=1; i<=n; i++) {
            answer = (dist[i]==mx_dist) ? answer+1:answer;
        } 
        
        return answer;
    }
}