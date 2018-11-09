input1 = input()
arr = input1.split()
n = int(arr[0])
a = int(arr[1])
b = int(arr[2])
c = int(arr[3])
d = int(arr[4])
iter = (a + b) * (c + d)
iterations = n // (a * (c + d) + c * (a + b))
time1 = iterations * iter
prog1 = a
prog2 = c
count = 0
bugs = n % (a * (c + d) + c * (a + b))
if bugs == 0:
    time1 -= min(b, d)
while bugs > 0:
    if prog1 > 0:
        prog1 -= 1
        bugs -= 1
        if prog1 == 0:
            prog1 = - b
    elif prog1 < 0:
        prog1 += 1
        if prog1 == 0:
            prog1 = a
    if prog2 > 0:
        prog2 -= 1
        bugs -= 1
        if prog2 == 0:
            prog2 = - d
    elif prog2 < 0:
        prog2 += 1
        if prog2 == 0:
            prog2 = c



    count += 1
ans = time1 + count
print(ans)
