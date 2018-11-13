class Book:
    def __init__(self, left, right, number):
        self.left = left
        self.right = right
        self.number = number

    def __str__(self):
        return str(self.left.number) + '-' + self.number + '-' + str(self.right.number)

    def __repr__(self):
        return str(self)


def write(start):
    if start is not None:
        print(start.number, end='-')
        write(start.right)


n = int(input())
left = None
right = None

for i in range(n):
    a = input().split()
    if left is None or right is None:
        left = right = Book(None, None, a[1])

    else:
        if a[0] == '1':
            book = Book(None, left, a[1])
            left.left = book
            left = book
        elif a[0] == '2':
            book = Book(right, None, a[1])
            right.right = book
            right = book
        elif a[0] == '3':
            print(left.number)
            left = left.right
            if left is not None:
                left.left = None
        elif a[0] == '4':
            print(right.number)
            right = right.left
            if right is not None:
                right.right = None
    # print(left.number, right.number)
    # print('s-', end='')
    # write(left)
    # print('e')
