a = input()
arr = []
written = False
for i in a:
    if i == '{' or i == '[' or i == '(':
        arr.append(i)
    else:
        try:
            c = arr.pop(-1)
            if (c == '(' and i == ')') or (c == '{' and i == '}') or (c == '[' and i == ']'):
                pass
            else:
                if not written:
                    print('NO')
                    written = True
        except:
            if not written:
                print('NO')
                written = True


if not written:
    if len(arr) == 0:
        print('YES')
    else:
        print('NO')


