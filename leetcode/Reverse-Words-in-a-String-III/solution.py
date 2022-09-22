class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([term[::-1] for term in s.split(" ")])