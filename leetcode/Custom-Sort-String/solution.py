class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        order_dict = {}
        for i, o in enumerate(order):
            order_dict[o] = i
        
        a = []
        index = []
        for i, al in enumerate(s):
            if al in order:
                a.append(al)
                index.append(i)
        
        a = sorted(a, key = lambda x : order_dict[x])
        
        s = [al for al in s]
        for i, a in zip(index, a):
            s[i] = a
        s = "".join(s)
        return s