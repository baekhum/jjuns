class Solution(object):
    def moveZeroes(self, nums):
        lo, hi = 0, 0
        for hi in range(len(nums)):
            if nums[hi] != 0:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
        