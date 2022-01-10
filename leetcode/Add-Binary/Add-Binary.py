class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        
        if len(a) > len(b):
            b += "0"*(len(a)-len(b))
        else:
            a += "0"*(len(b)-len(a))
        
        add_num = 0
        str_num = []
        for x,y in zip(a,b):
            x = int(x)
            y = int(y)
            if add_num + x + y == 3:
                str_num.append("1")
                add_num = 1
            elif add_num + x + y == 2:
                str_num.append("0")
                add_num = 1
            elif add_num + x + y == 1:
                str_num.append("1")
                add_num = 0
            else:
                str_num.append("0")
                add_num = 0
        if add_num != 0:
            str_num.append("1")
        
        str_num = "".join(str_num)[::-1]
        return str_num