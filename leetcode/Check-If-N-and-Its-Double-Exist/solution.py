class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        num_dict = {}
        for num in arr:
            if num % 2 == 0 and num // 2 in num_dict:
                return True
            elif num * 2 in num_dict:
                return True
            if num not in num_dict:
                num_dict[num] = 1
        return False