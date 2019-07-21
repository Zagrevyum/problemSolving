def mergeSortedArrays(list1: list, list2: list) -> list:
    result = []
    j = 0
    i = 0
    while list1 and list2:
        print(list1, list2)
        if list1[i] == list2[j]:
            result.append(list1[i])
            list1.pop(i)
            list2.pop(j)
        elif list1[i] < list2[j]:
            result.append(list1[i])
            list1.pop(i)
        elif list1[i] > list2[j]:
            result.append(list2[j])
            list2.pop(j)
    result = result + list1 + list2
    return result



list1 = [0, 3, 5, 6]
list2 = [1,2,3,4,5,7]

print(mergeSortedArrays(list1, list2))