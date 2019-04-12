class Bus:
    def __init__(self, size, num):
        self.size = size
        self.num = num


a = input().split()
n = int(a[0])
m = int(a[1])
arr = []
a = input().split()
count = 0
for i in range(len(a)):
    bus = Bus(int(a[i]), i)
    arr.append(bus)
if len(arr) > 1:
    for i in range(m):
        min_ind = i
        for j in range(i + 1, m):
            if arr[j].size < arr[min_ind].size:
                min_ind = j
        b = arr[i]
        arr[i] = arr[min_ind]
        arr[min_ind] = b

ans = ""
while n > 0:
    if len(arr) > 0:
        count += 1
        n -= arr[-1].size
        ans += str(arr[-1].num + 1) + " "
        arr.pop(-1)
    else:
        ans = "-1"
        break
if ans != "-1":
    print(count)
print(ans)