class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        temp_dict = {}
        for word in words:
            mos_word = ""
            for w in word:
                mos_word += mos[ord(w)-97]
            if mos_word not in temp_dict:
                temp_dict[mos_word] = 1
        return len(temp_dict.keys())