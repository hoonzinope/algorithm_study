class Solution:
    def numSteps(self, s: str) -> int:
        
        count = 0
        s = [int(n) for n in s]
        while len(s) != 1:
            s.reverse()
            add_num = 0
            if s[0] == 1:
                add_num = 1
                for i in range(len(s)):
                    if add_num == 1:
                        if s[i] == 0:
                            s[i] = add_num
                            add_num = 0
                        else:
                            s[i] = 0
                            add_num = 1
                if add_num == 1:
                    s.append(1)
            else:
                s = s[1:]
            s.reverse()
            count += 1
        return count