import sys
T = int(sys.stdin.readline().rstrip())
test_cases = [sys.stdin.readline().rstrip() for _ in range(T)]
N = max(map(int, test_cases))
dp = [0]*(N+1)
if N==1:
    dp[1]=1
elif N==2:
    dp[2]=2 # 1+1 / 2
elif N==3:
    dp[3]=4 # 1+1+1 / 1+2 / 2+1
elif N==4:
    dp[4]=7
else:
    dp[1]=1
    dp[2]=2
    dp[3]=4
    dp[4]=7
    for i in range(5,N+1):
        dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1_000_000_009

for t in test_cases:
    sys.stdout.write(str(dp[int(t)])+'\n')