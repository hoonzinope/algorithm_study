class Solution:
    def dictCompare(self, dict1, dict2):
        dict1_keySet = set(dict1.keys())
        dict2_keySet = set(dict2.keys())
        
        if len(dict1_keySet - dict2_keySet) == 0 and len(dict2_keySet - dict1_keySet) == 0:
            for key in dict1.keys():
                if dict1[key] != dict2[key]:
                    return False
            return True
        else:
            return False
        
    def buildDict(self, s):
        temp_dict = dict()
        for al in s:
            if al in temp_dict:
                temp_dict[al] += 1
            else:
                temp_dict[al] = 1
        return temp_dict
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        p_len = len(p)
        dict1 = self.buildDict(p)
        
        dict2 = {}
        for i in range(0, len(s) - p_len + 1):
            part_s = s[i:i+p_len]
            if i == 0:
                dict2 = self.buildDict(part_s)
            else:
                dict2[s[i-1]] -= 1
                if dict2[s[i-1]] == 0:
                    del dict2[s[i-1]]
                    
                if part_s[-1] in dict2:
                    dict2[part_s[-1]] += 1
                else:
                    dict2[part_s[-1]] = 1
            if self.dictCompare(dict1, dict2):
                answer.append(i)
        
        return answer