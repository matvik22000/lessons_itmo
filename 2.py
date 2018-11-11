c = input()
a = input()
arr = a.split()
for i in range(0, len(arr)):
    arr[i] = int(arr[i])

ans = 0
for i in arr:
    ans += i

if ans > 0:
    print('Right')
elif ans < 0:
    print('Left')
elif ans == 0:
    print('Stay')

