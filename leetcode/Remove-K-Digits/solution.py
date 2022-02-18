class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        
        stack = []
        for n in num:
            if len(stack) == 0:
                stack.append(n)
            else:
                if k == 0:
                    stack.append(n)
                else:
                    if stack[-1] > n:
                        while len(stack) > 0 and k > 0:
                            last = stack.pop()
                            if last > n:
                                k -= 1
                            else:
                                stack.append(last)
                                break
                        stack.append(n)
                    else:
                        stack.append(n)
        
        if k != 0:
            while k != 0:
                last = stack.pop()
                prev = stack.pop()
                if last < prev:
                    stack.append(last)
                else:
                    stack.append(prev)
                k -= 1
                
        first = stack[0]
        while first == "0":
            stack.pop(0)
            if len(stack) > 0:
                first = stack[0]
            else:
                break
        
        result = ""
        if len(stack) == 0:
            return "0"
        else:
            result = "".join(stack)
        
        return result