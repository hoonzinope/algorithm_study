class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for n in s:
            if len(stack) == 0:
                stack.append([n,1])
            else:
                if stack[-1][0] == n:
                    if stack[-1][1] == k-1:
                        stack.pop()
                    else:
                        stack[-1][1] += 1
                else:
                    stack.append([n,1])
                    
        string = ""
        for s in stack:
            string += s[0]*s[1]
        return string
