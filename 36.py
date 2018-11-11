a = input()
n = int(a.split()[0])
m = int(a.split()[1])
v = int(a.split()[2])

arr = []
for i in range(n):
    a = input()
    arr.append([int(a.split()[0]), int(a[1])])

visited = []


def dfs(v):
    visited.append(v)
    for i in arr:
        if i[0] == v:
            if not i[1] in visited:
                dfs(i[1])
        if i[1] == v:
            if not i[0] in visited:
                dfs(i[0])
    return visited


print(dfs(v))
