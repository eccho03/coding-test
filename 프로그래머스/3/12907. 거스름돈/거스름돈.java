class Solution {
    public int solution(int n, int[] money) {
        int answer = 0;
        int MOD = 1000000007;
        
        int []dp = new int[n+1];
        
        dp[0] = 1;
        
        for (int j=0; j<money.length; j++) {
            for (int i=1; i<=n; i++) {
                if (i-money[j]>=0) dp[i] += dp[i-money[j]]%MOD;
            }
        }
        
        // for (int num: dp) {
        //     System.out.println(num);
        // }
        answer = dp[n];
        return answer;
    }
}