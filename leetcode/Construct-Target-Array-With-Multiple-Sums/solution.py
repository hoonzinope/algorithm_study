class Solution:
    def isPossible(self, target: List[int]) -> bool:
        while target.count(1) != len(target):
            max_num = max(target)
            index = target.index(max_num)
            sum_num = sum(target[:index]+target[index+1:])
            if sum_num == 0:
                return False
            if max_num - sum_num <= 0:
                return False
            else:
                if max_num % sum_num > 0:
                    target[index] =  max_num % sum_num
                else:
                    if sum_num > 1:
                        return False
                    else:
                        target[index] = 1
        return True