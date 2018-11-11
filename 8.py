import math
h = int(input())
r = int(input())
len = math.sqrt(h * h - h / 2 * h / 2)
len = math.floor(len)

if r % len == 0:
    ans = r // len - 1
else:
    ans = r // len
print(ans)

