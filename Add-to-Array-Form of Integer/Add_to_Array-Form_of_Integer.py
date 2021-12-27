class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_str = "".join([str(n) for n in num])
        
        result_num = int(num_str) + k
        num_str = str(result_num)
        result = []
        for n in num_str:
            result.append(n)
        
        return result