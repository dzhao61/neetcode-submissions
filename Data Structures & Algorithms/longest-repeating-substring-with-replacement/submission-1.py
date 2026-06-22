class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = l + 1
        longest = 1

        freqDict = dict()
        freqDict[s[l]] = 1

        while r < n:
            if s[r] in freqDict:
                freqDict[s[r]] += 1
            else:
                freqDict[s[r]] = 1
            
            while (r - l + 1) - max(freqDict.values()) > k:
                print(l, r, max(freqDict.values()))
                freqDict[s[l]] -= 1
                l += 1
            
            if r - l + 1 > longest:
                longest = r - l + 1
            
            
            r += 1


        return longest

            

            




