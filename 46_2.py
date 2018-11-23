def change_time_type(time):
    if type(time) == str:
        return int(time.split()[0]) * 60 + int(time.split()[1])
    return str(time // 60) + ' ' + str(time % 60)


class Person:

    def __init__(self, w_t, c_t):
        self.work_time = 20
        self.wait_time = w_t
        self.current_time = c_t


n = int(input())
arr = [Person] * n
ans = [False] * n
TIME = 24 * 60
queue = []
for i in range(n):
    a = input().split()
    person = Person(int(a[2]), change_time_type(a[0] + ' ' + a[1]))
    arr[i] = person

for i in range(TIME):
    current_time = i
    for j in range(len(arr)):
        if arr[j].current_time == i:
            if arr[j].wait_time > len(queue):
                queue.append(j)
            else:
                ans[j] = arr[j].current_time



