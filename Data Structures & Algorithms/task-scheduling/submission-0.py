import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        timeoutHeap = []
        freq = {}

        for i in tasks:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        freq = list(freq.values())
        freq = [-i for i in freq]
        heapq.heapify(freq)

        print(freq)

        while freq or timeoutHeap:
            if freq:
                item = -1 * heapq.heappop(freq)
                if item > 1:
                    heapq.heappush(timeoutHeap, (time + n, item-1))
            
            while timeoutHeap and timeoutHeap[0][0] == time:
                heapq.heappush(freq, -timeoutHeap[0][1])
                heapq.heappop(timeoutHeap)
            
            print(freq, timeoutHeap)
            time += 1
        
        return time




        



