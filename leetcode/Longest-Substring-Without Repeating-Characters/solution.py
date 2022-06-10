class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        prev = []
        for n in s:
            # print(prev, n)
            if len(prev) == 0:
                prev.append(n)
                if len(prev) > max_length:
                    max_length = len(prev)
            else:
                if n not in prev:
                    prev.append(n)
                    if len(prev) > max_length:
                        max_length = len(prev)
                else:
                    index = prev.index(n)
                    prev= prev[index+1:]
                    prev.append(n)
        return max_length