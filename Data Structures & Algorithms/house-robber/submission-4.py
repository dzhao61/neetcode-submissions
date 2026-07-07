class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        res = [0] * n
        res[0] = nums[0]
        
        for i in range(1, n):
            res[i] = max(nums[i] + res[i-2], res[i-1])
        
        return max(res[-1], res[-2])
        
        