arr = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0],
]


LEN = 6
queue = []
used = [False] * LEN
queue.append(0)
while len(queue) > 0:
    el = queue.pop(0)
    if not used[el]:
        print(el + 1)
        used[el] = True
        for i in range(len(arr[el])):
            if arr[el][i] == 1:
                queue.append(i)

