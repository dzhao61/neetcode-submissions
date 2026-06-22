class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = set()

        for m in range(1, len(nums)):
            l = 0 
            r = len(nums) - 1
            while l < m and m < r:
                if nums[m] + nums[l] + nums[r] == 0:
                    res.add((nums[l], nums[m], nums[r]))
                    l += 1
                    r -= 1
                elif nums[m] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        out = [list(x) for x in list(res)]
        return out

