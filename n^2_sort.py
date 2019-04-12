
arr = []
a = input().split()
m = len(a)
for i in a:
    arr.append(int(i))

for i in range(m):
    min_ind = i
    for j in range(i + 1, m):
        if arr[j] < arr[min_ind]:
            min_ind = j
    b = arr[i]
    arr[i] = arr[min_ind]
    arr[min_ind] = b
print(arr)


