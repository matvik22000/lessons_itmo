a = input()
arr = []
written = False
for i in a:
    if i == '{' or i == '[' or i == '(':
        arr.append(i)
    else:
        try:
            count = arr.pop(-1)
            if (count == '(' and i == ')') or (count == '{' and i == '}') or (count == '[' and i == ']'):
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


