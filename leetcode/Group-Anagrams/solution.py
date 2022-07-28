class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp_dict= {}
        for st in strs:
            sorg = "".join(sorted(st))
            if sorg not in temp_dict:
                temp_dict[sorg] = [st]
            else:
                temp_dict[sorg].append(st)
        answer = []
        for key, value in temp_dict.items():
            answer.append(value)
        return answer