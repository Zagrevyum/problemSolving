class Repeated:

    def findFirstRepeatedChar(self, string):
        charDict = {}
        for s in string:
            if charDict.get(s):
                return s

            charDict[s] = 1

        return None

    def findFirstUniqueChar(self, string):
        charDict = {}
        for s in string:
            if charDict.get(s):
                charDict[s] += 1
            else:
                charDict[s] = 1
        i = 0
        for s in charDict:
            if charDict[s] == 1:
                return i
            i += 1

        return -1

    def findFirstUniqueChar2(self, string):
        for s in string:
            if string.count(s) == 1:
                return string.index(s)
        return -1



solved = Repeated()

print(solved.findFirstRepeatedChar("sag1234a5g67sf"))
print(solved.findFirstUniqueChar("sag12345g67sf"))




