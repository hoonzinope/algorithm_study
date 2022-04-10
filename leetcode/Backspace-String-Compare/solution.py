class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list = []
        for n in s:
            if n == "#":
                if len(s_list) > 0:
                    s_list.pop()
            else:
                s_list.append(n)
                
        t_list = []
        for n in t:
            if n == "#":
                if len(t_list) > 0:
                    t_list.pop()
            else:
                t_list.append(n)
                
        if len(s_list) != len(t_list):
            return False
        else:
            for x,y in zip(s_list, t_list):
                if x != y:
                    return False
            
            return True