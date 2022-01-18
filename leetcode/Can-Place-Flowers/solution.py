class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(0,len(flowerbed)):
            if flowerbed[i] == 0:
                if len(flowerbed) == 1:
                    return True
                else:
                    if i == 0:
                        if flowerbed[i+1] != 1:
                            flowerbed[i] = 1
                            n -= 1
                    elif i == len(flowerbed)-1:
                        if flowerbed[i-1] != 1:
                            flowerbed[i] = 1
                            n -= 1
                    else:
                        if flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                            flowerbed[i] = 1
                            n -= 1
                    
        if n <= 0:
            return True
        else:
            return False