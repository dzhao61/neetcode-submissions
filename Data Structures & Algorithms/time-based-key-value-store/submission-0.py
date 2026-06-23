class TimeMap:

    def __init__(self):
        self.myDict = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.myDict:
            self.myDict[key].append((timestamp, value))
        else:
            self.myDict[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.myDict:
            lst = list(self.myDict[key])
        else:
            return ""
        
        l = 0
        r = len(lst) - 1
        
        res = ""
        while (l <= r):
            mid = (l+r)//2

            if lst[mid][0] <= timestamp:
                res = lst[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res










