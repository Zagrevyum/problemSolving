class EncodingString:
    def encoding(self, string):
        count = 1
        result = ""
        for index in range(len(string)-1):
            if index+1 == len(string)-1:
                if string[index] == string[index+1]:
                    count += 1
                    result = result + str(count) + string[index + 1]
                    continue
                else:
                    result = result + str(count) + string[index]
                    count = 1
                    result = result + str(count) + string[index + 1]
            else:
                if string[index] != string[index + 1]:
                    result = result + str(count) + string[index]
                    count = 1
                    continue
            count += 1
        return result

    def decoding(self, string):
        result = ""
        for index in range(0,len(string),2):
            index2 = int(string[index])
            while index2 > 0:
                result = result + string[index+1]
                index2 -= 1
        return result




solved = EncodingString()

print(solved.encoding("AAAABBBCCDAAAADED"))
print(solved.decoding("4A3B2C1D4A1D1E1D"))