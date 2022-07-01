class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key= lambda x : x[1], reverse=True)
        
        count = 0
        for box in boxTypes:
            if truckSize >= box[0]:
                truckSize -= box[0]
                count += box[0]*box[1]
            else:
                count += truckSize * box[1]
                truckSize = 0
        return count