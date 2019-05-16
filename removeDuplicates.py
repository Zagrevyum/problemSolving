class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenght = len(nums)-1
        index = 0
        while index < lenght:
            #print(index, lenght)
            if nums[index] == nums[index+1]:
                nums.pop(index)
                lenght -= 1
                index -= 1
            index +=1
        return len(nums)


    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for num in nums:
            print(nums[index], num)
            if num != nums[index]:
                nums[index+1] = num
                index += 1
        return index


solved = Solution()
nums =[0,0,1,1,1,2,2,3,3,3]
nums2 =[0,0,1,1,1,2,2,3,3,4]
print(solved.removeDuplicates(nums))
print(solved.removeDuplicates2(nums2))
print (nums)
print (nums2)
