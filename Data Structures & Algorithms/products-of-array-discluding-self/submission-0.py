class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        out = []
        zeroes = 0

        for i in nums:
            if i != 0:
                prod *= i
            else:
                zeroes += 1
            if zeroes >= 2:
                return [0] * len(nums)

        if zeroes == 1:
            for i in nums:
                if i == 0:
                    out.append(int(prod))
                else:
                    out.append(0)
        else:
            for i in nums:
                out.append(int(prod/i))
        
        return out
        