class Solution:

    def encode(self, strs: List[str]) -> str:
        wordLens = []
        for s in strs:
            wordLens.append(len(s))
        
        longWord = ""
        for i in range(len(strs)):
            longWord = "".join((longWord, str(wordLens[i]).zfill(3), strs[i]))
        print(longWord)
        return longWord
        



    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        strs = []

        while i < n:
            sLen = int(s[i:i+3])
            strs.append(s[i+3:i+sLen+3])
            i += sLen + 3
        return strs

            





