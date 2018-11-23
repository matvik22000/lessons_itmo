import math
from collections import deque

MATH_POW = math.pow(2, 30)
line1 = input().split()
n = int(line1[1])
l = int(line1[0])
nums = input().split()
deq = deque()
for i in range(l):
    deq.append(int(nums[i]))

for i in range(n):
    if l != 1:
        x = deq.popleft()
        y = deq.pop()
        if x < y:
            deq.append(y)
            a = int((x + y) % MATH_POW)
            deq.append(a)
        else:
            deq.appendleft(x)
            a = int((y - x + MATH_POW) % MATH_POW)
            deq.appendleft(a)
    else:
        x = deq.pop()
        deq.appendleft(0)

ans = ''
for i in deq:
    ans += str(i) + ' '
f = open('sleepgame.out', 'w')
f.write(ans)
f.close()
