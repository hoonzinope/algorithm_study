class Solution:
    def BinaryToDecimal(self, a:str) -> int:
        num = 0
        for index in range(len(a)-1, -1, -1):
            pos = 0
            if a[index] == "1":
                pos = 1
            # print(index, (len(a)-1 - index), (2**(len(a) - index)), pos)
            num += ( (2**(len(a)-1 - index)) * pos)
            
        return num
    
    def DecimalToBinary(self, a:int) -> str:
        num_list = []
        while True:
            if a == 0 or a == 1:
                num_list.append(str(a))
                break
            num_list.append(str(a%2))
            a = a//2
        return "".join(list(reversed(num_list)))
        
    def addBinary(self, a: str, b: str) -> str:
        a_int = self.BinaryToDecimal(a)
        b_int = self.BinaryToDecimal(b)
        # print(a_int, b_int)
        a_b = a_int + b_int
        
        return self.DecimalToBinary(a_b)