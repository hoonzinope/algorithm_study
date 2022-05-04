class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        temp_dict = {}
        for num in nums:
            if num > k:
                continue
                
            if num not in temp_dict:
                temp_dict[num] = 1
            else:
                temp_dict[num] += 1
                
        count = 0
        for key in temp_dict:
            if temp_dict[key] == 0:
                continue
            else:
                if (k - key) in temp_dict:
                    if key == k-key:
                        count += temp_dict[key]//2
                        temp_dict[key] %= 2
                    else:    
                        if temp_dict[key] > temp_dict[k-key]:
                            count += temp_dict[k - key]

                            temp_dict[key] -= temp_dict[k-key]
                            temp_dict[k-key] = 0
                        else:
                            count += temp_dict[key]

                            temp_dict[k-key] -= temp_dict[key]
                            temp_dict[key] = 0
        return count