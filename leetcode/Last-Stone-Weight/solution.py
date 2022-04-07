class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        elif len(stones) == 1:
            return stones[0]
        else:
            temp = sorted(stones, reverse = True)
            while len(temp) >= 2:
                y = temp.pop(0)
                x = temp.pop(0)
                # print(y,x,temp)
                if y == x:
                    continue
                else:
                    if len(temp) == 0:
                        temp.append(y-x)
                        continue
                        
                    if temp[0] <= y-x:
                            temp.insert(0, y-x)
                    elif temp[len(temp)-1] >= y-x:
                        temp.append(y-x)
                    else:
                        for i in range(len(temp)-1, -1, -1):
                            if temp[i] >= y-x :
                                temp.insert(i+1, y-x)
                                break
                    
                    # print(temp)
            return self.lastStoneWeight(temp)