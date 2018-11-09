a = input()
arr = a.split()
stack = []
for i in arr:
    if i != '-' and i != '+' and i != '*':
        stack.append(int(i))
    elif i == '+':
        num1 = stack.pop(-1)
        num2 = stack.pop(-1)
        stack.append(num1 + num2)
    elif i == '-':
        num1 = stack.pop(-1)
        num2 = stack.pop(-1)
        stack.append(num2 - num1)
    elif i == '*':
        num1 = stack.pop(-1)
        num2 = stack.pop(-1)
        stack.append(num1 * num2)

print(stack.pop(-1))