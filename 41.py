a = input()
arr = []
b = True
for i in a:
    if i == '(':
        arr.append(i)
    else:
        try:
            arr.pop(-1)
        except:
            if b:
                print("NO")
                b = False

if b:
    if len(arr) == 0:
        print("YES")
    else:
        print('NO')




