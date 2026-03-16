T = int(input())
ans=[]
arr = [list(map(int, input().split())) for _ in range(T)]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    sum = 0

    for i in range(10):
        if arr[test_case-1][i]%2==1:
            sum+=arr[test_case-1][i]
    ans.append(sum)
    # ///////////////////////////////////////////////////////////////////////////////////
for i in range(T):
    print("#%d %d" % (i+1, ans[i]))