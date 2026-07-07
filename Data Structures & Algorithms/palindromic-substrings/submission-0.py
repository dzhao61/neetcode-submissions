class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        if n == 1:
            return 1
        
        count = 0
        
        def oddPali(i):
            count = 1
            l = i - 1
            r = i + 1
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    return count
                count += 1
                l -= 1
                r += 1
            return count
        
        def evenPali(i):
            count = 0
            l = i-1
            r = i
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    return count
                count += 1
                l -= 1
                r += 1
            return count
        
        tot = 1
        for i in range(1, n):
            tot += oddPali(i)
            tot += evenPali(i)
        
        return tot
