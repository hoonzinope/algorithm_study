class Solution:
    def binSub(self, bin1, bin2):
        a = len(bin1)
        
        bin_sub = [str(n) for n in bin(int("".join(bin1),2) - int("".join(bin2),2))[2:]]
        
        result = []
        if a > len(bin_sub):
            result = ["0"] * (a-1) + bin_sub
        return result
        
    def divide(self, dividend: int, divisor: int) -> int:
        end = abs(dividend)
        sor = abs(divisor)
        
        if end < sor:
            return 0
        else:
            Q = [n for n in bin(end)[2:]]
            R = ["0"] * len(Q)
            D = [n for n in bin(sor)[2:]]
            
            for i in range(len(Q)):
                R.pop(0)
                R.append(Q.pop(0))
                
                if int("".join(R),2) >= int("".join(D),2):
                    R = self.binSub(R,D)
                    Q.append("1")
                else:
                    Q.append("0")
            answer = int("".join(Q),2)
            if dividend < 0:
                answer *= -1
            if divisor < 0:
                answer *= -1
                
            if answer >= 2**31-1:
                answer = 2**31-1
            if answer < -2**31:
                answer = -2*31
            return answer