class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in nums_dict:
                j = nums_dict[remain]
                return [j, i]
            nums_dict[num] = i