list1 = [9, 4, 5, 6]
list2 = [3, 3, 4, 5]


def sum2lists(list1, list2):
    total_sum = []
    list2.reverse()
    list1.reverse()
    while len(list1) > len(list2):
        list2.append(0)
        print(list2)
    while len(list1) < len(list2):
        list1.append(0)
        print(list1)
    carry = 0
    for x, y in zip(list1, list2):
        print(x, y, carry)
        total_sum.append((x+y+carry)%10)
        carry = (x+y+carry)//10
    if carry > 0:
        total_sum.append(carry)
    total_sum.reverse()
    print(total_sum)


sum2lists(list1, list2)
