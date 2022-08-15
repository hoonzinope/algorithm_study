class Solution:
    def intToRoman(self, num: int) -> str:
        
        num_list = [n for n in str(num)]
        
        if len(num_list) < 4:
            for _ in range(4-len(num_list)):
                num_list = ["0"] + num_list
        answer = ""
        for i, n in enumerate(num_list):
            if n == "0":
                continue
            else:
                if i == 0:
                    answer += "M"*int(n)
                elif i == 1:
                    if n == "4":
                        answer += "CD"
                    elif n == "9":
                        answer += "CM"
                    elif int(n) < 4:
                        answer += "C" * int(n)
                    else:
                        answer += "D"+"C" * (int(n)-5)
                elif i == 2:
                    if n == "4":
                        answer += "XL"
                    elif n == "9":
                        answer += "XC"
                    elif int(n) < 4:
                        answer += "X" * int(n)
                    else:
                        answer += "L" + "X" * (int(n)-5)
                else: #i == 3
                    if n == "4":
                        answer += "IV"
                    elif n == "9":
                        answer += "IX"
                    elif int(n) < 4:
                        answer += "I" * int(n)
                    else:
                        answer += "V" + "I" * (int(n)-5)
        return answer