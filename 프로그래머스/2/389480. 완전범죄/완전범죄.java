class Solution {
    public int solution(int[][] info, int n, int m) {
        int N = info.length;
        
        int[][] dp = new int[N+1][m];
        int INF = Integer.MAX_VALUE;
        
        for (int i=0; i<=N; i++) {
            for (int j=0; j<m; j++) {
                dp[i][j]=INF;
            }
        }
        
        dp[0][0]=0;
        
        for (int i=1; i<=N; i++) {
            for (int j=0; j<m; j++) {
                if (dp[i-1][j] == INF) continue;
                int curA = info[i-1][0];
                int curB = info[i-1][1];
                
                if (dp[i-1][j]+curA<n) {
                    dp[i][j] = Math.min(dp[i][j], dp[i-1][j]+curA);    
                }

                if (j+curB<m) {
                    dp[i][j+curB] = Math.min(dp[i-1][j], dp[i][j+curB]);
                }
            }
        }
        
        int answer = INF;
        
        for (int j=0; j<m; j++) {
            answer = Math.min(answer, dp[N][j]);
        }
        
        answer = (answer!=INF)? answer:-1;
                
        return answer;
    }
}