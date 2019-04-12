def search_right(key):
    left = -1
    right = len(arr)
    while left < right - 1:
        mid = (left + right) // 2
        if arr[mid] <= key:
            left = mid
        else:
            right = mid

    return right


def search_left(key):
    left = -1
    right = len(arr)
    while left < right - 1:
        mid = (left + right) // 2
        if arr[mid] <= key:
            left = mid
        else:
            right = mid

    return right


a1 = input()
arr = input().split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

arr.sort()
k = int(input())
pairs = []
for i in range(k):
    a = input().split()
    pairs.append([int(a[0]), int(a[1])])

for i in pairs:
    l = search_left(i[0] - 1)
    r = search_right(i[1])
    print(str(r - l), end=' ')
