class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        res = [0] * n
        res[1] = nums[1]

        for i in range(2, n):
            res[i] = max(res[i-2] + nums[i], res[i-1])

        print(res)
        ans1 = res[-1]

        res = [0] * n
        res[0] = nums[0]

        for i in range(1, n-1):
            res[i] = max(res[i-2] + nums[i], res[i-1])
        
        print(res)
        ans2 = res[-2]
        
        return max(ans1, ans2)