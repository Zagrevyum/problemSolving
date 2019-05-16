class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_copy = nums.copy()
        for i in range (0,len(nums)):
            nums[(i-k)] = nums_copy[i]

        print(nums)



solved = Solution()
nums =[1,2,3,4,5,6,7]
solved.rotate(nums,3)

