class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        a = set()
        l = 0
        r = 1
        a.add(s[0])
        myMax = 1


        while r < n:
            while (l < r) and (s[r] in a):
                a.remove(s[l])
                l += 1
            a.add(s[r])
            myMax = max(myMax, r-l+1)
            r+=1
        return myMax
            

        