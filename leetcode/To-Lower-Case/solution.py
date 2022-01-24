class Solution:
    def toLowerCase(self, s: str) -> str:
        new_s = ""
        for i in range(len(s)):
            new_s += s[i].lower()
        return new_s