q = input()
a = input()
a = a.split()
for i in range(len(a)):
    a[i] = int(a[i])

cur_max = 0
for i in a:
    if a > 