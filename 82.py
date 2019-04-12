class Variant:
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __le__(self, other):
        return self.val <= other.val

    def __ge__(self, other):
        return self.val >= other.val


class Square:
    def __init__(self, diffculty, val):
        self.difficulty = diffculty
        self.val = val

    def __repr__(self):
        return self.difficulty


def step(pos):
    print(pos)
    if pos != [SIZE - 1, 0]:
        difficulty = arr[pos[0]][pos[1]]
        if pos[0] + 1 <= SIZE - 1:
            arr[pos[0] + 1][pos[1]] = Square(arr[pos[0] + 1][pos[1]], difficulty + arr[pos[0] + 1][pos[1]])
            step([pos[0] + 1, pos[1]])
        if pos[1] - 1 >= 0:
            arr[pos[0]][pos[1] - 1] = Square(arr[pos[0]][pos[1] - 1], difficulty + arr[pos[0]][pos[1] - 1])
            step([pos[0], pos[1] - 1])
        if (pos[0] + 1 < SIZE - 1) and (pos[1] - 1 >= 0):
            arr[pos[0] + 1][pos[1] - 1] = Square(arr[pos[0] + 1][pos[1] - 1], difficulty + arr[pos[0] + 1][pos[1] - 1])
            step([pos[0] + 1, pos[1] - 1])


arr = []
SIZE = 8
for i in range(SIZE):
    a = input()
    arr.append(a.split())
for i in range(SIZE):
    for j in range(SIZE):
        arr[i][j] = int(arr[i][j])
step([0, SIZE - 1])
print(arr)
pos = [SIZE - 1, 0]
count = 0
s = 0
while pos != [0, SIZE - 1]:
    variants = []
    if pos[0] - 1 >= 0:
        variants.append(Variant(arr[pos[0] - 1][pos[1]], pos[0] - 1, pos[1]))

    if pos[0] + 1 <= SIZE - 1:
        variants.append(Variant(arr[pos[0]][pos[1] + 1], pos[0], pos[1] + 1))

    if (pos[0] - 1 >= 0) and (pos[0] + 1 <= SIZE - 1):
        variants.append(Variant(arr[pos[0] - 1][pos[1] + 1], pos[0] - 1, pos[1] + 1))

    m = min(variants)
    s += m
