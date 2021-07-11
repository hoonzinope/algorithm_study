class Solution:
    def isValid(self, s: str) -> bool:
        
        result = []
        
        for braket in s:
            if braket in ['{','[','(']:
                result.append(braket)
            else:
                if len(result) == 0:
                    result.append(braket)
                else:
                    if result[-1] == '{' and braket == '}':
                        result.pop()
                    elif result[-1] == '[' and braket == ']':
                        result.pop()
                    elif result[-1] == '(' and braket == ')':
                        result.pop()
                    else:
                        result.append(braket)
                    
        if len(result) != 0:
            return False
        else:
            return True