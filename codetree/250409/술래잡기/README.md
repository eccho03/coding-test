# [술래잡기 ![Gold1][g1]](https://www.codetree.ai/training-field/search/problems/hide-and-seek)

|유형|출처|
|---|---|
|[dx dy technique](https://www.codetree.ai/training-field/search/?tags=dx+dy+technique), [Simulation](https://www.codetree.ai/training-field/search/?tags=Simulation)|[일반연습 / 문제은행](https://www.codetree.ai/training-field/home)|


# [REVIEW]
하 쉬웠는데 디테일이 떨어져서 제대로 풀지 못했다..

1)
```Python
if not (1<=ni<=N and 1<=nj<=N):  # 범위 밖이라면
    dr = opp[dr]
    ni, nj = ci + di[dr], cj + dj[dr]
    if (ni, nj) == (ti, tj):  continue
```
범위 밖이라면 방향 이동 후 다시 이동한 다음 **그 좌표도 술래 유무 확인**  

2)
```Python
ti,tj,td = (N+1)//2, (N+1)//2
```
아니 (N+1)//2인데 N//2로 계산했다... 잘못하면 큰 문제 되니까 무조건 확인하자

3)
술래 이동 시 *두 번에 한 번씩 길이 증가* 이 규칙을 제대로 찾았더라면 ,,
한 번에 한 번이라고 착각했다..

4)
```Python
for i in range(len(arr) - 1, -1, -1):
    ci, cj, dr = arr[i]
    if (ci, cj) in target and (ci, cj) not in tree:
        arr.pop(i)
        ans += T
```
배열에서 pop 해야 될 때는 무조건 **역순으로 for문 돌면서** pop 해주기 명심 !!
(잘못하면 인덱스 꼬일 수 있음)

[b5]: https://img.shields.io/badge/Bronze_5-%235D3E31.svg
[b4]: https://img.shields.io/badge/Bronze_4-%235D3E31.svg
[b3]: https://img.shields.io/badge/Bronze_3-%235D3E31.svg
[b2]: https://img.shields.io/badge/Bronze_2-%235D3E31.svg
[b1]: https://img.shields.io/badge/Bronze_1-%235D3E31.svg
[s5]: https://img.shields.io/badge/Silver_5-%23394960.svg
[s4]: https://img.shields.io/badge/Silver_4-%23394960.svg
[s3]: https://img.shields.io/badge/Silver_3-%23394960.svg
[s2]: https://img.shields.io/badge/Silver_2-%23394960.svg
[s1]: https://img.shields.io/badge/Silver_1-%23394960.svg
[g5]: https://img.shields.io/badge/Gold_5-%23FFC433.svg
[g4]: https://img.shields.io/badge/Gold_4-%23FFC433.svg
[g3]: https://img.shields.io/badge/Gold_3-%23FFC433.svg
[g2]: https://img.shields.io/badge/Gold_2-%23FFC433.svg
[g1]: https://img.shields.io/badge/Gold_1-%23FFC433.svg
[p5]: https://img.shields.io/badge/Platinum_5-%2376DDD8.svg
[p4]: https://img.shields.io/badge/Platinum_4-%2376DDD8.svg
[p3]: https://img.shields.io/badge/Platinum_3-%2376DDD8.svg
[p2]: https://img.shields.io/badge/Platinum_2-%2376DDD8.svg
[p1]: https://img.shields.io/badge/Platinum_1-%2376DDD8.svg
[passed]: https://img.shields.io/badge/Passed-%23009D27.svg
[failed]: https://img.shields.io/badge/Failed-%23D24D57.svg
[easy]: https://img.shields.io/badge/쉬움-%235cb85c.svg?for-the-badge
[medium]: https://img.shields.io/badge/보통-%23FFC433.svg?for-the-badge
[hard]: https://img.shields.io/badge/어려움-%23D24D57.svg?for-the-badge
