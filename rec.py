i = input()
i = int(i)


def rec(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    else:
        return rec(i - 1) + rec(i - 2)


print(rec(i))
