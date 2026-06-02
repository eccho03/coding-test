import java.util.*;

class Solution {
    static class Point {
        int x;
        int y;
        
        Point (int x, int y) {
            this.x=x;
            this.y=y;
        }
    }
    
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    
    static int N;
    static int M;
    
    static int bfs(int si, int sj, boolean[][] visited, int[][] picture) {
        Queue<Point> q = new LinkedList<>();
        int cnt = 0;
        
        q.offer(new Point(si, sj));
        visited[si][sj]=true;
        cnt++;
        
        while (!q.isEmpty()) {
            Point cur = q.poll();
            
            for (int i=0; i<4; i++) {
                int nx = cur.x+dx[i];
                int ny = cur.y+dy[i];
                
                if (nx<0||nx>=N||ny<0||ny>=M) continue;
                if (visited[nx][ny]) continue;
                if (picture[nx][ny]!=picture[cur.x][cur.y]) continue;
                
                q.offer(new Point(nx, ny));
                visited[nx][ny]=true;
                cnt++;
            }
        }
        return cnt;
    }
    
    public int[] solution(int m, int n, int[][] picture) {
        int area=0;
        int mx_area = Integer.MIN_VALUE;
        N = m;
        M = n;
        boolean[][] visited = new boolean[N][M];
        
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (!visited[i][j] && picture[i][j]!=0) {
                    area++;
                    int cnt = bfs(i, j, visited, picture);
                    mx_area = Math.max(mx_area, cnt);
                }
            }
        }
        
        
        return new int[] {area, mx_area};
    }
}