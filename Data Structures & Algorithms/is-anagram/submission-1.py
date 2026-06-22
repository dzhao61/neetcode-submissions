class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_lst = list(t)
        for i in s:
            if i in t_lst:
                t_lst.remove(i)
            else:
                return False
        if len(t_lst) == 0:
            return True
        else:
            return False
        