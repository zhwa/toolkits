class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 1
        L = len(nums)
        if L == 0: return 0
        known = nums[0]
        for i in range(1, L):
            if nums[i] != known:
                known = nums[i]
                nums[num] = nums[i]
                num += 1
        return num
