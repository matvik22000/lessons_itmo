import math

MATH_POW = math.pow(2, 30)


class Number:
    def __init__(self, left, right, number):
        self.left = left
        self.right = right
        self.number = int(number)

    def __str__(self):
        try:
            l = self.left.number
        except AttributeError:
            l = None
        try:
            r = self.right.number
        except AttributeError:
            r = None
        return str(l) + '-' + str(self.number) + '-' + str(r)

    def __repr__(self):
        return str(self)


line1 = input().split()
n = int(line1[1])
l = int(line1[0])
left = None
right = None
nums = input().split()
arr = []
if l == 1:
    print(0)
else:
    for i in range(l):
        a = nums[i]
        num = Number(None, None, a)
        arr.append(num)

        if i == 0:
            left = num
        else:
            num.left = arr[i - 1]
        arr[i - 1].right = num
        if i + 1 == l:
            right = num

    # print(arr)

    for i in range(n):
        x = left.number
        y = right.number
        # print(x, y)
        if x < y:
            num = Number(right, None, (x + y) % MATH_POW)
            left = left.right
            left.left = None
            right = num
            right.left.right = right
        else:
            # print(left, right)
            num = Number(None, left, (y - x + MATH_POW) % MATH_POW)
            right = right.left
            right.right = None
            left = num
            left.right.left = left

        # print(left, right)

    for i in range(l):
        a = left
        print(a.number, end=' ')
        try:
            left = a.right
        except AttributeError:
            pass
