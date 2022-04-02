class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        index_list = []
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                index_list.append(len(s)-1-i)
                index_list.append(i)
                break
                
        if len(index_list) == 0:
            return True
        else:
            result_list = []
            for index in index_list:
                temp_s = s[:index]+s[index+1:]
                result = True
                for i in range(len(temp_s)//2):
                    if temp_s[i] != temp_s[len(temp_s)-1-i]:
                        result = False
                        break
                result_list.append(result)
            for result in result_list:
                if result == True:
                    return True
            return False
                                