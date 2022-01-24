class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        first_letter_upper = word[0].isupper()
        
        if first_letter_upper == True:
            count = 0
            for w in word[1:]:
                if w.isupper():
                    count+=1
            if count == len(word)-1 or count == 0:
                return True
            else:
                return False
        else:
            count = 0
            for w in word:
                if w.isupper():
                    return False
            return True
            