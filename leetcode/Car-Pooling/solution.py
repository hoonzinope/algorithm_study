class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        temp = [0] * 1000
        for trip in trips:
            psg = trip[0]
            start = trip[1]
            end = trip[2]
            for idx in range(start-1,end-1):
                temp[idx] += psg
          
        if(max(temp)> capacity):
            return False
        else:
            return True