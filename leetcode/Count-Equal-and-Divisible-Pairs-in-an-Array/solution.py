class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        num_dict = {}
        for i in range(len(nums)):
            if nums[i] not in num_dict:
                num_dict[nums[i]] = [i]
            else:
                num_dict[nums[i]].append(i)
        count = 0
        for num in num_dict.keys():
            index_list = num_dict[num]
            for i in range(len(index_list)):
                for j in range(i+1, len(index_list)):
                    if (index_list[i] * index_list[j]) % k == 0:
                        count+=1
        return count