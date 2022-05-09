class Solution:
    def dfs(self, temp_dict, index, digits):
        if index == len(digits)-1:
            return temp_dict[digits[index]]
        else:
            result = []
            child = self.dfs(temp_dict, index+1, digits)
            curr = temp_dict[digits[index]]
            for n in curr:
                for c in child:
                    result.append(n+c)
            return result
        
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        temp_dict = {}
        temp_dict[2] = "abc"
        temp_dict[3] = "def"
        temp_dict[4] = "ghi"
        temp_dict[5] = "jkl"
        temp_dict[6] = "mno"
        temp_dict[7] = "pqrs"
        temp_dict[8] = "tuv"
        temp_dict[9] = "wxyz"
        
        for key in temp_dict:
            temp_dict[key] = [n for n in temp_dict[key]]
        
        digits = [int(n) for n in digits]
        # digits = sorted(digits)
        
        result = self.dfs(temp_dict, 0, digits)
        return result