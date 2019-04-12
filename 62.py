import sys


def compare(el1, el2):
    num1 = el1.num
    num2 = el2.num
    digits1 = el1.digits
    digits2 = el2.digits
    if len(digits1) == len(digits2):
        return int(el1.num) > int(el2.num)
    elif len(digits1) > len(digits2):
        while len(digits1) > len(digits2):
            num2 += el2.digits[-1]
            digits2 += el2.digits[-1]
    else:
        while len(digits1) < len(digits2):
            num1 += el1.digits[-1]
            digits1 += el1.digits[-1]
    return int(num1) > int(num2)



class Number:
    def __init__(self, num):
        num = num.rstrip()
        self.num = num
        self.digits = []
        for i in range(len(num)):
            self.digits.append(num[0])
    def __repr__(self):
        return self.num

arr = []
while True:
    line = sys.stdin.readline()

    if line == "\n" or line == "":
        break
    number = Number(line)
    arr.append(number)
ans = ""

if len(arr) != 1:
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            print(arr[j], arr[min_ind], compare(arr[j], arr[min_ind]))
            if compare(arr[j], arr[min_ind]):
                min_ind = j
        print(arr[i], arr[min_ind])
        b = arr[i]
        arr[i] = arr[min_ind]
        arr[min_ind] = b
        print(arr[i], arr[min_ind])
print(arr)

for i in arr:
    ans += i.num

print(ans)
