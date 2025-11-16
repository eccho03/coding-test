import java.util.*;
class Solution {
    static int N;
    static int M;
    
    static class Point {
        int x;
        int y;
        
        Point(int x, int y) {
            this.x=x;
            this.y=y;
        }
    }
    
    public int[] solution(String[] maps) {
        List<Integer> answer = new ArrayList<>();
        
        N = maps.length;
        M = maps[0].length();
        boolean[][] visited = new boolean[N][M];
        int[][] board = new int[N][M];
        
        for (int i=0; i<N; i++) {
            String tmp = maps[i];
            for (int j=0; j<M; j++) {
                if (tmp.charAt(j)=='X') board[i][j]=0;
                else board[i][j] = Integer.parseInt(String.valueOf(tmp.charAt(j)));
            }
        }
        
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (!visited[i][j] && board[i][j]!=0) {
                    int tmp = bfs(visited, board, new Point(i, j));
                    answer.add(tmp);
                }
            }
        }
        
        if (answer.size()>0) Collections.sort(answer);
        else answer.add(-1);
        
        return answer.stream().mapToInt(i->i).toArray();
    
    }
    
    static int bfs(boolean[][] visited, int[][] board, Point start) {
        int[] dx = {0,0,-1,1};
        int[] dy = {-1,1,0,0};
        int stayDays = 0;
        
        Queue<Point> q = new LinkedList<Point>();
        q.add(start);
        visited[start.x][start.y]=true;
        stayDays += board[start.x][start.y];
        
        while (!q.isEmpty()) {
            Point cur = q.poll();
            
            for (int i=0; i<4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                
                if (nx<0||nx>=N||ny<0||ny>=M) continue;
                if (visited[nx][ny]) continue;
                if (board[nx][ny]==0) continue;
                
                q.add(new Point(nx, ny));
                visited[nx][ny]=true;
                stayDays += board[nx][ny];
            }
        }
        
        return stayDays;
    }
}