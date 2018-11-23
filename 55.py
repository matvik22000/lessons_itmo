n = int(input())
arr = input().split()
ans = []
MAX = 601
d = {}
for i in range(len(arr)):
    try:
        d[int(arr[int(i)])].append(i)
    except KeyError or IndexError:
        d[int(arr[int(i)])] = [i]

for i in range(0, MAX):

    try:
        if len(d[i]) > 0:
            for j in range(len(d[i])):
                # print(d, i, j, d[i][j])
                ans.append(d[i][j])

    except KeyError:
        pass

for i in ans[::-1]:
    print(i + 1, end=' ')
