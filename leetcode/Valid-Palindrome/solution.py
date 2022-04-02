class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        else:
            s = [n for n in s.lower().replace(" ","")]
            index = 0
            while index < len(s):
                if s[index].isalnum():
                    index+=1
                else:
                    s.pop(index)
            for i in range(len(s)//2):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True