class Solution:
  def moveZeros(self, nums):
    # Fill this in.
    index = 0
    k = 0
    for num in nums:
        if num > 0:
            k += 1
    count = 0
    while index < len(nums)-1 and count < k:

        if nums[index] == 0:
            #print(index)
            nums.pop(index)
            index -= 1
            nums.append(0)
        else:
            count += 1
        index += 1
    return nums






nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
assert nums == [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]