class Solution {
    fun dfs(graph: ArrayList<ArrayList<Int>>, visited: BooleanArray, node: Int) {
        visited[node]=true
        
        for (nxt in graph[node]) {
            if (!visited[nxt]) {
                dfs(graph, visited, nxt)
            }
        }
    }
    
    fun solution(n: Int, computers: Array<IntArray>): Int {
        var answer = 0
        var graph = ArrayList<ArrayList<Int>>()
        
        for(i in 0 until n) {
            graph.add(ArrayList())
        }
        
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (computers[i][j]==1) {
                    graph[i].add(j)
                }
            }
        }
        
        var visited = BooleanArray(n)
        
        for (i in 0 until n) {
            if (!visited[i]) {
                dfs(graph, visited, i)
                answer++
            }
        }
        
        return answer
    }
}