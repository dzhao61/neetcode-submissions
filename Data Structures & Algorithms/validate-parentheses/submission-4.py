class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if stack:
                    j = stack.pop()

                    if j == "(" and i != ")":
                        return False
                    elif j == "[" and i != "]":
                        return False
                    if j == "{" and i != "}":
                        return False
                else:
                    return False
        if not stack:
            return True
        else:
            return False

