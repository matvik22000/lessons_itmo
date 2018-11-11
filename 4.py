a = input()
b = input()
a = a.split()
b = b.split()
pg_width = int(a[0])
pg_height = int(a[1])
num = int(b[0])
l_width = int(b[1])
l_height = int(b[2])
strings_num = pg_height // l_height
l_in_srt = pg_width // l_width
l_in_pg = l_in_srt * strings_num
if (l_width > pg_width) or (l_height > pg_height) :
    print(-1)
else:
    pg = num // l_in_pg
    if num % l_in_pg != 0:
        pg += 1
    print(pg)

