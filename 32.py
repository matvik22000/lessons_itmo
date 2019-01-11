n = int(input())
arr = []
for i in range(n):
    arr1 = []
    for j in range(n):
        arr1.append(0)
    arr.append(arr1)

for i in range(1, n):
    a = input().split()
    for j in a:
        arr[int(j) - 1][i] = 1

start = 0
levels = [[start]]
while True:
    levels.append([])
    for j in range(len(levels[-2])):
        for k in range(len(arr[levels[-2][j]])):
            if arr[levels[-2][j]][k] == 1:
                levels[-1].append(k)

    if len(levels[-1]) == 0:
        break

print(len(levels) - 2)
print(len(levels[-2]))
levels[-2].sort()
for i in levels[-2]:
    print(i + 1, end=' ')

