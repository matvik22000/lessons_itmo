class Mouse:
    def __init__(self, left, right, name):
        self.left = left
        self.right = right
        self.name = name

    def __str__(self):
        return self.left.name + '-' + self.name + '-' + self.right.name

    def __repr__(self):
        return str(self)


a = input()
n = int(a.split()[1])
first_name = a.split()[0]
first_mouse = Mouse(None, None, first_name)
first_mouse.left = first_mouse
first_mouse.right = first_mouse
table = {first_name: first_mouse}
for i in range(n):
    a = input().split()
    name1 = a[0]
    name2 = a[1]
    rl = a[2]
    if rl == "l":
        r = table[name2]
        mouse = Mouse(r.left, r, name1)
        r.left.right = mouse
        r.left = mouse
        table[name1] = mouse

    else:
        l = table[name2]
        mouse = Mouse(l, l.right, name1)
        l.right.left = mouse
        l.right = mouse
        table[name1] = mouse

mouse = first_mouse.right
f = open('mice.out', 'w')
f.write(first_name + '\n')
while mouse != first_mouse:
    f.write(mouse.name + '\n')
    mouse = mouse.right
f.close()
