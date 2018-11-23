
a = input()
a = a.split()
n = int(a[0])
m = int(a[1])
arr = []
for i in range(n):
    arr1 = []
    for j in range(n):
        arr1.append(0)
    arr.append(arr1)

for i in range(m):
    a = input()
    a = a.split()
    arr[int(a[0]) - 1][int(a[1]) - 1] = 1


print(arr)