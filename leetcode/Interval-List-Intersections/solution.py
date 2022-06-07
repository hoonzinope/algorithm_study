class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a_index = 0
        b_index = 0
        result = []
        while a_index < len(firstList) and b_index < len(secondList):
            x1, y1 = firstList[a_index]
            x2, y2 = secondList[b_index]
            
            if x1 <= x2:
                if x1 <= x2 and y2<= y1: # include
                    result.append([x2,y2])
                    b_index+=1
                elif x2 < y1 and y1 < y2:
                    result.append([x2,y1])
                    a_index+=1
                elif y1 == x2:
                    result.append([x2,x2])
                    a_index+=1
                else:
                    a_index+=1
            else: # x1 >= x2:
                if x2 <= x1 and y1 <= y2:
                    result.append([x1,y1])
                    a_index+=1
                elif x1 < y2 and y2 < y1:
                    result.append([x1, y2])
                    b_index+=1
                elif y2 == x1:
                    result.append([x1,x1])
                    b_index+=1
                else:
                    b_index+=1
        return result