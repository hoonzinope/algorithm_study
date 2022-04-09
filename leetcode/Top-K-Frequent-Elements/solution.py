class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        temp_dict = {}
        for num in nums:
            if num in temp_dict:
                temp_dict[num] += 1
            else:
                temp_dict[num] = 1
                
        temp_list = []
        for key, value in temp_dict.items():
            temp_list.append([key, value])
            
        temp_list = sorted(temp_list, key= lambda x : x[1], reverse=True)
        return [x[0] for x in temp_list[:k]]