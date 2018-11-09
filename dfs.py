arr = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0],
]

used = [False] * 6


def dfs(a):
    if used[a]:
        return
    used[a] = True
    print(a + 1)
    for i in range(len(arr[a])):
        if arr[a][i] == 1:
            dfs(i)

dfs(0)

