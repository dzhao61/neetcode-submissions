class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        myFreq = [[] for i in range(n)]
        mySet = dict()
        outK = []
        count = 0

        for i in nums:
            if i in mySet:
                mySet[i] += 1
            else:
                mySet[i] = 1
        
        for key, val in mySet.items():
            myFreq[val-1].append(key)

        for i in range(n-1, -1, -1):

            if len(myFreq[i]) != 0:
                for j in myFreq[i]:
                    outK.append(j)
                    count += 1
            if count == k:
                return outK
        
        return outK



            

        

        