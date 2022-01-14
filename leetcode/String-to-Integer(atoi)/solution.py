class Solution:
    def myAtoi(self, s: str) -> int:
        num_list = [ str(n) for n in range(0, 10) ]
        op_list = ["+","-"]
        num_str = ""
        neg_flag = False
        
        s = s.strip()
        print(s)
        try:
            num = int(s)
            
            if num > 2**31 -1:
                num = 2**31-1
            if num < 2**31 * -1:
                num = 2**31 * -1
            print("hi9")  
            return num
        except:
            pass
        
        if len(s) == 0:
            return 0
        if s[0] not in num_list and s[0] not in op_list and s[0] != " ":
            print("hi000")
            return 0
        else:
            for index, n_str in enumerate(s):
                if n_str == " ":
                    if index+1 < len(s) and s[index+1] in num_list:
                        if len(n_str) == 0:
                            return 0
                        else:
                            break
                    continue
                if n_str == "-":
                    neg_flag = True
                    if index-1 >= 0 and s[index-1] in num_list:
                        print("hi")
                        if len(n_str) == 0:
                            return 0
                        else:
                            break
                    elif index+1 < len(s) and s[index+1] not in num_list:
                        print("bye")
                        if len(n_str) == 0:
                            return 0
                        else:
                            break
                    continue
                if n_str == "+":
                    neg_flag = False
                    if index-1 >= 0 and s[index-1] in num_list:
                        print("hi2")
                        if len(n_str) == 0:
                            return 0
                        else:
                            break
                    elif index+1 < len(s) and s[index+1] not in num_list:
                        print("hi3")
                        if len(n_str) == 0:
                            return 0
                        else:
                            break
                    continue
                if n_str in num_list:
                    num_str += n_str
                    if index+1 < len(s) and s[index+1] not in num_list:
                        break
                else:
                    break
               
            if len(num_str) == 0:
                return 0
            num = int(num_str)
            if neg_flag:
                num = num * -1
            
            
            if num > 2**31 -1:
                num = 2**31-1
            if num < -2**31:
                num = -2**31
            
            return num