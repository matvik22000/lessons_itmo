a = input().split()
n = int(a[0])
m = int(a[1])
arr = []

ans = []
for i in range(n):
    ans1 = []
    for j in range(m):
        ans1.append(0)
    ans.append(ans1)
for i in range(m):
    a = input().split()
    ans[int(a[0]) - 1][i] = 1
    ans[int(a[1]) - 1][i] = 1

f = open('incident.out', 'w')
for i in ans:
    for j in range(m):
        f.write(str(i[j]) + ' ')
    f.write('\n')
f.close()

