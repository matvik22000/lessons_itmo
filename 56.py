def change_time_type(time):
    if type(time) == str:
        t = time.split(':')
        return int(t[0]) * 3600 + int(t[1]) * 60 + int(t[2])
    return str(time // 3600) + ':' + str((time % 3600) // 60) + ':' + str((time % 3600) % 60)


def sort(arr):
    ans = []
    d = {0: 0}

    for i in arr:
        try:
            d[int(i)] += 1
        except KeyError:
            d[int(i)] = 1

    for i in range(MAX):
        try:
            if d[i] > 0:
                for j in range(d[i]):
                    ans.append(i)
        except KeyError:
            pass


MAX = 3600 * 60
