class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            complement = target - num
            j = nums_dict.get(complement)
            if i == j:
                continue
            if j:
                return [i, j]