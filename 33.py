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
    if a[0] == 'F':
        arr[int(a[1]) - 1][int(a[2]) - 1] = 1
        arr[int(a[2]) - 1][int(a[1]) - 1] = 1
    else:
        arr[int(a[1]) - 1][int(a[2]) - 1] = 0
        arr[int(a[2]) - 1][int(a[1]) - 1] = 0
    it = True
    for j in arr:
        ans = 0
        for k in j:
            if j == 1:
                ans += 1
        if ans > len(arr) - 2:
            it = False
    if it:
        print(arr)
        depth = [0]
        ans = 0
        ans2 = ''
        used = [False] * n
        while len(depth) > 0:
            e = depth.pop(0)
            if not used[e]:
                used[e] = True
                for i in range(len(arr[e])):
                    if arr[e][i] == 1:
                        depth.append(i)

        if False not in used:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')









