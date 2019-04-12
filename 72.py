    def check(val, l):
        a = 0
        for i in arr:
            a += i // val
        if a < l:
            return -1
        elif a > l:
            return 1
        elif a == l:
            return 0


    def search(max, l):
        left = 0
        right = max + 1
        while left < right - 1:
            mid = (left + right) // 2
            a = check(mid, l)
            if a >= 0:
                left = mid
            elif a == -1:
                right = mid
        return left


    a = input().split()
    n = int(a[0])
    k = int(a[1])
    arr = []
    for i in range(n):
        arr.append(int(input()))
    arr.sort()
    print(search(arr[-1], k))

