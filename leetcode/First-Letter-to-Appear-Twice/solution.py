class Solution:
    def repeatedCharacter(self, s: str) -> str:
        al_dict = {}
        for i,e in enumerate(s):
            if e not in al_dict:
                al_dict[e] = 1
            else:
                al_dict[e] += 1
                
                for al in al_dict:
                    if al_dict[al] == 2:
                        return al
                    