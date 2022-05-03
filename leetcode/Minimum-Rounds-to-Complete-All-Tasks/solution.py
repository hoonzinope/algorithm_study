class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        num_dict = {}
        for n in tasks:
            if n not in num_dict:
                num_dict[n] = 1
            else:
                num_dict[n] += 1
        
        
        count = 0
        for n in num_dict:
            a = num_dict[n]
            while a >= 2:
                if a % 2 == 0 and a % 3 == 0:
                    a -= 3
                    count += 1
                elif a % 2 == 0:
                    a -= 2
                    count += 1
                else:
                    a -= 3
                    count += 1
            if a != 0:
                return -1
        return count