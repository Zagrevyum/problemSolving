class Solution:
    def isValid(self, s: str) -> bool:
        charStack = []
        closingChars = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in "([{":
                charStack.append(c)
            if (closingChars.get(c)):
                if not charStack:
                    return False
                if closingChars[c] != charStack[-1]:
                    return False
                charStack.pop()
        if len(charStack) > 0:
            return False
        return True

solved = Solution()


print(solved.isValid("([)]"))

print(solved.isValid("]"))

