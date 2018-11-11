a = input()
a = a.split()
n = int(a[0])
m = int(a[1])
start = int(a[2])
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
    arr[int(a[1]) - 1][int(a[0]) - 1] = 1

depth = [start - 1]
ans = 0
ans2 = ''
used = [False] * n
while len(depth) > 0:

    e = depth.pop(0)
    if not used[e]:
        used[e] = True
        ans += 1
        ans2 += str(e + 1) + ' '
        for i in range(len(arr[e])):
            if arr[e][i] == 1:
                depth.append(i)

print(ans)
print(ans2)










