class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for idx in range(len(nums)):
            table[nums[idx]] = idx + 1
        for idx in range(len(nums)):
            a = nums[idx]
            b = target - a
            if b in table and table[b] != idx + 1:
                return idx+1, table[b]
        
