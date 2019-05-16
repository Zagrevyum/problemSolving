
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = x
        reverse = 0
        if x > 0:
            while x > 0:
                reverse = (reverse*10) + x%10
                x = x//10
        if a == reverse:
            return True
        return False

solved = Solution()
print(solved.isPalindrome(123))
print(solved.isPalindrome(121))
print(solved.isPalindrome(10))
print(solved.isPalindrome(-121))



