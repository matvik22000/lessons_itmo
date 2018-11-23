n = int(input())
arr = input().split()
ans = []
d = {0: 0}
for i in arr:
    try:
        d[int(i)] += 1
    except KeyError:
        d[int(i)] = 1

MAX = int(arr[0]) + 10000
MIN = int(arr[0]) - 10000
if MIN < 0:
    MIN = 0
for i in range(MIN, MAX):
    try:
        if d[i] > 0:
            for j in range(d[i]):
                ans.append(i)
    except KeyError:
        pass

for i in ans:
    print(i, end=' ')
