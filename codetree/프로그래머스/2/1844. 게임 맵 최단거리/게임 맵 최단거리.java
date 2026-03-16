import java.util.*;

class Solution {
    static int N;
    static int M;
    
    static class Point {
        int x;
        int y;
        int way;
        
        Point(int x, int y, int way) {
            this.x=x;
            this.y=y;
            this.way=way;
        }
    }
    public int solution(int[][] maps) {
        int answer = 0;
        N = maps.length;
        M = maps[0].length;
        
        answer = bfs(maps);
        
        
        return answer;
    }
    
    static int bfs(int[][] maps) {
        int[] dx = {0,0,1,-1};
        int[] dy = {1,-1,0,0};
        
        Queue<Point> q = new LinkedList<Point>();
        boolean[][] v = new boolean[N][M];
        
        q.add(new Point(0, 0, 1));
        v[0][0]=true;
        
        while (!q.isEmpty()) {
            Point cPoint = q.poll();
            if (cPoint.x==N-1 && cPoint.y==M-1) {
                return cPoint.way;
            }
            
            for (int i=0; i<4; i++) {
                int nx = cPoint.x + dx[i];
                int ny = cPoint.y + dy[i];
                
                if (nx<0||nx>=N||ny<0||ny>=M) continue;
                if (v[nx][ny]) continue;
                if (maps[nx][ny]==0) continue;
                
                q.add(new Point(nx,ny,cPoint.way+1));
                v[nx][ny]=true;
            }
          
        }
        return -1;
    }
}