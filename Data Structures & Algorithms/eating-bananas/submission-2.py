class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)
        smallest = (lower + upper) // 2

        while (lower <= upper):
            mid = (lower + upper) // 2
            time = 0
            for i in piles:
                time += (i-1) // mid + 1
            
            if time > h:
                lower = mid + 1
            else:
                smallest = mid
                upper = mid - 1
        return smallest
