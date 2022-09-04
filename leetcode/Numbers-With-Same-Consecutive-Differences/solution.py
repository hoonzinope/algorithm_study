class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        def dfs(num, order):
            if order == n-1:
                num_list = []
                for i in range(10):
                    if abs(num-i) == k:
                        num_list.append([i])
                return num_list
            else:
                num_list = []
                for i in range(10):
                    if abs(num-i) == k:
                        temp_list = dfs(i, order+1)
                        for n_list in temp_list:
                            num_list.append([i]+n_list)
                return num_list
        
        answer = []
        for i in range(1,10):
            temp_list = dfs(i, 1)
            for n_list in temp_list:
                answer.append([i]+n_list)
        
        answer = [int("".join([str(n) for n in nums])) for nums in answer]    
        return answer