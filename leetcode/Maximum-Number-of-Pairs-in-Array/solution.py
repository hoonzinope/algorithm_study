class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        temp_dict = {}
        for num in nums:
            if num not in temp_dict:
                temp_dict[num] = 1
            else:
                temp_dict[num] += 1
        
        answer = [0,0]
        for num in temp_dict:
            answer[0] += temp_dict[num]//2
            answer[1] += temp_dict[num]%2
        return answer