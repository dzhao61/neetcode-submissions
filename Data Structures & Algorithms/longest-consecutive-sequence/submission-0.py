class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myNums = set(nums)
        heads = []

        for i in nums:
            if i-1 not in myNums:
                heads.append(i)
        
        maxCount = 0
        for i in heads:
            count = 1
            j = 1
            while (i + j in myNums):
                count += 1
                j += 1
            if count > maxCount:
                maxCount = count

        return maxCount
            

            

        