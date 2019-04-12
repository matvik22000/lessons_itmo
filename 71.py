
def search(arr, key):
    left = -1
    right = len(arr)
    while left < right - 1:
        mid = (left + right) // 2
        if arr[mid] < key:
            left = mid
        else:
            right = mid
    if right == len(arr):
        return -1
    if arr[right] == key:
        return right
    else:
        return -1


count = input()
arr = input().split()
b = input().split()
for i in range(len(arr)):
    arr[i] = int(arr[i])

for i in b:
    i = int(i)
    if i < arr[-1]:
        if search(arr, i) != -1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")



