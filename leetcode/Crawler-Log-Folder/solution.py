class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        temp = []
        for log in logs:
            if log == "../":
                if len(temp) > 0:
                    temp.pop()
            elif log == "./":
                continue
            else:
                temp.append(log)
        
        return len(temp)