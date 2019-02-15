def bfs(arr, target):
    size = len(arr)
    d = 0
    arr[0][0] = d
    while True:
        for i in range(size):
            for j in range(size):
                if arr[i][j] == d:
                    arr = mark(i, j, d, arr)
        d += 1
        if arr[target[0]][target[1]] == d:
            break


def dfs(arr, start, d):





def mark(x, y, d, arr):
    try:
        if arr[x - 1][y] != d:
            arr[x - 1][y] = d + 1
    except IndexError:
        pass
    try:
        if arr[x - 1][y + 1] != d:
            arr[x - 1][y + 1] = d + 1
    except IndexError:
        pass
    try:
        if arr[x - 1][y - 1] != d:
            arr[x - 1][y - 1] = d + 1
    except IndexError:
        pass

    try:
        if arr[x + 1][y] != d:
            arr[x + 1][y] = d + 1
    except IndexError:
        pass
    try:
        if arr[x + 1][y + 1] != d:
            arr[x + 1][y + 1] = d + 1
    except IndexError:
        pass
    try:
        if arr[x + 1][y - 1] != d:
            arr[x + 1][y - 1] = d + 1
    except IndexError:
        pass
    try:
        if arr[x][y + 1] != d:
            arr[x][y + 1] = d + 1
    except IndexError:
        pass
    try:
        if arr[x][y - 1] != d:
            arr[x][y - 1] = d + 1
    except IndexError:
        pass
    return arr



a = int(input())
SIZE = 100
field = []
for i in range(SIZE):
    arr = []
    for j in range(SIZE):
        arr.append('_')
    field.append(arr)

for i in range(a):
    t = input().split()
    x = int(t[0])
    y = int(t[1])

    for k in range(x, x + 5):
        for j in range(y, y + 5):
            field[k][j] = 101

f = open("test.txt", "w")
for i in range(100):
    print(field[i], file=f)
f.close()
