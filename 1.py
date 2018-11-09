line1 = input()
line1 = line1[::-1]
line2 = ''
for i in line1:
    if i == 'A':
        line2 += 'T'
    elif i == 'T':
        line2 += 'A'
    elif i == 'G':
        line2 += 'C'
    elif i == 'C':
        line2 += 'G'

print(line2)

