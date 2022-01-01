class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for index in range(len(s)-1, -1, -1):
            if s[index] != " ":
                count+=1
                if s[index-1] == " ":
                    return count
        return count