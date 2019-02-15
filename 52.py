n = int(input())
b = input()
arr = b.split()
for i in range(len(arr)):
    arr[i] = int(arr[i])

arr.sort()
t = 0
ans = 0
for i in range(len(arr)):

    try:
        if arr[i + 1] <= t + 1:

            for j in range(i, len(arr)):
                if arr[j] > arr[i]:
                    i = j

    except IndexError:
        pass

    if arr[i] - t > 0:
        ans += arr[i] - t
    arr[i] = 0
    t += 1

print(ans)
