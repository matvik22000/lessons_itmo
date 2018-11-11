a = input()
cur_max = 0
for i in a:
    if ord(i) > cur_max:
        cur_max = ord(i)

print(chr(cur_max))