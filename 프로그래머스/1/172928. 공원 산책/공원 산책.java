import java.util.*;

class Solution {
    static boolean possible(int ni, int nj, int N, int M, int[][] arr) {
        // 범위 체크
        if (ni<0||ni>=N||nj<0||nj>=M) {
            return false;
        }
        // 장애물 체크
        if (arr[ni][nj]==1) {
            return false;
        }
        
        return true;
    }
    public int[] solution(String[] park, String[] routes) {
        int[] answer = {};
        int N = park.length;
        int M = park[0].length();
        int[][] arr = new int[N][M];
        int si=-1;
        int sj=-1;
        
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (park[i].charAt(j)=='S') {
                    arr[i][j]=2;
                    si = i;
                    sj = j;
                }
                else if (park[i].charAt(j)=='O') {
                    arr[i][j]=0;
                }
                else {
                    arr[i][j]=1;
                }
            }
        }
        
        for (String route: routes) {
            String[] token = route.split(" ");
            int n = Integer.parseInt(token[1]);
            
            int ni = si;
            int nj = sj;
            
            boolean flag = true;
                        
            if (token[0].equals("N")) {
                int i = 0;
                while (i<n) {
                    ni-=1;
                    flag = possible(ni, nj, N, M, arr);
                    if (!flag) break;
                    i++;
                }
            }
            else if (token[0].equals("S")) {
                int i = 0;
                while (i<n) {
                    ni+=1;
                    flag = possible(ni, nj, N, M, arr);
                    if (!flag) break;
                    i++;
                }
            }
            if (token[0].equals("W")) {
                int i = 0;
                while (i<n) {
                    nj-=1;
                    flag = possible(ni, nj, N, M, arr);
                    if (!flag) break;
                    i++;
                }
            }
            if (token[0].equals("E")) {
                int i = 0;
                while (i<n) {
                    nj+=1;
                    flag = possible(ni, nj, N, M, arr);
                    if (!flag) break;
                    i++;
                }
            }
            
            // System.out.println(ni+" "+nj);
            
            if (flag) {
                si=ni;
                sj=nj;
            }
            
            // System.out.println(si+" "+sj);
        }
        
        return new int[]{si, sj};
    }
}