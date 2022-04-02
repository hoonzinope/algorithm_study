class Solution:
    def pal(self, word):
        for i in range(len(word)//2):
            if word[i] != word[len(word)-1-i]:
                return False
        return True
        
    def firstPalindrome(self, words: List[str]) -> str:
        
        for word in words:
            if self.pal(word):
                return word
        return ""