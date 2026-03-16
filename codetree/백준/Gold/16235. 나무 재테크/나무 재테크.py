from collections import deque
def init_tree():
    tree_loc = [[deque() for _ in range(n)] for _ in range(n)]
    for i, j, age in B:
        tree_loc[i - 1][j - 1].append(age)
    return tree_loc

def spring(tree_loc):
    died_tree_loc = [[deque() for _ in range(n)] for _ in range(n)]
    new_tree_loc = [[deque() for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if tree_loc[i][j]:

                while tree_loc[i][j]:
                    age = tree_loc[i][j].popleft()
                    if graph[i][j] >= age:
                        graph[i][j] -= age
                        new_tree_loc[i][j].append(age + 1)
                    else:
                        died_tree_loc[i][j].append(age)

    return died_tree_loc, new_tree_loc


def summer(died_tree):
    for i in range(n):
        for j in range(n):
            while died_tree[i][j]:  # 죽은 나무가 있다면
                graph[i][j] += died_tree[i][j].popleft() // 2  # 양분 추가

def fall(tree_loc):

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for x in range(n):
        for y in range(n):
            if tree_loc[x][y]:
                for age in tree_loc[x][y]:
                    if age % 5 != 0:  # 번식하는 나무 5의 배수인 경우만
                        continue

                    for i in range(8):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < n and 0 <= ny < n:
                            tree_loc[nx][ny].appendleft(1)
    # print("새로 추가된 나무", new_trees)
    # print(tree_loc)

def winter():
    for i in range(n):
        for j in range(n):
            graph[i][j] += A[i][j]

n, m, k = map(int, input().split())
graph = [[5] * n for _ in range(n)]

A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]

k *= 4  # k를 사계절로

# 처음 나무 심기
tree_loc = init_tree()

died_tree = []

while k > 0:
    if k % 4 == 0:
        died_tree, tree_loc = spring(tree_loc)
        # print("봄")

    elif k % 4 == 3:
        summer(died_tree)
        # print("여름")

    elif k % 4 == 2:
        # print("sage",tree_loc)
        fall(tree_loc)
        # print("가을")

    else:
        winter()
        # print("결")
    k -= 1

print(sum(len(tree_loc[i][j]) for i in range(n) for j in range(n)))
