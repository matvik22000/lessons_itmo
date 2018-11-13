def in_process():
    if current_person is not None:
        return 1
    return 0

def ret_time(c_t):
    if type(c_t) == str:
        return int(c_t.split()[0]) * 60 + int(c_t.split()[1])
    return str(c_t // 60) + ' ' + str(c_t % 60)


def work(current_person):
    # print(queue, arr)
    # print(ret_time(c_t), ret_time(last_time))
    if current_person is not None:
        if current_person.time_left <= 0:
            # print(c_t, last_time)
            person = queue.pop(0)
            current_person = person
            print(ret_time(cur_time))
            # ans[person.number] = ret_time(c_t) + ' 1'
        current_person.time_left -= 1
    else:
        if len(queue) > 0:
            person = queue.pop(0)
            current_person = person

    return current_person


class Person:
    def __init__(self, time, patience, number, time_left):
        self.time = int(time)
        self.patience = patience
        self.number = number
        self.time_left = time_left

    def __repr__(self):
        return str(self.number)


n = int(input())
queue = []
ans = [False] * n
arr = []
for i in range(n):
    a = input().split()
    patience = int(a[2])
    cur_time = int(a[0]) * 60 + int(a[1])
    person = Person(cur_time, patience, i, 20)
    arr.append(person)
last_time = arr[0].time
cur_time = 0
current_person = None
while len(queue) > 0 or len(arr) > 0:
    print(current_person)
    if len(arr) > 0:
        person = arr[0]
        if cur_time == person.time:
            arr.pop(0)
            print(person.patience, len(queue), person.patience < len(queue) + in_process())
            if person.patience < len(queue) + in_process():
                print(ret_time(person.time), 't')
                # ans[person.number] = ret_time(person.time) + ' ' + '2'
            else:
                queue.append(person)

    current_person = work(current_person)
    cur_time += 1


# print(ans)
