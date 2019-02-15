def search(arr, key):
    left = -1
    right = len(arr)
    while left < right - 1:
        mid = (left + right) // 2
        if arr[mid] < key:
            left = mid
        else:
            right = mid

    try:
        if arr[right] == key:
            return right
        else:
            return -1
    except IndexError:
        return -1



