class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        bin_list = []
        for d in data:
            bin_list.append(bin(d).replace("0b","").zfill(8))
            
        def isValid(bin_sub_list):
            first = bin_sub_list[0]
            if first[0] == "0" and len(bin_sub_list):
                return True
            elif first[0:3] == "110":
                if len(bin_sub_list) != 2:
                    return False
                for sub in bin_sub_list[1:]:
                    if sub[0:2] != "10":
                        return False
                return True
            elif first[0:4] == "1110":
                if len(bin_sub_list) != 3:
                    return False
                for sub in bin_sub_list[1:]:
                    if sub[0:2] != "10":
                        return False
                return True
            elif first[0:5] == "11110":
                if len(bin_sub_list) != 4:
                    return False
                for sub in bin_sub_list[1:]:
                    if sub[0:2] != "10":
                        return False
                return True
        
        while len(bin_list):
            temp_list = []
            temp_list.append(bin_list.pop(0))
            flag = False
            try:
                if temp_list[0][0] == "0":
                    flag = isValid(temp_list)
                elif temp_list[0][0:3] == "110":
                    temp_list.append(bin_list.pop(0))
                    flag = isValid(temp_list)
                elif temp_list[0][0:4] == "1110":
                    temp_list.append(bin_list.pop(0))
                    temp_list.append(bin_list.pop(0))
                    flag = isValid(temp_list)
                elif temp_list[0][0:5] == "11110":
                    temp_list.append(bin_list.pop(0))
                    temp_list.append(bin_list.pop(0))
                    temp_list.append(bin_list.pop(0))
                    flag = isValid(temp_list)
            except:
                return False
            
            if flag == False:
                return False
        return True