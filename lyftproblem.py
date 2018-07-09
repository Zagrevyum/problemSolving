import operator
from itertools import accumulate
numbers = [2, 3, 4, 5, 0, 6]
initialProductValue = [1]
leftProduct = initialProductValue + (list(accumulate(numbers, operator.mul)))
numbers.reverse()
rightProduct = initialProductValue + (list(accumulate(numbers, operator.mul)))
numbers.reverse()
leftProduct.pop()
rightProduct.pop()
rightProduct.reverse()
for number in range(len(numbers)):
    print(leftProduct[number] * rightProduct[number])


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




