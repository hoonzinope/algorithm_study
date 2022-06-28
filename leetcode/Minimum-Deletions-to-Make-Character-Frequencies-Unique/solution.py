class Solution:
    def minDeletions(self, s: str) -> int:
        al_dict = {}
        for n in s:
            if n not in al_dict:
                al_dict[n] = 1
            else:
                al_dict[n] += 1
        
        num_dict = {}
        for key, value in al_dict.items():
            if value not in num_dict:
                num_dict[value] = [key]
            else:
                num_dict[value].append(key)
                
        flag = True
        count = 0
        while flag:
            flag = False
            
            new_dict = {}
            for num, al_list in num_dict.items():
                new_dict[num] = al_list
            
            for num, al_list in num_dict.items():
                if len(al_list) > 1 and num > 0:
                    count += len(al_list)-1
                    if num-1 not in new_dict:
                        new_dict[num-1] = al_list[1:]
                    else:
                        new_dict[num-1].extend(al_list[1:])
                    new_dict[num] = al_list[:1]
                    flag = True
            num_dict = {}
            for num, al_list in new_dict.items():
                num_dict[num] = al_list
                
        return count