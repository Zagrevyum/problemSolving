def mergeintervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    index = 0
    mergedintervals = list()
    while index < len(intervals) -1:
        interval = intervals[index]
        nextinterval = intervals[index+1]
        if nextinterval[0] < interval[1] < nextinterval[1]:
            mergedintervals.append(interval[0], nextinterval[1])
        index += 1
    return mergedintervals


