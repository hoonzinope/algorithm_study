class Solution:
    def dictCreate(self, s):
        temp_dict = {}
        for n in s:
            if n in temp_dict:
                temp_dict[n] += 1
            else:
                temp_dict[n] = 1
        return temp_dict
    
    def dictCompare(self, dict1, dict2):
        if len(set(dict1.keys()) - set(dict2.keys())) == 0 and len(set(dict2.keys()) - set(dict1.keys())) == 0:
            for key in dict1.keys():
                if dict1[key] != dict2[key]:
                    return False
            return True
        else:
            return False
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_dict = self.dictCreate(s1)
        
        index_list = []
        for key in s1_dict.keys():
            index_list.extend([i for i in range(len(s2)) if s2.startswith(key, i)])
            
        for i in index_list:
            alpha = s2[i]
            if alpha in s1:
                s2_dict = self.dictCreate(s2[i:i+len(s1)])
                if self.dictCompare(s1_dict, s2_dict):
                    return True
        return False