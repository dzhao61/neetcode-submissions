class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        n = len(digits)
        res = []
        curr = []

        digMap = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def dfs(i):
            if i == n:
                res.append(curr.copy())
                return
            
            for l in digMap[digits[i]]:
                curr.append(l)
                dfs(i+1)
                curr.pop()
            return
        
        dfs(0)
        res = ["".join(i) for i in res]
        return res
        