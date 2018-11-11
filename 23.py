a = input()
n = int(a.split()[0])
m = int(a.split()[1])
inp = []
for i in range(n):
    a = input()
    a1 = int(a.split()[0])
    a2 = int(a.split()[1])
    inp.append([a1, a2])

arr = []
arr1 = []
for i in range(n):
    arr1 = []
    for j in range(n):
        arr1.append(0)
    arr.append(arr1)

for i in inp:
    p1 = i[0] - 1
    p2 = i[1] - 1
    arr[p1][p2] = 1
    arr[p2][p1] = 1

for i in arr:
    for j in i:
        print(j, end = ' ')
    print(' ')





