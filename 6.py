a = input()
arr = []
sum = 0
for i in a:
    mark = (ord('Z') + 1) - ord('A') - (ord(i) - ord('A'))
    arr.append(mark)
    sum += mark
mid = sum / (len(arr))
ans = 0
if round(mid) < min(arr) + 1:
    ans = round(mid)
else:
    ans = round(min(arr) + 1)
ans2 = chr(ord('A') + ord('Z') - ord('A') - ans + 1)
print(ans2)