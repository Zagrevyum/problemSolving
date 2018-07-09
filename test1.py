numbers = [1, 1, 1, 2, 2, 5, 5, 5,5, 3]
count = {}
for number in numbers:
    try:
        count[number] += 1
    except KeyError:
        count[number] = 1
max = 0
min = 0
for value in count:
    if count[value] > max:
        max = count[value]
        min = value
    elif count[value] == max and min > value:
        min = value
print(min, max)



