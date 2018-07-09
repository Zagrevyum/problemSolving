
class Solution:

    def twoSum(nums, target):

        dictionary = {}
        for index in range(len(nums)):
            try:
                dictionary[nums[index]] = [dictionary[nums[index]]]+ [index]
            except KeyError:
                dictionary [nums[index]] = index

       # print(dictionary)

        for number in nums:
            try:

                if target - number != number:
                    index1 = dictionary[number]
                    index2 = dictionary[target-number]
                    return [index1, index2]
                    break
                else:
                    try:
                        index1 = dictionary[number][0]
                        index2 = dictionary[target-number][1]
                        return [index1, index2]
                        break
                    except:
                        index1= 0
                        index2 = 0
            except KeyError:
                index1 = 0
                index2 = 0










#print(Solution.twoSum(array, 16021))

print(Solution.twoSum([3,3], 6))
