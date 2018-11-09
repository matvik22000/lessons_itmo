n = int(input())
a = input()
arr = a.split()
for i in range(len(arr)):
    arr[i] = int(arr[i])
ans = []
for i in range(n):
    ans += ' '
current_pos = 0
for k in range(len(arr)):
    max_el = -1
    for i in range(len(arr)):
        if arr[i] > max_el:
            max_el = arr[i]
            max_index = i
    # print(max_el)
    if abs(current_pos + max_el) > abs(current_pos - max_el):
        current_pos -= max_el
        ans[max_index] = "L"
    else:
        current_pos += max_el
        ans[max_index] = "R"
    # print(current_pos)
    # print(arr)
    arr[max_index] = -1

c = ""
for i in ans:
    c += i
print(c)

