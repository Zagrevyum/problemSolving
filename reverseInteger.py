class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        −231,  231 − 1
        """
        if x > 0:
            reverse = int((str(x)[::-1]))
        else:
            reverse = int((str(x*-1)[::-1]))*-1

        if reverse < -(2**31) or reverse > (2**31)-1:
            return 0
        else:
            return reverse




solved = Solution()

print(solved.reverse(132450))
print(solved.reverse(-132450))
print(solved.reverse(1534236469))

