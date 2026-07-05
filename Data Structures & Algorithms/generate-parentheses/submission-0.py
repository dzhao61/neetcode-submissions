class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        curr = []

        def dfs(i, curr, op, cl):
            if cl > op or cl > n or op > n:
                return
            if i == n * 2:
                res.append(curr.copy())
                return

            curr.append('(')
            dfs(i+1, curr, op+1, cl)
            curr.pop()
            curr.append(')')
            dfs(i+1, curr, op, cl+1)
            curr.pop()
            return
        
        dfs(0,curr,0,0)
        res = ["".join(i) for i in res]
        print(res)
        return res

        