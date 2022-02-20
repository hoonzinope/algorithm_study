class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        temp_list = []
        
        intervals = sorted(intervals, key = lambda x : (x[1]-x[0]), reverse=True)
        
        for interval in intervals:
            if len(temp_list) == 0:
                temp_list.append(interval)
            else:
                insert_flag = True
                for temp in temp_list:
                    if temp[0] <= interval[0] and interval[1] <= temp[1]:
                        insert_flag = False
                        break
                if insert_flag == True:
                    temp_list.append(interval)
        
        return len(temp_list)