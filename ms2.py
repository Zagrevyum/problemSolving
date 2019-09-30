def generatelowestnumber(num: str, k: int):
    num = [i for i in num]
    while k >0:
        index = mindigit(num)
        num.pop(index)
        k -= 1
    result = ""
    for n in num:
        result += n
    return result.lstrip("0")

def mindigit(number):
    for i in range(len(number)-1):
        if int(number[i]) > int(number[i+1]):
            return i
    return i+1
print(generatelowestnumber("112", 1))
