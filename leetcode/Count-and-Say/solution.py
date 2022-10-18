class Solution:
    def countAndSay(self, n: int) -> str:
        
        def recur(n):
            if n == 1:
                return 1
            else:
                num = recur(n-1)
                
                if num == 1:
                    return 11
                else:
                    num_string = ""
                    temp_list = []
                    for s in [s for s in str(num)]:
                        if len(temp_list) == 0:
                            temp_list.append(s)
                        else:
                            if temp_list[-1] != s:
                                num_string += str(len(temp_list))+temp_list[-1]
                                temp_list = []
                                temp_list.append(s)
                            else:
                                temp_list.append(s)
                    
                    num_string += str(len(temp_list))+temp_list[-1]
                    return int(num_string)
        return str(recur(n))