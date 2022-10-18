class Solution:
    def compress(self, chars: List[str]) -> int:
        temp_list = []
        temp_str = ""
        index = 0
        for char in chars:
            if len(temp_list) == 0:
                temp_list.append(char)
            else:
                if temp_list[-1] == char:
                    temp_list.append(char)
                else:
                    if len(temp_list) == 1:
                        temp_str += temp_list[0]
                    else:
                        temp_str += temp_list[0]+str(len(temp_list))
                    temp_list = []
                    temp_list.append(char)
                    for i in range(index, index+len(temp_str)):
                        chars[i] = temp_str[i]
                        
        if len(temp_list) == 1:
            temp_str += temp_list[0]
        else:
            temp_str += temp_list[0]+str(len(temp_list))
            
        for i in range(index, index+len(temp_str)):
            chars[i] = temp_str[i]
        
        for _ in range(len(chars)-len(temp_str)):
            chars.pop()
        return len(chars)