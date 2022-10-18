class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i,al in enumerate(s):
            if len(stack) == 0:
                stack.append(al)
            elif ord(al) < ord(stack[-1]):
                if al in stack:
                    continue
                    
                while ord(al) < ord(stack[-1]):
                    if stack[-1] in s[i+1:]:
                        stack.pop()
                    else:
                        break
                    if len(stack) == 0:
                        break
                stack.append(al)
            else:
                if al not in stack:
                    stack.append(al)
        return "".join(stack)                