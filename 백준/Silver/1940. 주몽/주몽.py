def main():
    n = int(input())
    m = int(input())
    ingredient = list(map(int, input().split()))
    ingredient.sort()
    start, end = 0, n-1
    intervel_sum = 0
    cnt = 0

    while start < end:
        intervel_sum = ingredient[start] + ingredient[end]
        if intervel_sum < m:
            start += 1
        elif intervel_sum > m:
            end -= 1
        else:
            cnt += 1
            start += 1
            end -= 1

    print(cnt)

if __name__ == '__main__':
    main()