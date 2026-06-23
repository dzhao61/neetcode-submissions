class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        n = len(nums)

        if nums[r] >= nums[l]:
            return nums[l]
        
        while (l <= r):
            mid = (l+r) // 2
            print(mid, l, r)

            if nums[mid] < nums[(mid-1+n)%n] and nums[mid] < nums[(mid + 1)%n]:
                return nums[mid]
            elif nums[r] >= nums[l]:
                return nums[l]
            elif nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        