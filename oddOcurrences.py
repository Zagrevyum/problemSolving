
def solution(n):
    count = {}
    for i in n:
        if count.get(i):
            count.pop(i)
        else:
            count[i] = 1

    for i in count:
        return i