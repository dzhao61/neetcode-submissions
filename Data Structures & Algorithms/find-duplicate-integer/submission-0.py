class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        hasSeen = [0] * n

        for i in nums:
            if hasSeen[i] == 1:
                return i
            hasSeen[i] = 1
        
        




        