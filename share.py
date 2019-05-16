def solution(T):
    # write your code in Python 3.6
    toGive = len(T)//2
    count = {}
    result = 0
    for i in T:
        if count.get(i):
            if toGive > 0:
                toGive -= 1
            else:
                count[i] += 1
        else:
            count[i] = 1
            result += 1

    for i in count:
        if toGive > 0:
            count[i] = 0
            result -= 1
            toGive -= 1
        else:
            return result



print(solution([80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]))

print(solution([3, 4, 7, 7, 6, 6]))