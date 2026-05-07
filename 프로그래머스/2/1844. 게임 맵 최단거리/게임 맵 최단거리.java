import java.util.*;

class Solution {
    static class Point {
        int x;
        int y;
        int dist;
        
        Point(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
    }
    
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    
    int bfs(int[][] maps, int N, int M) {
        Queue<Point> q = new LinkedList<>();
        boolean[][] visited = new boolean[N][M];
        
        q.offer(new Point(N-1, M-1, 1));
        visited[N-1][M-1] = true; // 항상 똑같은 위치에서 시작
        
        boolean flag = false;
        
        while (!q.isEmpty()) {
            Point cur = q.poll();
            if (cur.x==0 && cur.y==0) return cur.dist;
            
            flag = false;
            for (int i=0; i<4; i++) {
                int nx = cur.x+dx[i];
                int ny = cur.y+dy[i];
                
                if(nx<0||nx>=N||ny<0||ny>=M) continue;
                if (visited[nx][ny]) continue;
                if (maps[nx][ny]==0) continue;
                
                q.offer(new Point(nx, ny, cur.dist+1));
                visited[nx][ny] = true;
                flag = true;
            }
        } 
        
        return -1;
    }
    
    public int solution(int[][] maps) {
        int answer = 0;
        int N = maps.length;
        int M = maps[0].length;
        
        answer = bfs(maps, N, M);
        
        return answer;
    }
}