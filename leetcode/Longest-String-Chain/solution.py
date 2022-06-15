class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_dict = {}
        words = sorted(words, key=lambda x : len(x))
        for word in words:
            word_dict[word] = 1
        
        for word in words:
            for n in range(len(word)):
                new_word = word[:n]+word[n+1:]
                if new_word in word_dict:
                    if word_dict[new_word] >= word_dict[word]:
                        word_dict[word] = word_dict[new_word]+1
        max_count = 0
        for k,v in word_dict.items():
            if max_count < v:
                max_count = v
        return max_count