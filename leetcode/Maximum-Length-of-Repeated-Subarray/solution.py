class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        temp_list = []
        for i in range(len(nums1)):
            temp = []
            for j in range(len(nums2)):
                temp.append(0)
            temp_list.append(temp)
        
        max_num = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if i-1 >=0 and j-1 >=0:
                        temp_list[i][j] = temp_list[i-1][j-1] + 1
                    else:
                        temp_list[i][j] = 1
                    if temp_list[i][j] > max_num:
                        max_num = temp_list[i][j]
                else:
                    continue
        # for i in range(len(nums1)):
        #     print(temp_list[i])
        
        return max_num
        