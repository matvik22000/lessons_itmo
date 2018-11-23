def change_time_type(time):
    if type(time) == str:
        t = time.split()
        return int(t[0]) * 3600 + int(t[1]) * 60 + int(t[2])
    return str(time // 3600) + ' ' + str((time % 3600) // 60) + ' ' + str((time % 3600) % 60)


n = int(input())
arr = []
ans = []
MAX = 3600 * 60
d = {0: 0}
t = ''
for i in range(n * 3):
    if i % 3 == 0:
        if t != '':
            arr.append(change_time_type(t))
        t = input()
    else:
        t += ' ' + input()
arr.append(change_time_type(t))
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
    print(change_time_type(i))
