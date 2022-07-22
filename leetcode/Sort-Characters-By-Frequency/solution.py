class Solution:
    def frequencySort(self, s: str) -> str:
        temp_dict = {}
        for n in s:
            if n not in temp_dict:
                temp_dict[n] = 1
            else:
                temp_dict[n] += 1
        temp_list = []
        for key, value in temp_dict.items():
            temp_list.append([key, value])
        temp_list = sorted(temp_list, key=lambda x : x[1], reverse=True)
        
        answer = ""
        for info in temp_list:
            answer += info[0]*info[1]
        
        return answer