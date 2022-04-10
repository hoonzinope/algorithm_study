class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        temp = []
        for op in ops:
            if op == "C":
                temp.pop()
            elif op == "D":
                temp.append(temp[-1]*2)
            elif op == "+":
                temp.append(temp[-2] + temp[-1])
            else:
                temp.append(int(op))
        return sum(temp)