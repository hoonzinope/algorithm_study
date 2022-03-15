class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        bra_list = []
        alpha_list = []
        for alpha in s:
            if alpha == ")":
                if len(bra_list) and bra_list[-1] == "(":
                    bra_list.pop()
                    alpha_list.append(alpha)
                else:
                    continue
            elif alpha == "(":
                bra_list.append(alpha)
                alpha_list.append(alpha)
            else:
                alpha_list.append(alpha)
        
        result = "".join(alpha_list)
        result = result[::-1]
        for i in range(bra_list.count("(")):
            result = result.replace("(","",1)
            
        return result[::-1]