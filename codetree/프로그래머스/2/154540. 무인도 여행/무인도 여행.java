import java.util.*;

class Solution {
    
    static class Point {
        int x;
        int y;
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    static int bfs(String[] maps, boolean[][] visited, Point start) {
        int[] dx = {-1,1,0,0};
        int[] dy = {0,0,-1,1};
        int cnt = maps[start.x].charAt(start.y) -'0';
        int N = maps.length;
        int M = maps[0].length();
        
        Queue<Point> q = new LinkedList<>();
        q.add(start);
        visited[start.x][start.y]=true;
        
        while (!q.isEmpty()) {
            Point cur = q.poll();
            
            for (int i=0; i<4; i++) {
                int ni = cur.x + dx[i];
                int nj = cur.y + dy[i];
                
                if (ni<0 || ni>=N || nj<0 || nj>=M) continue;
                if (visited[ni][nj]) continue;
                if (maps[ni].charAt(nj)=='X') continue;
                
                q.add(new Point(ni, nj));
                visited[ni][nj]=true;
                
                //System.out.println(maps[ni].charAt(nj));
                cnt+=maps[ni].charAt(nj) -'0';
            } 
        }
        return cnt;
    }
    
    public int[] solution(String[] maps) {
        List<Integer> answer = new ArrayList<>();
        int N = maps.length;
        int M = maps[0].length();
        
        boolean[][] visited = new boolean[N][M];
        
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (!visited[i][j] && maps[i].charAt(j)!='X') {
                    int tmp = bfs(maps, visited, new Point(i, j));
                    visited[i][j]=true;
                    if (tmp!=0) answer.add(tmp);
                }
            }
        }
        if (answer.isEmpty()) return new int[] {-1};
        Collections.sort(answer);
        return answer.stream().mapToInt(i->i).toArray();
    }
}