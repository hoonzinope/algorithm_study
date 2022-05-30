class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        temp_list = []
        for word in words:
            temp_list.append([set(word), len(word)])
            
        max_count = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                else:
                    if len(set(temp_list[i][0]).intersection(temp_list[j][0])) > 0:
                        continue
                    else:
                        if max_count < temp_list[i][1] * temp_list[j][1]:
                            max_count = temp_list[i][1] * temp_list[j][1]
                            
        return max_count