class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 1:
            return s
        
        def oddPali(i):
            l = i - 1
            r = i + 1
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    return s[l+1:r]
                l -= 1
                r += 1
            return s[l+1:r]
        
        def evenPali(i):
            l = i-1
            r = i
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    return s[l+1:r]
                l -= 1
                r += 1
            return s[l+1:r]

        maxLen = 0
        maxStr = ""
        for i in range(1, n):
            odd = oddPali(i)
            even = evenPali(i)

            if len(even) > maxLen:
                maxLen = len(even)
                maxStr = even
            if len(odd) > maxLen:
                maxLen = len(odd)
                maxStr = odd
        
        return maxStr
