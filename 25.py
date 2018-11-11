n = int(input())
arr = []
arr1 = []

for i in range(n):
    arr1 = []
    for j in range(n):
        arr1.append(0)
    arr.append(arr1)

for i in range(n):
    a = input().split()
    for j in range(n):
        arr[i][j] = int(a[j])

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and i <= j:
            print(i + 1, j + 1)
