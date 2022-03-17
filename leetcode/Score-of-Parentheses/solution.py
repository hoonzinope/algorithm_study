class Solution:
    def deeper(self, s):
        # print(s)
        answer = 0
        if ")(" in s:
            temp_list = s.split(")(",1)
            for i in range(len(temp_list)):
                bra = temp_list[i]
                left = bra.count("(")
                right = bra.count(")")
                if left > right:
                    for k in range(left-right):
                        temp_list[i] += ")"
                else:
                    for k in range(right-left):
                        temp_list[i] = "("+temp_list[i]
            
            answer = 0
            for bra in temp_list:
                answer += self.deeper(bra)
        else:
            answer = 1
            answer *= (2**(s.count("(")-1))
            
        return answer   
    def scoreOfParentheses(self, s: str) -> int:
        answer = self.deeper(s)
        return answer