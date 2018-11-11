class Person:
    def __init__(self, time, pr, num):
        self.time = time
        self.product = pr
        self.num = num

    def d(self):
        ans[self.num] = current_time - self.time

    def time_lim(self):
        ans[self.num] = -1

    def __repr__(self):
        return str(self.product) + '-' + str(self.time)


def find():
    if len(queue) > 0:
        # print(queue, products)
        # print(queue[0].product, products[queue[0].product], current_time)
        if products[queue[0].product] != 0:
            queue[0].d()
            products[queue[0].product] -= 1
            queue.pop(0)
            find()


current_time = 0
queue = []
products = [0] * 10001
n = int(input())
ans = ['place'] * n
for i in range(n):
    a = input().split()
    t = int(a[0])
    current_time = int(a[1])
    product = int(a[2])
    if t == 1:
        products[product] += 1
    else:
        person = Person(current_time, product, i)
        queue.append(person)
    find()

if len(queue) > 0:
    for i in queue:
        i.time_lim()

for i in ans:
    if i != 'place':
        print(i, end=' ')
