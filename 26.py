def rec(arr, p, list):
    for i in p:
        for j in p:
            if arr[i][j] == 1:
                return False
    ans = []
    for i in p:
        for j in arr:
            if arr[i][j] == 1:
                ans += j
    for i in ans:


