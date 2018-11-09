def bin_search(a, item):
    first = 0
    last = len(a) - 1
    while first <= last:
        mid = round((first + last) / 2)
        if a[mid] == item:
            raise Exception('error')
        else:
            if item < a[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return first

m = input()
nums = [-1] * 100001
free_places = []
for i in range(100000):
    free_places.append(i + 1)

for i in range(int(m)):
    event = input()
    a = event.split()
    tp = a[0]
    num = int(a[1])
    if tp == "+":
        place = free_places[0]
        del free_places[0]
        nums[num] = place
        print(place)

    elif tp == "-":
        car_place = nums[num]
        free_places.insert(bin_search(free_places, car_place), car_place)
        nums[num] = -1

# print(len(free_places))





