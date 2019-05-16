class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        symbols ={
            "I":  1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000

        }
        for index in range(0, len(s)-1):
            if symbols[s[index]] < symbols[s[index+1]]:
                result -= symbols[s[index]]
            else:
                result += symbols[s[index]]
        return result + symbols[s[len(s)-1]]

solved = Solution()

print(solved.romanToInt("LVIII"))

print(solved.romanToInt("MCMXCIV"))
print(solved.romanToInt("MMMCDXC"))

