class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        num_dict = {}
        for a in arr:
            if a not in num_dict:
                num_dict[a] = 1
            else:
                num_dict[a] += 1
        
        length = len(arr)
        num_list = sorted([[num, val] for num, val in num_dict.items()], key = lambda x : x[1], reverse=True)
        total = 0
        count = 0
        for num_info in num_list:
            total += num_info[1]
            count += 1
            if total >= length//2:
                return count
        return count