class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def binSearch(nums, num_tuple):
            left = 0
            right = len(nums)
            
            while left < right:
                mid = (left+right)//2
                if nums[mid][0] == num_tuple[0]:
                    return mid
                else:
                    if nums[mid][0] < num_tuple[0]:
                        left = mid+1
                    else:
                        right = mid
            return left
        
        temp_list = []
        for i, point in enumerate(points):
            ed = (point[0]**2+point[1]**2)**1/2
            index = binSearch(temp_list, (ed, i))
            temp_list.insert(index, (ed, i))
        
        result = []
        for tu in temp_list[:k]:
            result.append(points[tu[1]])
        return result