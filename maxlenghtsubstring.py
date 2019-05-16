class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = {}
        count = 0
        maxi = 0
        for char in s:
            if mem[char]:
                count = 0
                if count > maxi:
                    maxi = count
                continue
            mem[char] = 1
            count += 1

        return maxi