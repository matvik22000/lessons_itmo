n = int(input())
arr = input().split()
ans = []
MAX = 10001
d = {0: 0}
for i in arr:
    try:
        d[int(i)] += 1
    except KeyError:
        d[int(i)] = 1

for i in range(MAX):
    try:
        if d[i] > 0:
            for j in range(d[i]):
                ans.append(i)
    except KeyError:
        pass

for i in ans:
    print(i, end=' ')
