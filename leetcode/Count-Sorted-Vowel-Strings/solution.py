class Solution:
    
    vow = ['a','e','i','o','u']
    
    def dfs(self, step, k):
        if step == k:
            return self.vow
        else:
            temp_result = self.dfs(step+1, k)
            result = []
            for a in self.vow:
                for temp in temp_result:
                    if temp[0] >= a:
                        result.append(a+temp)
            return result
            
    def countVowelStrings(self, n: int) -> int:
        
        result = self.dfs(1, n)
        return len(result)