a = input()
a = a.split()
n = int(a[0])
m = int(a[1])
arr = []
for i in range(n):
    arr1 = []
    for j in range(n):
        arr1.append(0)
    arr.append(arr1)

for i in range(m):
    a = input()
    a = a.split()
    arr[int(a[0]) - 1][int(a[1]) - 1] = 1

used = [False] * n
stack = []

cycle_found = False

ans = None


def dfs(a):
    global cycle_found
    if not cycle_found:
        if used[a]:
            if a in stack:
                global ans7
                ans = stack[stack.index(a)::]
                cycle_found = True
            return
        stack.append(a)
        used[a] = True
        for i in range(len(arr[a])):
            if arr[a][i] == 1:
                dfs(i)
        stack.pop(-1)


dfs(0)

if cycle_found:
    print('YES')
    for i in ans:
        print(i + 1, end=' ')
else:
    print('NO')
