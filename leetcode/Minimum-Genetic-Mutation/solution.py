class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def checkMu(a, b):
            count = 0
            for x,y in zip(a,b):
                if x != y:
                    count += 1
                    if count > 1:
                        return False
            if count == 1:
                return True
            else:
                return False
        answer = 0
        flag = False
        mu_list = [start]
        while len(mu_list) > 0:
            temp_list = []
            for mu in mu_list:
                for b in bank:
                    if checkMu(mu, b) and b not in temp_list:
                        temp_list.append(b)
            for t in temp_list:
                bank.remove(t)
            
            answer += 1            
            if end in temp_list:
                flag = True
                break
            else:
                mu_list = temp_list
        if flag == False:
            answer = -1
        return answer