import operator
from itertools import accumulate

numbers = [2, 3, 4, 5, 0, 6]
numbers1 = [2, 3, 4, 5, 7, 6]
def sol1(numbers):
    initialProductValue = [1]
    result = []
    leftProduct = initialProductValue + (list(accumulate(numbers, operator.mul)))
    numbers.reverse()
    rightProduct = initialProductValue + (list(accumulate(numbers, operator.mul)))
    numbers.reverse()
    leftProduct.pop()
    rightProduct.pop()
    rightProduct.reverse()
    for number in range(len(numbers)):
        result.append(leftProduct[number] * rightProduct[number])
    print(result)


def sol2(numbers):
    prod = 1
    result =[]
    i = 0
    while(i < len(numbers)):
        result.append(prod)
        prod *= numbers[i]
        i += 1
    i -=1
    prod = 1
    while(i >= 0):
        result[i] *= prod
        prod *= numbers[i]
        i-=1
    print(result)




sol1(numbers)
sol2(numbers)
sol1(numbers1)
sol2(numbers1)


"""accumulatedProduct = 1
for number in numbers:
    accumulatedProduct *= number
    #print (accumulatedProduct)
    leftProduct.append(accumulatedProduct)

print (leftProduct)
accumulatedProduct = 1
for number in numbers:
    if number != 0:
        print(accumulatedProduct/number)
    else:
        print("Broken")
"""
""""
for number in numbers:
    accumulatedProduct *= number
    #print(accumulatedProduct)
    rightProduct.append(accumulatedProduct)
"""




