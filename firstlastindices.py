class Solution:
    def getRange(self, arr, target):
        min = -1
        max = -1
        for index, num in enumerate(arr):
            if target == num and min == -1:
                min = index
            if min != -1 and target != num:
                max = index - 1
                break
        return [min, max]

# Fill this in.

# Test program
arr = [1, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]