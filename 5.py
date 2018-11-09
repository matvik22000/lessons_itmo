n = input()
a = input()
m = input()
arr = a.split()
for i in range(len(arr)):
    arr[i] = int(arr[i])

best_cur = 10000
best_index = -1
count = 0
ans = 0
change = False
while count < int(m):
    best_cur = 10000
    best_index = -1
    change = False
    for i in range(len(arr)):
        if arr[i] % 10 == 0 and arr[i] > 0 and arr[i] != 10:
            if int(arr[i]) < best_cur:
                best_cur = int(arr[i])
                best_index = i
                change = True
    if not change:
        for i in range(len(arr)):
            if arr[i] > 10:
                best_cur = arr[i]
                best_index = i
                change = True
    if not change:
        count = int(m)
    if best_cur > 10 and best_cur != 10000:
        arr.append(10)
        arr[best_index] -= 10
    count += 1

for i in arr:
    if i == 10:
        ans += 1
print(ans)
