def next_num(prev_num, count, c):
    if count >= N:
        global s
        s += c
        return
    else:
        c += 1
        if prev_num == -1:
            next_num(1, 1, 1)
            next_num(2, 1, 1)
            next_num(3, 1, 1)
            next_num(4, 1, 1)
            next_num(5, 1, 1)
            next_num(6, 1, 1)
            next_num(7, 1, 1)
            next_num(9, 1, 1)
        elif prev_num == 1:
            next_num(6, count + 1, c)
            next_num(8, count + 1, c)
        elif prev_num == 2:
            next_num(7, count + 1, c)
            next_num(9, count + 1, c)
        elif prev_num == 3:
            next_num(4, count + 1, c)
            next_num(8, count + 1, c)
        elif prev_num == 4:
            next_num(3, count + 1, c)
            next_num(9, count + 1, c)
            next_num(0, count + 1, c)
        elif prev_num == 5:
            next_num(5, count + 1, c)
        elif prev_num == 6:
            next_num(1, count + 1, c)
            next_num(7, count + 1, c)
            next_num(0, count + 1, c)
        elif prev_num == 7:
            next_num(2, count + 1, c)
            next_num(6, count + 1, c)
        elif prev_num == 8:
            next_num(1, count + 1, c)
            next_num(3, count + 1, c)
        elif prev_num == 9:
            next_num(2, count + 1, c)
            next_num(4, count + 1, c)
        elif prev_num == 0:
            next_num(4, count + 1, c)
            next_num(6, count + 1, c)


s = 0
f = open("input.txt", 'r')
N = int(f.readline())
next_num(-1, 0, 0)
f.close()
f = open("output.txt", "w")
f.write(s)
f.close()
