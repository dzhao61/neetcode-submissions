class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1

        while lower <= upper:
            mid = (lower + upper) // 2
            
            if nums[mid] == target:
                return mid
            
            if (nums[lower] < nums[mid] and target <= nums[mid] and target >= nums[lower]) or (nums[lower] > nums[mid] and (target >= nums[lower] or target <= nums[mid])):
                upper = mid - 1
                print('here')
            else:
                lower = mid + 1
            
        
        return -1


        