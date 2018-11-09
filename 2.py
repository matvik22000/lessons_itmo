input1 = input()
h = int(input1.split()[0])
l = int(input1.split()[1])
height = []
for i in range(h):
    n = input()
    n2 = []
    for k in n:
        n2.append(k)
    height.append(n2)

for i in range(0, len(height)):
    for k in range(0, len(height[i])):
        if height[i][k] != "#":
            if (k - 1) >= 0:
                if height[i][k - 1] == "#":
                    height[i][k] = "X"
            if (k + 1) < l:
                if height[i][k + 1] == "#":
                    height[i][k] = "X"
            if (i - 1) >= 0:
                if height[i - 1][k] == "#" :
                    height[i][k] = "X"
            if (i + 1) < h:
                if height[i + 1][k] == "#":
                    height[i][k] = "X"
for i in height:
    for k in i:
        print(k, end='')
    print('')
