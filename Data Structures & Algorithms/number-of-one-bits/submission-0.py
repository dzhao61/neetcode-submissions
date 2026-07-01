class Solution:
    def hammingWeight(self, n: int) -> int:
        z = bin(n)
        print(z)
        count = 0
        for i in z:
            if i == "1":
                count += 1
        return count


        