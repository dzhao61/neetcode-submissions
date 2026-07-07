class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [0] * n
        
        def recur(i):
            res = 0
            if i == n:
                return 1
            if memo[i] != 0:
                return memo[i]
            if s[i] == '0':
                return 0
            if 1 <= int(s[i]) <= 9:
                res += recur(i+1)
            if 10 <= int(s[i:i+2]) <= 26:
                res += recur(i+2)
            
            memo[i] = res
            return res
        
        return recur(0)
