class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = dict()

        for i in range(len(strs)):
            if str(sorted(strs[i])) in myDict:
                myDict[str(sorted(strs[i]))].append(strs[i])
            else:
                myDict[str(sorted(strs[i]))] = [strs[i]]
        
        return list(myDict.values())

        