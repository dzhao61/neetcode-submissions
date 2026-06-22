class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        water = [0] * n

        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]

        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])
            rightMax[n-i-1] = max(rightMax[n-i], height[n-i-1])

        for i in range(1, n - 1):
            water[i] = max(min(leftMax[i-1], rightMax[i+1]) - height[i], 0)
        
        print(leftMax)
        print(rightMax)
        print(water)
        
        return sum(water)


            

        

            
            
                
        