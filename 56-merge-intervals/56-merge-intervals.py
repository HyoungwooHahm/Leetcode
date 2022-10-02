class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mi=[]
        intervals.sort()
        
        for i in range(len(intervals)):
            if mi == []:
                mi.append(intervals[i])
            else:
                if mi[-1][1]>= intervals[i][0]:
                    mi[-1][1] = max(mi[-1][1],intervals[i][1])
                else:
                    mi.append(intervals[i])
        return mi