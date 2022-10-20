class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x : (x[0], x[1]))
        
        i = 0
        while i != len(intervals)-1:
            a = intervals[i]
            b = intervals[i+1]
            
            if b[0] <= a[1] and a[1] <= b[1]:
                intervals[i] = [a[0], b[1]]
                intervals.pop(i+1)
            elif a[0] <= b[0] and b[1] <= a[1]:
                intervals.pop(i+1)
            else:
                i += 1
        return intervals