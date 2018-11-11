a = input()
l = int(a.split()[0])
arr = []
arr1 = []
ans = 0
for i in range(l):
    arr1 = []
    for j in range(l):
        arr1.append(0)
    arr.append(arr1)
for i in range(l):
    a = input()
    a = a.split()
    for j in range(len(a)):
        arr[i][j] = int(a[j])

for i in range(l):
    for j in range(l):
        if arr[i][j] == 1:
            ans += 1

print(ans // 2)
