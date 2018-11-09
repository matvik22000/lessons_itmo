arr = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]
queue = []
levels = []
for i in range(0, len(arr)):
    levels.append([])
print(levels)
used = [False] * 6
queue.append([0, 0])
while len(queue) > 0:
    el = queue.pop(0)
    levels[el[1]].append(el[0])
    if not used[el[0]]:
        print(el[0] + 1)
        used[el[0]] = True
        for i in range(len(arr[el[0]])):
            if arr[el[0]][i] == 1 and not used[i]:
                queue.append([i, el[1] + 1])


print(levels)

