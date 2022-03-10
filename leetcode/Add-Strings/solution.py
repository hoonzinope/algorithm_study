class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        n1 = num1[::-1]
        n2 = num2[::-1]
        
        result = []
        add_num = 0
        for x,y in zip(n1, n2):
            x = int(x)
            y = int(y)
            total = x+y+add_num
            if total >= 10:
                result.append(str((total)%10))
                add_num = 1
            else:
                result.append(str(total))
                add_num = 0
        
        if len(n1) > len(n2):
            for n in n1[len(n2):]:
                n = int(n)
                if add_num != 0:
                    n += add_num
                if n >= 10:
                    n = n%10
                    add_num = 1
                else:
                    add_num = 0
                n = str(n)
                result.append(n)
        else:
            for n in n2[len(n1):]:
                n = int(n)
                if add_num != 0:
                    n += add_num
                if n >= 10:
                    n = n%10
                    add_num = 1
                else:
                    add_num = 0
                n = str(n)
                result.append(n)
        
        if add_num != 0:
            result.append(str(add_num))
        return "".join(result)[::-1]