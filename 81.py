def jump(pos):
    if pos == n - 1:
        global count
        count += 1
    else:
        for i in range(1, k + 1):
            p = pos + i
            if p < n:
                jump(p)


count = 0
n = 8
k = 2
jump(0)
print(count)

