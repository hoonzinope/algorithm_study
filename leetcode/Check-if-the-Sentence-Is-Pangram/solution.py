class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        temp = [0 for i in range(26)]
        for s in sentence:
            temp[ord(s)-ord('a')] = 1
            
        if sum(temp) == len(temp):
            return True
        else:
            return False