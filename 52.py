n = int(input())
arr = input().split()
ans = [0, 0]
MAX = 1001
d = {0: 0}
for i in arr:
    try:
        d[int(i)] += 1
    except KeyError:
        d[int(i)] = 1

for i in range(MAX):
    try:
        if d[i] > 0:
            if d[i] > ans[0]:
                ans[1] = i
                ans[0] = d[i]
    except KeyError:
        pass

print(ans[1])
