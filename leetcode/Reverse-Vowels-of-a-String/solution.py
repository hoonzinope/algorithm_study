class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [n for n in s]
        
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        index = []
        for i in range(len(s)):
            if s[i] in vowels:
                index.append(i)
        
        temp = ""
        for i in range(len(index)//2):
            temp = s[index[i]]
            s[index[i]] = s[index[len(index)-1-i]]
            s[index[len(index)-1-i]] = temp
        
        return "".join(s)