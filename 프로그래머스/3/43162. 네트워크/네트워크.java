import java.util.*;

class Solution {
    static void dfs(List<List<Integer>> graph, boolean[] visited, int node) {
        // System.out.println(node);
        visited[node] = true;
        
        for (int nxt: graph.get(node)) {
            if (!visited[nxt]) {
                dfs(graph, visited, nxt);
                visited[nxt] = true;
            }
        }
    }
    
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        List<List<Integer>> graph = new ArrayList<>();
        
        for (int i=0; i<n; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (computers[i][j]==1) {
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }
            }
        }
        
        
        boolean[] visited = new boolean[n];
        for (int i=0; i<n; i++) {
            if (!visited[i]) {
                answer++;
                dfs(graph, visited, i);
            }
        }
        
        return answer;
    }
}