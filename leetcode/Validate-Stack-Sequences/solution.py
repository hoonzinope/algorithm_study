class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        temp_list = []
        while True:
            if len(pushed) == 0 and len(popped) == 0:
                return True
            
            if len(temp_list) == 0:
                if len(pushed) > 0:
                    num = pushed.pop(0)
                    temp_list.append(num)
                    
            if temp_list[-1] == popped[0]:
                temp_list.pop()
                popped.pop(0)
            else:
                if len(pushed) > 0:
                    num = pushed.pop(0)
                    temp_list.append(num)
                else:
                    return False
