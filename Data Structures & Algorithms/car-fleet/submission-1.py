class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(position)
        sortedCars = sorted([(position[i], speed[i]) for i in range(n)])
        stack = []

        for car in sortedCars:
            arrival = (target - car[0]) / car[1]

            while stack and stack[-1] <= arrival:
                stack.pop()
            stack.append(arrival)
        
        return len(stack)


        