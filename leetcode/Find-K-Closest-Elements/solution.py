class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        temp_arr = [(abs(a-x), a) for a in arr]
        temp_arr = sorted(temp_arr, key = lambda x : (x[0],x[1]))
        temp_arr = sorted([a[1] for a in temp_arr[:k][::-1]])
        return temp_arr
