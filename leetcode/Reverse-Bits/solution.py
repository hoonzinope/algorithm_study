class Solution:
    def reverseBits(self, n: int) -> int:
#         total = 0
#         n_list = []
#         while n > 0:
#             n_list.append(n%2)
#             n//=2
        
#         n_list.reverse()
#         if len(n_list) < 32:
#             n_list = [0]*(32-len(n_list)) + n_list
        
#         for i in range(len(n_list)):
#             total += n_list[i]* (2**i)
#         return total
    
    
        total = 0
        i = 31
        while i >= 0:
            if n > 0:
                total += (n%2)* (2**i)
                n //= 2
            else:
                total += 0
            i -= 1
        return total